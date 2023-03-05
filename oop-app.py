#logika
class Application():

    def __init__(self):
        self.all_users = []

    def premenu(self,heading):
        print("--------------------")
        print(heading)
        print("--------------------")

    def menu(self):
        print("Vyberte si akci")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    def end_of_application(self,end_text):
        print(end_text)

    def find_user(self):

        searched_first_name = input("Zadejte jméno pojištěného: ")
        searched_second_name = input("Zadejte příjmení pojištěného: ")
        found_users = []
        #hledání pojištěnců podle jména a příjmení
        for one_user in self.all_users:
            if searched_first_name == one_user['first_name'] and searched_second_name == one_user['second_name']:
                found_users.append(one_user)
        #vypisování nalezených pojištěnců
        if len(found_users) != 0:
            for one_user in found_users:
                print(f"{one_user['first_name']}\t\t {one_user['second_name']} \t\t {one_user['phone_number']} \t\t {one_user['age']}")    
        else:
            print("Nebyl nalezen žádný pojištěnec.")
        print("\n")     

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
            "phone_number": self.phone_number,
            "age": self.age
        }
        return new_user
    
#použití
insurance_application = Application()
insurance_application.premenu("Evidence pojištěných")


while True:
    insurance_application.menu()
    user_choice = int(input("Zadejte svou volbu: "))
    if user_choice == 1:
        applicant = Insurance_applicant()
        created_applicant = applicant.create_new_applicant()
        insurance_application.all_users.append(created_applicant)
        #print(insurance_application.all_users)
    elif user_choice == 2:
        for one_user in insurance_application.all_users:
            print(f"{one_user['first_name']}\t\t {one_user['second_name']} \t\t {one_user['phone_number']} \t\t {one_user['age']}")
    elif user_choice == 3:
        insurance_application.find_user()
    elif user_choice == 4:
        insurance_application.end_of_application("Děkujeme za používání aplikace.")
        break
