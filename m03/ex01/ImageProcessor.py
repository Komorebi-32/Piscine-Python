# import cv2


# class ImageProcessor:
#     def load(self, path):
#         img = cv2.imread(path)
#         if img is None:
#             print("Error: cannot read image")
#             return None
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         height, width, channels = img.shape
#         print(f"Loading image of dimensions {height} x {width}")
#         return img

#     def display(self, array):
#         cv2.imshow("z6400", array)

from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        try:
            img = Image.open(path)
            if img.size[0] == 0 or img.size[1] == 0:
                print("Error: empty image")
                return None
        except FileNotFoundError:
            print("Error: non existing file")
            return None
        except UnidentifiedImageError:
            print("Error: empty image")
            return None
        print(f"Loading image of dimensions {img.size[0]} x {img.size[1]}")
        arr = np.asarray(img)
        return arr

    def display(self, array):
        # Solution with Image from Pillow. It shows the image but without a frame
        # img = Image.fromarray(array)
        # img.show()

        # Solution with matplotlib
        plt.imshow(array)
        plt.axis('off')  # Turn off axis labels
        plt.show()
