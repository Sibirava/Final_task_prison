from model.prisoner import Prisoner
from util.killercreator import KillerCreator
from util.converter import Converter
from model.analyst import Analyst

def main():
   ls = KillerCreator.create(10)
   print(Converter.convert_to_string(ls))

   sum_term = Analyst.count_term(ls)
   print(f"Total terms is: {sum_term}")

   max_term = Analyst.find_max_term(ls)
   print(f"Max terms has: {max_term}")

if __name__ == "__main__":
    main()