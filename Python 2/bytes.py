x=[10,20,30,40,50]
b=bytes(x)
print(b[1])
print(b[3])
print(b[2])
print(b[-1])
print(b[-5])
print(b[0])
for i in b : print(i)


y=[1,2,3,4,5,6,7]
b=bytearray(y)
for i in b : print(i)
b[0]=8
for i in b : print(i)

list=[10,10,"anil",True,20,30]
print(list)
print(list[0])
print(list[-1])
list[0]=1
for i in list : print(i)
t=(1,2,3,4,5)
print(t)
list.append("anil")
print(list)
list.remove("anil")
print(list)


r=range(10)
for i in r : print(i)

s={100,0,10,200,10,'durga'}
print(s)
s.add(60)
print(s)
s.remove(100)
print(s)

s={10,20,30,40,50,60,70}
fs=frozenset(s)
for i in fs : print(i)

d={1:'anil',2:'suji',3:'anil'}
d[1]='pawan'
print(d)



