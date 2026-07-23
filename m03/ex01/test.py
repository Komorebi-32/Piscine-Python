from ImageProcessor import ImageProcessor

imp = ImageProcessor()

arr = imp.load("./z6400.png")
print(arr)
imp.display(arr)

arr = imp.load("non existing file")
print(arr)

arr = imp.load("./empty.png")
print(arr)
