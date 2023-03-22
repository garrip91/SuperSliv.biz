class Person():

    def eat(self):
        print("Ням-ням!")


class Employee(Person):

    def visit_demo(self):
        print("Все сотрудники ходят на демо. Я тоже схожу!")


class Developer(Employee):

    def review_code(self):
        print("Делаю код-ревью коллеге. Всё неплохо, пара замечаний и мержим!")


class FrontendDeveloper(Developer):

    def code_frontend(self):
        print("Делаю запрос на сервер, кидаю данные в стор, раскладываю по компонентам и пушим!")


class BackendDeveloper(Developer):

    def code_backend(self):
        print("Ловим параметры запроса, проверяем права, дёргаем БД, сериализуем, пишем тест, тестим и пушим!")
