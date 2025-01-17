class Person:
    def nameprint(self, name, age):

        print(name)


fstnm = Person()
fstnm.nameprint('golan', 20)


class Pizza:
    def __init__(self, name):
        self.name = name

    def menu(self):
        men = {'mushroom': 39, 'union': 40, 'cheeze': 35}
        print(f'Pizza Menu: {men}')

    def make(self):
        pizza = Pizza(self.name)
        prices = {'mushroom': 39, 'union': 40, 'cheeze': 35}
        PN = self.name

        if pizza.name in prices:
            print(f'making a {PN} Pizza for {prices[PN]}')
        elif pizza.name == '':
            print('please choose Pizza')
        else:
            print("Pizza dos'ent exist")

    def eat(self):

        print('you ate 1 piece of pizza')


menu = Pizza('menu')
menu.menu()

mk = Pizza('')
mk.make()

eat = Pizza('eat')
eat.eat()


