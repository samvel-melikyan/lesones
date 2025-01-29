from tkinter.font import names

import Lambdas
from functions import new_line, short_line, new_section
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

def combin_data(list):
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
    return producs

def sales_stats(list, **kwargs):
    total_revenue = None
    product_quantities = None
    producs = combin_data(list)

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

new_line("N-3")

def create_report(list, funk, **kwargs):
    result = f"Средний доход за данный период составил {funk(list, revenue=True)[0] / len(list)}.\nКоличество проданных единиц каждого товара:"
    for i,j in zip(funk(list, quantity=True)[1].keys(),funk(list, quantity=True)[1].values()):
        result += f"\n{i}: {j}"
    return result

new_line()
sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
# print(combin_data(sales_data))
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})
short_line()
print(create_report(sales_data, sales_stats))
# # ------------------------------------
# def sales_stats(data, **kwargs):
#    revenue = sum([item[1]*item[2] for item in data]) if kwargs.get('revenue') else None
#    if kwargs.get('quantity'):
#        quantity = {}
#        for item in data:
#            if item[0] in quantity:
#                quantity[item[0]] += item[1]
#            else:
#                quantity[item[0]] = item[1]
#    else:
#        quantity = None
#    return revenue, quantity
# def create_report(data, func):
#    revenue, quantity = func(data, revenue=True, quantity=True)
#    report = f"Средний доход за данный период составил {revenue/len(data)}.\n"
#    report += "Количество проданных единиц каждого товара:\n"
#    for item, qty in quantity.items():
#        report += f"{item}: {qty}\n"
#    return report
new_line("N-4")

def sort_users_by_activity(users):
    return sorted(users,  key=lambda user: users[user], reverse=True)

user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
print(sort_users_by_activity(user_activity))
# ['user3', 'user4', 'user1', 'user5', 'user2']






