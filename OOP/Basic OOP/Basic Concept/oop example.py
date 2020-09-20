class movie:
    """ This class is developed for movie"""

    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('The movie name is::', self.title)
        print('The hero name is::', self.hero)
        print('The heroine name is::', self.heroine)


movoieslist = []

while True:
    title = input('Please enter the movie name: ')
    hero = input('Please enter the hero name')
    heroine = input('Please enter the heroine name')
    m = movie(title, hero, heroine)
    movoieslist.append(m)
    print('Movies information added successfully')
    option = input('Do you want to add more movies:, Enter Yes or No')
    if option.lower() == 'no':
        break
print('All movies information')
for movie in movoieslist:
    movie.info()
    print()
