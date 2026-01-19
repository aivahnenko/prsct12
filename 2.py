prices = [1500, 500, 2000, 3500, 1000, 4500]
min_price = min(prices)
max_price = max(prices)
sum_price = sum(prices)
sre_parse = sum_price / len(prices)
print(f'минимальная цена {min_price}')
print(f'максимальная цена {max_price}')
print(f'сумма всех цен в списке {sum_price}')
print(f'средняя цена {sre_parse}')