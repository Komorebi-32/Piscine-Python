from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../athlete_events.csv")
fl.display(df, 32)
print("")
fl.display(df, -32)
print("")
fl.display(df, 3000000)