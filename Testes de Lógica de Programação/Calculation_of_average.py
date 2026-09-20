class Average:
    '''Calcula a média de uma lista de notas'''
    def __init__(self, grades: list):
        self.grades = grades


    def calculate_average(self) -> int | float:
        self.result = sum(self.grades) / len(self.grades)
        return self.result

    @staticmethod
    def check_status(result) -> str:
        if result >= 90:
            return "well Done!✨"
        elif result >= 70:
            return "OK!"
        else:
            return "This is Bad"

my_grades = Average([78, 67, 78, 90])
média = my_grades.calculate_average()
print(média)
print(my_grades.check_status(média))
