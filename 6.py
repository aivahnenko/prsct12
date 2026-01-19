word = str(input('введите имя '))
name_list = list(word)
rev_list = name_list[::-1]
if name_list == rev_list:
    print("ваше имя это палиндром")
else:
    print("ваше имя не палиндром")