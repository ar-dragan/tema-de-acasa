o=int(input('primul nr='))
q=int(input('al doilea nr='))
def a(x,y):
    s=x+y
    return s
print('suma nr =',a(o,q))

def b(x,y):
    s=x*y
    return s
print('produsul nr =',b(o,q))

def c(x,y):
    s=(x+y)/2
    return s
print('media aritmetica a nr =',c(o,q))

def f(x,y):
    t=[]
    t.extend([x,y])
    m=min(t)
    return m 
print('nr minim =',f(o,q))

def g(x,y):
    t=[]
    t.extend([x,y])
    m=max(t)
    return m 
print('nr maxim =',g(o,q))

def d(x,y):
    divizor=0
    for i in range(1,(f(x,y)+1)):
        if x%i==0 and y%i==0 and i>divizor:
            divizor=i
    return divizor
print('Cel mai mare divizor comun =',d(o,q))
def e(x,y):
    multiplu=0
    for i in range(1,100):
        if i*g(x,y)%f(x,y)==0 :
            multiplu=i*g(x,y)
            return multiplu
print('cel mai mic multiplu comun =',e(o,q))

def h(x,y):
    frmt=str(x)+"+"+str(y)+"="+str(a(x,y))
    return frmt
print(h(o,q))

def i(x,y):
    frmt=str(x)+"*"+str(y)+"="+str(b(x,y))
    return frmt
print(i(o,q))

def j(x,y):
    divizori=""
    divizor=0
    for i in range(1,(f(x,y)+1)):
        if x%i==0 and y%i==0 and i>divizor:
            divizor=i
            divizori+=str(i)+" "
    return divizori
print('toti divizorii comuni:',j(o,q))

def k(x,y):
    multipli=[]
    multiplu=0
    for i in range(1,100000):
        if len(multipli)<5:
            if i*g(x,y)%f(x,y)==0 :
                multiplu=i*g(x,y)
                multipli.append(str(multiplu))
    multipli=' '.join(multipli)
    return multipli
print('5 multipli comuni:',k(o,q))

def l(x,y):
    cifre=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) in str(y):
            cifre+=str(i)+" "
    return cifre
print('cifrele care se contin in ambele nr:',l(o,q))           

def m(x,y):
    cifre=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) not in str(y):
            cifre+=str(i)+" "
    return cifre
print('cifrele care se contin doar in primul nr:',m(o,q))  

def n(x,y):
    divx=0
    divy=0
    for i in range(1,x+1):
        if x%i==0 :
            divx+=1
    for i in range(1,y+1):
        if y%i==0 :
            divy+=1   
    if divx==divy:
        d="PRIETENE"  
    else:
        d="nu sunt prietene"  
    return d
print(n(o,q))