import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim:   tuple of 2 integers.
        position: tuple of 2 integers.

        Returns:
        -------
        crop: the cropped numpy.ndarray.
        None:    (if the combination of parameters is not possible).

        Raises:
        ------
        This function should not raise any Exception.
        """
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not isinstance(dim, tuple)
            or len(dim) != 2
        ):
            print("Error: Wrong input parameters")
            return None
        if position[0] < 0 or position[1] < 0:
            print("Error: position coordinates must be positive")
            return None
        og_height, og_width = array.shape
        dim_height, dim_width = dim
        pos_y, pos_x = position
        if dim_height > og_height - pos_y:
            print("Crop dimension alongside height is too big. Cropping to the end of the image")
            dim_height = og_height - pos_y
        if dim_width > og_width - pos_x:
            print("Crop dimension alongside width is too big. Cropping to the end of the image")
            dim_width = og_width - pos_x
        # crop = array[position[0]:position[1], position[0] + dim[0]:position[1] + dim[1]]
        bottom_right_x = pos_x + dim_width
        bottom_right_y = pos_y + dim_height
        crop = array[pos_y:bottom_right_y, pos_x:bottom_right_x]
        return crop
