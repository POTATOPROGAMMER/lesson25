import array as arr
a=arr.array("i",[1,2,3])
print("\nthe new created aray is: " , end="")
for i in range (0,3):
    print(a[i],end="")
print()
b = arr.array("d",[2.5,3.2,3.3])
print("\nthe new created aray is: " , end="")
for i in range (0,3):
    print(b[i],end="")
a.insert(1,4)
print("\narray after insertion: " , end="")
for i in (a):
    print(i,end="")
print()


