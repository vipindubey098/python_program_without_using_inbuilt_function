numbers = [0,1,2,3,4,5,6,7,8,9]
arr = []
L = len(numbers)
print(L)
for i in range(int(L)):
    n = numbers[i]
    print(n)
    inverse_numbers = L-n-1 #10-0-1 =9, 10-1-1=8, 10-2-1=7 ....
    arr.append(inverse_numbers)

print(arr)
