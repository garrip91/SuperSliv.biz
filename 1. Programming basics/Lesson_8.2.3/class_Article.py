class Article:

    def __init__(self, content):
        self.content = content


class ArticleExtended(Article):

    def count_symbols(self):
        return len(self.content)

    def count_words(self):
        return len(self.content.split())


article = ArticleExtended(
    """
    Ваш баланс составляет $ -567.072.565,13.
    Номер заблокирован.
    Вас ожидает 26 лет рабства на урановых рудниках.
    Одна СМСка. Чёртов роуминг на Сириусе. (c) Юрий Ермаков - Баланс
    """
)


print(article.count_symbols())
print(article.count_words())
