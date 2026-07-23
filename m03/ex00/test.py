from NumPyCreator import NumPyCreator

print("from_shape((32, 32), 32)\n")
array = NumPyCreator().from_shape((32, 32), 32)
print(array)
print("\nfrom_shape((3, 3))\n")
array = NumPyCreator().from_shape((3, 3))
print(array)
print("\nempty(4, 4)\n")
array = NumPyCreator().random((4, 4))
print(array)