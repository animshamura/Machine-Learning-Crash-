import pandas as pond

sigmas = {
  "names" : ["bale","decap","patty"],
  "casting": [1.0,1.2,1.3]
}

frame = pond.DataFrame(sigmas)
print(frame)
print()
print(frame.loc[0])
