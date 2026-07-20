from datetime import datetime

kata = (2019, 9, 25, 3, 30)
dt = datetime(*kata)
# *kata means unpacking the tuple, passing all the values to datetime()
# it's equivalent to datetime(2019, 9, 25, 3, 30)

print(dt.strftime("%m/%d/%Y %H:%M"))