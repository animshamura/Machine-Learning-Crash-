import pandas as pond

casting = [1000000, 1200000, 1120000]

sigmas = pond.Series(casting, index = ["bale", "patty", "decap"])

print(sigmas)
