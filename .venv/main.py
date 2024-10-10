import requests
from bs4 import BeautifulSoup

# Функция для получения ссылок с Википедии
def get_wikipedia_links():
    url = 'https://ru.wikipedia.org/wiki/Заглавная_страница'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск ссылок, содержащих слово "Галактика"
    links = []
    for link in soup.find_all('a', href=True):
        if 'Галактика' in link.text:
            links.append({'text': link.text, 'href': link['href']})

    return links

# Функция для создания HTML-файла
def create_html_file(filename, title, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="index.html">Мой сайт</a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="wikipedia.html">Работа с википедией</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="products.html">Карточки товаров</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="about.html">О сайте и контакты</a>
                        </li>
                    </ul>
                </div>
            </nav>
            <div class="container mt-4">
                {content}
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        ''')

# Создание главной страницы
create_html_file('index.html', 'Главная страница', '''
<h1>Добро пожаловать на мой сайт!</h1>
<p>Выберите пункт меню для продолжения.</p>
''')

# Создание страницы "Работа с Википедией"
wikipedia_links = get_wikipedia_links()
links_html = '<ul class="list-group">'
for link in wikipedia_links:
    links_html += f'<li class="list-group-item"><a href="https://ru.wikipedia.org{link["href"]}" target="_blank">{link["text"]}</a></li>'
links_html += '</ul>'

create_html_file('wikipedia.html', 'Работа с Википедией', f'''
<h1>Ссылки с Википедии по запросу "Галактика"</h1>
{links_html}
''')

# Создание страницы "Карточки товаров"
products = [
    {'name': 'Товар 1', 'description': 'Описание товара 1', 'price': '1000 ₽'},
    {'name': 'Товар 2', 'description': 'Описание товара 2', 'price': '2000 ₽'},
    {'name': 'Товар 3', 'description': 'Описание товара 3', 'price': '3000 ₽'},
]

products_html = '<div class="row">'
for product in products:
    products_html += f'''
    <div class="col-md-4">
        <div class="card mb-4">
            <div class="card-body">
                <h5 class="card-title">{product["name"]}</h5>
                <p class="card-text">{product["description"]}</p>
                <p class="card-text"><strong>{product["price"]}</strong></p>
            </div>
        </div>
    </div>
    '''
products_html += '</div>'

create_html_file('products.html', 'Карточки товаров', f'''
<h1>Карточки товаров</h1>
{products_html}
''')

# Создание страницы "О сайте и контакты"
create_html_file('about.html', 'О сайте и контакты', '''
<h1>О сайте</h1>
<p>Этот сайт создан для демонстрации работы с Python, Bootstrap и BeautifulSoup.</p>
<p>Контакты: example@example.com</p>
''')

print("Сайт успешно создан. Откройте файлы .html в браузере.")
