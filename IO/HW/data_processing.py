import json
"""
    1.Какой номер самого дорого заказа за июль?
    2.Какой номер заказа с самым большим количеством товаров?
    3.В какой день в июле было сделано больше всего заказов?
    4.Какой пользователь сделал самое большое количество заказов за июль?
    5.У какого пользователя самая большая суммарная стоимость заказов за июль?
    6.Какая средняя стоимость заказа была в июле?
    7.Какая средняя стоимость товаров в июле?
"""

with open("data.json", 'r') as my_file:
    json_data = json.load(my_file)



def max_data():
    max_price = 0
    max_order = ''
    max_quantity = 0
    max_day = ''
    max_user = 0
    max_price_user = 0
    for order_num, orders_data in json_data.items():
        price = orders_data['price']
        quantity = orders_data['quantity']
        if quantity > max_quantity:
            max_order = order_num
            max_quantity = quantity
            max_day = orders_data['date'].split('-')[1]
            max_user = orders_data['user_id']

        if price > max_price:
            max_order = order_num
            max_price = price
            max_price_user = orders_data['user_id']




    print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}'
          f'Номер заказа с самым большим количеством товаров: {max}')
