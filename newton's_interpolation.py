import matplotlib.pyplot as plt
def dd(start,end,y,x):
    if start != end:
        
        return (dd(start,end-1,y,x)-dd(start+1,end,y,x))/(x[0][start]-x[0][end])
    else:
        
        return y[0][start] 
  
x=list()
y=list()
out=list()
inp=list()
t=0

with open("C:/Users/User/Downloads/kagglecatsanddogs_3367a/newtoninputx.data") as f:
    lines1 = f.read().splitlines()
    for i in lines1:
        arr=list()
        arr=i.split(" ")
    x.append(arr)
    for i in range(len(x)):
        for j in range(5):
            x[i][j]=float(x[i][j])
            
with open("C:/Users/User/Downloads/kagglecatsanddogs_3367a/newtonoutputy.data") as f:
    lines1 = f.read().splitlines()
    for i in lines1:
        arr=list()
        arr=i.split(" ")
    y.append(arr)
    for i in range(len(y)):
        for j in range(5):
            y[i][j]=float(y[i][j])
print(x)
print(y)

while t <= 7:
 inp.append(t)	
 b=list()
 b.append(dd(0,3,y,x))
 i=2   
 while i >= 0:
    c=dd(0,i,y,x)
    p=c+(t-x[0][i])*b[2-i]
    b.append(p)
    
    i=i-1
    
 out.append(p)
 print(p)
 t=t+0.5

plt.plot(inp,out,'ro')
