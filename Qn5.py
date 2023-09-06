n = int(input("Enter no. of strings: "))
l = []
for i in range(n):
    s = input("Enter string:")
    l.append(s)

print("String with low>2 and same lsat char is: ")
for j in l:
    if len(j) >= 2 and j[0] == j[-1]:
        print(j)
