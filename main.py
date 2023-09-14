print('Введите натуральные a и b такие, что a<b')
d=1
while d==1:
    a=input()
    b=input()
    try:
        while (int(a)>=int(b)) or (int(a)<=0) or (int(b)<=0):
            print('Введите натуральные a и b такие, что a<b')
            a=input()
            b=input()
        d=0
    except:
        print('Введите натуральные a и b такие, что a<b')
a=int(a)
b=int(b)
count=0
for i in range (a, b+1):
    f=[]
    for j in range (1, int(i**0.5)+1):
        if i%j==0:
            f.append(j)
            if j**2!=i:
                f.append(i//j)
    if len(f)==4:
        count=1
        print(i)
        t=sorted(f, reverse=True)
        print(*t)
if count==0:
    print('Не найдено')
