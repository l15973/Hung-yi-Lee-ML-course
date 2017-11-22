# 輸入一張圖，將圖上下顛倒，左右相反（旋轉180度）

import sys
from scipy import misc
import numpy as np

IMAGE_NAME = sys.argv[1]
raw_image = misc.imread('autumn_map-2.jpg')
flip_ud_image = np.flipud(raw_image)
flip_lr_image = np.fliplr(flip_ud_image)
misc.imsave('ans2.jpg', flip_lr_image)
