n = int(input('введите число n '))
list=[]
for i in range(1, n+1):
    if i % 2 == 1:
       list.append(i)
print(f'список нечетных чисел до {n}:' , *list)