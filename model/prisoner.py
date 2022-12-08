class Prisoner:
    def __init__(self, name, age, article, term):
        self._name = name
        self._age = age
        self._article = article
        self._term = term

    def __str__(self):
        return (f"{self._name} age {self._age}: "
                f"article = {self._article}, "
                f"term = {self._term}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age

    @property
    def article(self):
        return self._article

    @article.setter
    def article(self, article):
        if 1 < article < 5:
            self._article = article

    @property
    def term(self):
        return self._term

    @article.setter
    def article(self, term):
        self._term = term