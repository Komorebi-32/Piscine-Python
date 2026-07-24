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

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
                (depending of axis value).
        axis: positive non null integer.

        Returns:
        -------
        new_arr: thined numpy.ndarray.
        None: (if the combination of parameters is not possible).

        Raises:
        ------
        This function should not raise any Exception.
        """
        height, width = array.shape
        if axis == 0:
            if n > width:
                print("Error: n must be lower than the number of columns")
                return None
            lines_to_delete = list(range(n - 1, width, n))
            axis_delete = 1
        elif axis == 1:
            if n > height:
                print("Error: n must be lower than the number of rows")
                return None
            lines_to_delete = list(range(n - 1, height, n))
            axis_delete = 0
        else:
            print("Error: axis must be 0 or 1")
            return None

        return np.delete(array, lines_to_delete, axis_delete)
