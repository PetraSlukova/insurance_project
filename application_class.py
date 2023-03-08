#main class for insurance application
class Application():

    def __init__(self):
        self.all_users = []

    def premenu(self,heading):
        print("--------------------")
        print(heading)
        print("--------------------")

    def options(self):
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
        #insured searching according to first name and surname 
        for one_user in self.all_users:
            if searched_first_name == one_user['first_name'] and searched_second_name == one_user['second_name']:
                found_users.append(one_user)
        #insured listing
        if len(found_users) != 0:
            for one_user in found_users:
                print(f"{one_user['first_name']}\t\t {one_user['second_name']} \t\t {one_user['phone_number']} \t\t {one_user['age']}")    
        else:
            print("Nebyl nalezen žádný pojištěnec.")
        print("\n")     