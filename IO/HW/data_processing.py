import json
from collections import Counter

"""
    1.Какой номер самого дорого заказа за июль?
    2.Какой номер заказа с самым большим количеством товаров?
    3.В какой день в июле было сделано больше всего заказов?
    4.Какой пользователь сделал самое большое количество заказов за июль?
    5.У какого пользователя самая большая суммарная стоимость заказов за июль?
    6.Какая средняя стоимость заказа была в июле?
    7.Какая средняя стоимость товаров в июле?
"""
# opening and reading data from json file, assigning it to a var - json_data
with open("data.json", 'r') as my_file:
    json_data = json.load(my_file)
# defining variables for counting
max_price = 0
max_order_id = ""
max_quantity = 0
max_quantity_order_id = ""
orders_per_day = Counter()
orders_per_user = Counter()
total_spent_per_user = Counter()
total_price = 0
total_orders = 0
total_items = 0
# running a loop throw json_data, dictionary items
for order_id, order_data in json_data.items():
    # declearing and storing the values into a separate variables
    price = order_data["price"]
    quantity = order_data["quantity"]
    date = order_data["date"]
    user_id = order_data["user_id"]
    # finding maximum price
    if price > max_price:
        max_price = price
        max_order_id = order_id
    # finding maximum quantity
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order_id = order_id
    # increasing a value of a counters by meeting a spacific value
    orders_per_day[date] += 1
    orders_per_user[user_id] += 1
    total_spent_per_user[user_id] += price
    total_price += price
    total_orders += 1
    total_items += quantity
# counting total values
busiest_day = max(orders_per_day, key=orders_per_day.get)
most_orders_user = max(orders_per_user, key=orders_per_user.get)
highest_spending_user = max(total_spent_per_user, key=total_spent_per_user.get)
average_order_price = total_price / total_orders if total_orders else 0
average_item_price = total_price / total_items if total_items else 0


# defining a fnction to show results
def print_the_results():
    print(f"Самый дорогой заказ: {max_order_id}, стоимость: {max_price}")
    print(f"Заказ с наибольшим количеством товаров: {max_quantity_order_id}, количество: {max_quantity}")
    print(f"День с наибольшим числом заказов: {busiest_day}")
    print(f"Пользователь с наибольшим числом заказов: {most_orders_user}")
    print(f"Пользователь с самой большой суммарной стоимостью заказов: {highest_spending_user}")
    print(f"Средняя стоимость заказа: {average_order_price:.2f}")
    print(f"Средняя стоимость товаров: {average_item_price:.2f}")
