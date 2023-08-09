import pandas as pond

frame = pond.read_csv('data.csv')

newFrame = frame.dropna()

print(newFrame.to_string())
