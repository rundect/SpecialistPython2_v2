# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход:дано N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
goods_price = [2, 1, 10, 50, 10]
goods_price.sort()

most_price_goods = (len(goods_price)+1) // 2
sum_price = 0
a = goods_price[- most_price_goods:]
for price in goods_price[- most_price_goods:]:
    sum_price += price

print(sum_price)
