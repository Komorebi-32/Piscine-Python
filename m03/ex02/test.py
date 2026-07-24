# from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
import numpy as np


# imp = ImageProcessor()

spb = ScrapBooker()
arr1 = np.arange(0, 25).reshape(5, 5)
crop = spb.crop(arr1, (3, 1), (1, 0))
print(arr1)
print(crop)