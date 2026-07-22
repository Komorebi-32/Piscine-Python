import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        return (np.array(lst))

    def from_tuple(self, tpl):
        self.from_list(tpl)
    
    def from_iterable(self, itr):
        