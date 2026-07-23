import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        return (np.array(lst))

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.fromiter(itr, float)

    def from_shape(self, shape, value=0):
        """returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array, and the second
        argument specifies the value of the elements. This value must be 0 by default."""
        return np.full(shape, value)
        # find how to fill the array with same values
        # np.reshape(shape[0], shape[1])

    def random(self, shape):
        """returns an array filled with random values. It takes as an
        argument a tuple which specifies the shape of the array."""
        return np.random.rand(*shape)

    def identity(self, n):
        """returns an array representing the identity matrix of size n."""
        return np.identity(n)
