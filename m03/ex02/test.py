# from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker
import numpy as np


# imp = ImageProcessor()

spb = ScrapBooker()
# arr1 = np.arange(0, 25).reshape(5, 5)
# crop = spb.crop(arr1, (3, 1), (1, 0))
# print(arr1)
# print(crop)

# crop = spb.crop(arr1, (6, 1), (1, 0))
# print(arr1)
# print(crop)

# crop = spb.crop(arr1, (3, 6), (1, 0))
# print(arr1)
# print(crop)

# crop = spb.crop(arr1, (3, 1), (-1, 0))
# print(arr1)
# print(crop)

# crop = spb.crop(arr1, (6, 1, 3), (1, 0))
# print(arr1)
# print(crop)

arr2 = np.array("A B C D E F G H I".split() * 6)
print(arr2)
arr2 = arr2.reshape(-1, 9)
print(arr2)
thin = spb.thin(arr2, 3, 0)
print(thin)
