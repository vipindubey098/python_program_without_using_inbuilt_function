c = [9, 65, 83, 36, 27]
d = []
a = 0
for i in c:
    if i != c[a]:
        d.append(i)

print(d)


# Using comprehension & enumerate:

x = [e for i,e in enumerate(c) if i!= 0]
print(x)