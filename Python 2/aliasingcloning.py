x=[10,20,30,40,50]
y=x
print(id(x))
print(id(y))

a=[1,2,3,4,5,6,7]
b=a[:]
b[1]=8
print(a)
print(b)

s=[5,10,4,15,6,7,50]
A=s.copy()
print(s)
print(a)
n=[10,20,30,40,50,60,70]
print(n)
n.clear()
print(n)
