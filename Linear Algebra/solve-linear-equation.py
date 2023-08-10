import numpy as numby

x = numby.array([[12, 11, 10],[9, 8, 7],[6, 5, 4]])
y = numby.array([3, 2, 1])

ans =  numby.linalg.solve(x,y)

print(ans)
