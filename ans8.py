A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) 
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted(A0.values())
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]
A7 = 10 + 23 - 45 + 33
A8 = [2 * i for i in [1, 2, 3, 4]]
A9 = [x for x in ["I", "want", "to", "learn", "python"] if len(x) > 3]

# Print the final values of A0, A1, ...An
print("A0:", A0)
print("A1:", A1)
print("A2:", A2)
print("A3:", A3)
print("A4:", A4)
print("A5:", A5)
print("A6:", A6)
print("A7:", A7)
print("A8:", A8)
print("A9:", A9)
