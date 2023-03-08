import os
from application_class import Application
from insurance_applicant_class import Insurance_applicant
    
#main code 
insurance_application = Application()
insurance_application.premenu("Evidence pojištěných")

#main cycle for options
while True:
    insurance_application.options()
    user_choice = int(input("Zadejte svou volbu: "))
    if user_choice == 1:
        applicant = Insurance_applicant()
        created_applicant = applicant.create_new_applicant()
        insurance_application.all_users.append(created_applicant)
        os.system("cls")
    elif user_choice == 2:
        for one_user in insurance_application.all_users:
            print(f"{one_user['first_name']}\t\t {one_user['second_name']} \t\t {one_user['phone_number']} \t\t {one_user['age']}")
    elif user_choice == 3:
        insurance_application.find_user()
    elif user_choice == 4:
        insurance_application.end_of_application("Děkujeme za používání aplikace.")
        break
