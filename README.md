# Introduction
This repository contains code for the paper: [Paper](https://www.researchgate.net/publication/224114693_Image_enhancement_method_via_blur_and_noisy_image_fusion\n)

# Usage
1. Clone this repository
2. Install required packages (with Python > 3.6):\
    `pip install -r requirements.txt`
3. Put your images to main folder, save images name as `<name>_short_exposed.jpg` and `<name>_long_exposed.jpg` correspond to short and long-exposed image respectively.
4. There are 2 ways to run the code:
    1. Simply run `!python enhance.py <name>` in your terminal
    2. Use `photometric_calibration.py` to get photometric calibrated image.  
        Use `fusion.py` to get the fusion image.  
        A guide notebook is provided in the `quickstart.ipynb` file.
5. The results are saved in `output` folder as  `pced_<name>.jpg`, `fused_<name>.jpg` and 3 `coparagram_<color>.jpg` correspond to photometric calibrated, fusion and 3 coparagrams for each channel in rgb color space respectively.

# Demo
<img src="demo_short_exposed.jpg" width="400"/> <img src="demo_long_exposed.jpg" width="400"/> 
<img src="output/pced_demo.jpg" width="400"/> <img src="output/fused_demo.jpg" width="400"/> 

*Image enhancement result: short- and long-exposed images (upper row), the photometrically calibrated short-exposed image (bottom left), and the result (bottom right).*

# Annotation
The results in this code is not exactly the same as the paper, based on the polynomial fitting and the noise varience estimation.

# Contributors
* Duong Quang Tung - 19020654
* Trang Minh Ngoc
* Le Thi My Duyen
  

