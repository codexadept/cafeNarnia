startMessage = 'Приветствуем в нашем боте! Вы можете открыть меню, сделать заказ, ' \
               'посмотреть расположение! Выберите нужную опцию:'

my_order = 'Выберите дату заказа:'

year = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля', '08': 'Августа',
        '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'}

def order(data):
    orderId, menu, date, recipient, custId = data[0], data[1], data[2], data[3], data[4]
    order_date = date.split()
    day, month = order_date[0].split('-')[2], order_date[0].split('-')[1]
    date_time = f'{day} {year[month]} в {":".join(order_date[1].split(":")[0:2])}'
    return f'Номер заказа #{orderId}\n\n' \
           f'Состав: \n' \
           f'   {menu}' \
           f'\n\nДата и время заказа: {date_time}'