x = 1
y = 1
fibo = [x,y]
while x<55:
    x,y = y,x+y 
    fibo.append(x) 

print(fibo)