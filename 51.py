A = [A * 3 for A in 'abc']
print(A)
B = ['Hello', 'world!', 'qwe']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list.insert(0, '*')
        i = i + 1
        
print(B)
