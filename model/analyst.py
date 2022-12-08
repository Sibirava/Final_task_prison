from model.prisoner import Prisoner

class Analyst:
    @staticmethod
    def count_term(ls):
        sum_term = 0

        for prisoner in ls:
            if isinstance(prisoner, Prisoner):
                sum_term += prisoner.term
        return sum_term

    @staticmethod
    def find_max_term(prisoners):
        if not isinstance(prisoners, (list, tuple)):
            return

        iterm = 0
        for index in range(1, len(prisoners)):
            current = prisoners[index].term
            max = prisoners[iterm].term

            if current > max:
                iterm = index
        return prisoners[iterm]




