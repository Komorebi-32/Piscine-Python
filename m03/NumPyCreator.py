import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        return (np.array(lst))

    def from_tuple(self, tpl):
        self.from_list(tpl)

    def from_iterable(self, itr):
        return np.fromiter(itr, float)
    
    def from_shape(self, shape, value = 0):
        # find how to fill the array with same values
        #np.reshape(shape[0], shape[1])