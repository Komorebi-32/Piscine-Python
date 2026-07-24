import sys
sys.path.insert(0, "../ex00")

from FileLoader import FileLoader
import pandas as pandas
from YoungestFellah import youngest_fellah


fl = FileLoader()
df = fl.load("../athlete_events.csv")
print(youngest_fellah(df, 2004))
youngest_fellah(df, 2003)
