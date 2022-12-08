from model.prisoner import Prisoner

class Thief(Prisoner):
    def __init__(self, article=3):
        self._article = article
