import pywt
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.restoration import estimate_sigma
import pywt

def fusion(short_img, long_img, save_name):
    
    # Luminance fusion
    # estimate noise variance
    sigma = estimate_sigma(short_img, multichannel=True, average_sigmas=True)   
    # print('sigma: ', sigma)

    # image in LAB color space
    L_short, A_short, B_short = cv2.split(cv2.cvtColor(short_img, cv2.COLOR_BGR2LAB))
    L_long, A_long, B_long = cv2.split(cv2.cvtColor(long_img, cv2.COLOR_BGR2LAB))

    # apply wavelet transform for L channel
    coeffs_short = pywt.dwt2(L_short, 'bior1.3')
    coeffs_long = pywt.dwt2(L_long, 'bior1.3')

    cA_short, (cH_short, cV_short, cD_short) = coeffs_short
    cA_long, (cH_long, cV_long, cD_long) = coeffs_long

    # adjust
    dA = cA_long - cA_short
    dH = cH_long - cH_short
    dV = cV_long - cV_short
    dD = cD_long - cD_short
    wA = np.maximum(estimate_sigma(cA_short) ** 2,np.mean(dA) ** 2)
    wH = np.maximum(estimate_sigma(cH_short) ** 2,np.mean(dH) ** 2)
    wV = np.maximum(estimate_sigma(cV_short) ** 2,np.mean(dV) ** 2)
    wD = np.maximum(estimate_sigma(cD_short) ** 2,np.mean(dD) ** 2)
    
    cA_hat = cA_short + sigma ** 2 / wA * dA
    cH_hat = cH_short + sigma ** 2 / wH * dH
    cV_hat = cV_short + sigma ** 2 / wV * dV
    cD_hat = cD_short + sigma ** 2 / wD * dD
    
    # new L channel
    coeffs_hat = cA_hat, (cH_hat, cV_hat, cD_hat)
    L_new = pywt.idwt2(coeffs_hat, 'bior1.3')
    L_new = L_new.astype(np.uint8)

    # Chrominance fusion
    # short weight
    ws = (L_new/ 255) ** 6

    # adjust
    A_new = A_short * ws + A_long * (1 - ws)
    B_new = B_short * ws + B_long * (1 - ws)

    # New image in LAB color space
    # L_new = L_new.astype(np.uint8)
    # A_new = A_new.astype(np.uint8)
    # B_new = B_new.astype(np.uint8)
    
    new_img = cv2.cvtColor(short_img, cv2.COLOR_BGR2LAB).copy()
    new_img[:,:,0] = L_new
    new_img[:,:,1] = A_new
    new_img[:,:,2] = B_new

    # to BGR color space
    new_img = cv2.cvtColor(new_img, cv2.COLOR_LAB2BGR)

    # save
    cv2.imwrite('output/' + save_name, new_img)

    return new_img

