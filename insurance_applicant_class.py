#class for insurance applicant
class Insurance_applicant():
    def __init__(self):
        self.first_name = input("Zadejte jméno pojištěného:\n")
        self.second_name = input("Zadejte příjmení:\n")
        self.phone_number = input("Zadejte telefonní číslo:\n")
        self.age = int(input("Zadejte věk:\n"))

    def create_new_applicant(self):
        new_user = {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "phone_number": self.phone_number.strip().replace(" ", ""),
            "age": self.age
        }
        return new_user