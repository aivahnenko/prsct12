marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
five = 0
two = 0
for i in marks:
    if i == 5:
        five += 1
    if i == 2:
        two =+ 1
print (f'количество пятерок {five}')
print(f'количество двоек {two}')