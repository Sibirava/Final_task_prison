from model.prisoner import Prisoner

class SerialKiller(Prisoner):
    def __init__(self, victim, death_penalty=True):
        self._victim = victim
        self._death_penalty = death_penalty

    @property
    def victim(self):
        return self._victim

    @victim.setter
    def victim(self, victim):
        if victim >= 3:
            self._victim = victim

    @property
    def death_penalty(self):
        return self._death_penalty

    @death_penalty.setter
    def death_penalty(self, death_penalty):
        self._death_penalty = death_penalty
