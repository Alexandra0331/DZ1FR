#Задание №9
#Создать базовый шаблон для интернет-магазина,
#содержащий общие элементы дизайна (шапка, меню,
#подвал), и дочерние шаблоны для страниц категорий
#товаров и отдельных товаров.
#Например, создать страницы "Одежда", "Обувь" и "Куртка",
#используя базовый шаблон.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_9():
    return render_template('index_9.html')

@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')
##правильно ли, что куртка должна наследоваться от одежды? или нужно было оставить от магазина?

if __name__ == '__main__':
    app.run(debug=True)