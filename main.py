
#print hello world
print("hello word")

#variable
x=5
print(x)

name="ahmad zaki"
print(name)

a=10
b=20

v=a+b
w=a-b
x=a%b
y=a*b
z=a/b

print(v,w,x,y,z)

name1,name2="ahmad","zaki"
print(name1,name2)


def myfunc():
    global name
    name="ahmad zaki"
    print(name)
    
myfunc()

def kecepatan():
    jarak=float(input("masukan jarak :"))
    
    waktu=float(input("masukan waktu :"))
    
    kecepatan=jarak/waktu
    print(kecepatan)

kecepatan()