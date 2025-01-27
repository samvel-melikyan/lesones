from tkinter.font import names

import Lambdas
from functions import new_line
from strings import index

new_line("N-1")
def customer_support_simulator(questions):
    result = []
    for i in questions:
        if "Ошибка".casefold() in i:
            result.append("Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.")
        elif "Заказ".casefold() in i:
            result.append("Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.")
        elif "Вернуть".casefold() in i:
            result.append("Вы можете вернуть товар в течение 14 дней с момента получения.")
        else:
            result.append("Благодарим вас за обращение. Ваш вопрос передан специалистам.")
    return result

questions = ['Когда будет отправлен мой заказ?', 'Я хочу вернуть товар', 'В моем заказе произошла ошибка', 'Ваш сервис просто отличный!']
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')

new_line("N-2")


def sales_stats(list, **kwargs):
    total_revenue = None
    product_quantities = None
    producs = {}

    for item in list:
        product_name, quantity, price = item
        if product_name in producs.keys():
            producs[product_name]["quantity"] += quantity
            producs[product_name]["price"] += price
            producs[product_name]["total_price"] += quantity * price
        else:
            producs[product_name] = {"quantity": quantity,
                                     "price": price,
                                     "total_price": quantity * price}
    # print(producs)

    if kwargs.get("revenue") and kwargs.get("quantity"):
        total_revenue = sum(item[1] * item[2] for item in list)
        product_quantities = {}
        for i in producs:
            product_quantities[i] = producs[i]["quantity"]
    elif kwargs.get("quantity"):
        product_quantities = {}
        for i in producs:
            product_quantities[i] = producs[i]["quantity"]
    elif kwargs.get("revenue"):
        total_revenue = sum(x["total_price"] for x in producs.values())

    return total_revenue, product_quantities



sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})













