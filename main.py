class Book():
    def __init__(self, name, year, publisher, author):
        self.__name = ''
        self.__year = 0
        self.__publisher = ''
        self.__author = ''

        self.set_name(name)
        self.set_year(year)
        self.set_publisher(publisher)
        self.set_author(author)

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name.capitalize()

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if str(year).isdigit() and 1650 < int(year) < 2022:
            self.__year = year
        else:
            print('Не верно указан год!')

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher: str):
        self.__publisher = publisher.capitalize()

    def get_author(self):
        return self.__author

    def set_author(self, author: str):
        self.__author = author.capitalize()

    def __str__(self):
        return (f'Название: {self.__name}\n'
                f'Год выпуска: {self.__year}\n'
                f'Издательство: {self.__publisher}\n'
                f'Автор: {self.__author}\n')


obj_book = Book('Изучаем Java', 2021, 'ЭКСМО', 'Кэти Сьерра и Берт Бейтс')
print('Книга:')
print(obj_book)
print()

class Magazine(Book):
    def __init__(self, name, year, publisher, author, themes, periodicity, price):
        super().__init__(name, year, publisher, author)
        self.__periodicity = ''
        self.__themes = ''
        self.__price = 0

        self.set_themes(themes)
        self.set_periodicity(periodicity)
        self.set_price(price)

    def get_periodicity(self):
        return self.__periodicity

    def set_periodicity(self, periodicity: str):
        self.__periodicity = periodicity

    def get_themes(self):
        return self.__themes

    def set_themes(self, themes: str):
        themes_list = [line.replace('\n', '').lower() for line in open('themes.txt', 'r', encoding="utf8")]
        if themes.lower() in themes_list:
            self.__themes = themes
        else:
            print('Не вверно введена тематика! Тематика не изменена!')

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if str(price).isdigit() and int(price) > 0:
            self.__price = price
        else:
            print('Не верно указана цена! Цена не изменена!')

    def __str__(self):
        return (f'{super().__str__()}'
                f'Тематика: {self.__themes}\n'
                f'Периодичность: {self.__periodicity}\n'
                f'Цена: {self.__price} грн.')


obj_magazine = Magazine('Vogue', 1892, 'Conde Nast Publication', 'Anna Viktur', 'журнал мод', 'ежемесячный', 100)
print('Журнал:')
print(obj_magazine)
print()

class Newspaper(Book):
    # по принципу территориального распространения и охвату аудитории:
    # общенациональные, региональные (республиканские, областные, краевые), местные (городские, районные), внутрикорпоративные (обращённые к сотрудникам определённой организации), многотиражные, профессиональные;
    # по тематике — деловые, общеполитические, отраслевые, рекламно-информационные, развлекательные, смешанные;
    # по периодичности — ежедневные (утренние или вечерние), еженедельные, ежемесячные;
    # по качеству — солидные, популярные, квалоиды и «жёлтые»;
    def __init__(self, name, year, publisher, author, territorial_distribution, themes, periodicity, quality, price):
        super().__init__(name, year, publisher, author)
        self.__territorial_distribution = ''
        self.__periodicity = ''
        self.__themes = ''
        self.__quality = ''
        self.__price = 0

        self.set_territorial_distribution(territorial_distribution)
        self.set_themes(themes)
        self.set_periodicity(periodicity)
        self.set_quality(quality)
        self.set_price(price)

    def get_territorial_distribution(self):
        return self.__territorial_distribution

    def set_territorial_distribution(self, territorial_distribution: str):
        territorial_distribution_list = ['общенациональная', 'региональная',
                                         'местная', 'внутрикорпоративная',
                                         'многотиражная', 'профессиональная']
        if territorial_distribution.lower() in territorial_distribution_list:
            self.__territorial_distribution = territorial_distribution
        else:
            print('Не вверно введен принцип территориального распространения! Данные не изменены!')

    def get_periodicity(self):
        return self.__periodicity

    def set_periodicity(self, periodicity: str):
        periodicity_list = ['ежедневные', 'утренние', 'вечерние', 'еженедельные', 'ежемесячные']
        if periodicity.lower() in periodicity_list:
            self.__periodicity = periodicity
        else:
            print('Не вверно введена периодичнсть! Данные не изменены!')

    def get_themes(self):
        return self.__themes

    def set_themes(self, themes: str):
        themes_list = ['деловые', 'общеполитические',
                       'отраслевые', 'рекламно-информационные',
                       'развлекательные', 'смешанные']
        if themes.lower() in themes_list:
            self.__themes = themes
        else:
            print('Не вверно введена тематика! Тематика не изменена!')

    def get_quality(self):
        return self.__quality

    def set_quality(self, quality: str):
        quality_list = ['солидные', 'популярные', 'квалоиды', 'жёлтые']
        if quality.lower() in quality_list:
            self.__quality = quality
        else:
            print('Не вверно указано качество! Данные не изменены!')

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if str(price).isdigit() and int(price) > 0:
            self.__price = price
        else:
            print('Не верно указана цена! Цена не изменена!')

    def __str__(self):
        return (f'{super().__str__()}'
                f'Принцип распрастранения: {self.__territorial_distribution}\n'
                f'Тематика: {self.__themes}\n'
                f'Периодичность: {self.__periodicity}\n'
                f'Качество: {self.__quality}\n'
                f'Цена: {self.__price} $')


obj_newspaper = Newspaper('The New York Times', 1851, 'A.G. Sulzberger', 'Din Bake', 'общенациональная', 'смешанные', 'ежедневные', 'солидные', 1)
print('Газета:')
print(obj_newspaper)
