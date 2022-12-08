from model.prisoner import Prisoner

class Killer(Prisoner):
    def __init__(self, name, age, term, victim, article=2):
        self._name = name
        self._age = age
        self._article = article
        self._term = term
        self._victim = victim


    @property
    def victim(self):
        return self._victim

    @victim.setter
    def victim(self, victim):
        self._victim = victim



