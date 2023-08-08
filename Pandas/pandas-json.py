import pandas as pond

read = pond.read_json('sigmas.json')

print(read.to_string())
