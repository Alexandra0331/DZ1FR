#Задание №7
#Написать функцию, которая будет выводить на экран HTML
#страницу с блоками новостей.
#Каждый блок должен содержать заголовок новости,
#краткое описание и дату публикации.
#Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/blok1/')
def blok1():
    context = [
        {'title': '<<Морозы в Сибири>>',
        'content': 'В ближайшие дни сибирякам предстоит подготовится к резкому похолоданию',
        'data': '10.12.2023'},

    ]
    return render_template('blok1.html', context=context)

@app.route('/blok2/')
def blok2():
    contex = [

        {'title': '<<Новый год 2024>>',
        'content': 'Символ предстоящего 2024 года по восточному календарю — Зеленый Деревянный Дракон. ',
         'data': '12.12.2023'},
    ]
    return render_template('blok2.html', context=contex)

@app.route('/blok3/')
def blok3():
    cont = [
        {'title': '<<Открытие городской елки>>',
         'content': 'Открытие главной городской елки Красноярска перенесено на неделю.',
         'data': '13.12.2023'},
    ]
    return render_template('blok3.html', context=cont)

if __name__ == '__main__':
    app.run(debug=True)