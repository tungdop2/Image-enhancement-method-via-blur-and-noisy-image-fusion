import cv2
import os
import matplotlib.pyplot as plt
from photometric_calibration import *
from fusion import *
import argparse

def enhance_image(img_name):
    short_name = img_name + '_short_exposed.jpg'
    long_name = img_name + '_long_exposed.jpg'

    short_img = cv2.imread(short_name)
    long_img = cv2.imread(long_name)

    pced_img = photometric_calibration(short_img, long_img, 'pced_' + img_name + '.jpg')

    fused_img = fusion(pced_img, pced_img, 'fused_' + img_name + '.jpg')

    return pced_img, fused_img

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_name', type=str, default='demo')
    args = parser.parse_args()
    img_name = args.img_name
    enhance_image(img_name)

