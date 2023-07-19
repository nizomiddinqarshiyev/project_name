class Movie:
    def __init__(self, title, year, country, language, time):
        self.title = title
        self.year = year
        self.country = country
        self.language = language
        self.time = time

    def get_info(self):
        dic = {
            'title': self.title,
            'year': self.year,
            'country': self.country,
            'language': self.language,
            'time': self.time
        }
        return dic

    def set_title(self):
        self.title = input('Enter the title: ')

    def set_year(self):
        self.year = input('Enter the year: ')

    def set_country(self):
        self.country = input('Enter the country: ')

    def set_language(self):
        self.language = input('Enter the language: ')

    def set_time(self):
        self.time = input('Enter the time: ')


