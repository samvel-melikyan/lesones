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



def sales_stats(list, revenue=False, quantity=False, *args):
    products = []
    products_quantity = 0
    products_revenue = 0
    for i,k in zip(list, products):
        k = {"name": i[0],
             "quantity": i[1],
             "price": i[2]
             }
        products_quantity += k["quantity"]
        products_revenue += k["revenue"]
    print(products_revenue)
    if revenue == True:
        return products_revenue
    elif quantity == True:
        data = {products[i] for i in products}
        return (args, {products})

    else:
        print(f"""Products : {[products["name"] for key in products.keys() if key in products]}
Quantity : {products_quantity}
Revenue : {products_revenue}""")



sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})













