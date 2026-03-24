##imports
import os
##


###Global variable###
#Athlete storage#
Athletes = []

###plan prices###
Beginner = 25
Intermediate = 45
Advanced = 80
Professional = 120
########
###


class Person():
    #initialisation 
    def __init__(self, Name, Age, Weight, Sex):
        self.Name = Name
        self.Age = Age
        self.Weight = Weight
        self.Sex = Sex

    #returns a user friendly version of the Sex for display
    def get_Sex(self):
        if self.Sex == "M":
            return "male"
        elif self.Sex == "F":
            return "female"
    
    #prints an introductory sentance
    def introduction(self):
        return f"Hello, my Name is {self.Name}, I am {self.Age} year old {self.get_Sex()}, and I Weight {self.Weight} kgs."
        
class Athlete(Person):
    #initialisation
    def __init__(self, Name, Age, Weight, Sex, gym_plan, manual_input):
        #determines if the program or the user is filling initalisation info
        if manual_input == False:
            #program fills out
            self.Name = Name
            self.Age = Age
            self.Weight = Weight
            self.Sex = Sex
            self.gym_plan = gym_plan
        else:
            #user fills out
            print("#####Adding new Athlete#####\n")
            self.Name = input("Enter Name:")
            self.Age = 0
            self.Weight = 0
            self.Sex = ""
            self.Weight_category = ""
            #loops until a valid age other than zero entered
            while(self.Age == 0):
                #ageinput
                attempt = input('Enter Age(eg "34"):')
                #remove all whitespaces from back and front of input
                attempt = attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.Age = int(attempt)
                    #if age is just a number and is above 0, it is valid, else prompt user to try again
                    if self.Age > 0:
                        break
                    else:
                        print('Age must be a positive number and more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('Age must be given as number of years alone (no "year" or "yr"), please retry.')

            #loops till valid Weight is given
            while(self.Weight == 0):
                #input
                attempt = input('Enter Weight in kgs (eg "34.5"):')
                #remove all whitespaces from back and front of input
                attempt = attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.Weight = float(attempt)
                    #if Weight is just a number and is above 0, it is valid, else prompt user to try again
                    if self.Weight > 0:
                        break
                    else:
                        print('Weight must be a positive number more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('Weight must be given as a number alone (no "kilograms" or "kgs")')

            #
            while(self.Sex == ""):
                attempt = input('Enter Sex(eg "M" or "F"):')
                attempt = attempt.strip().upper()

                if attempt in ["M", "F"]:
                    self.Sex = attempt
                elif input('Unrecognized Sex, would you like to be marked as "other"? Y/N').strip().upper() == "Y":
                    self.Sex = "O"
                else:
                    pass

        if self.Sex == "M" and self.Weight < 73:
            self.Weight_category = "Male Light Weight"
        elif self.Sex == "M" and self.Weight < 90:
            self.Weight_category = "Male medium Weight"
        elif self.Sex == "M" and self.Weight > 90:
            self.Weight_category = "Male Heavy Weight"
        elif self.Sex == "F" and self.Weight < 57:
            self.Weight_category = "Female Light Weight"
        elif self.Sex == "F" and self.Weight < 70:
            self.Weight_category = "Female medium Weight"
        elif self.Sex == "F" and self.Weight > 70:
            self.Weight_category = "Female Heavy Weight"
        print("Athlete created successfully")

    def introduction(self):
        return f"Hello, my Name is {self.Name}, I am {self.Age} year old {self.get_Sex()} Athlete, and I Weight {self.Weight} kgs,\nthis puts me in the {self.Weight_category} category."
    
    def print_info(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Weight: {self.Weight}")
        print(f"Sex: {self.get_Sex()}")
        print(f"Weight category: {self.Weight_category}")
        

#returns the list of costs and total costs
def calculate_cost(Athletes):
    price = 0
    prices = []
    for instance in Athletes:
        match instance.gym_plan:
            case "1":
                price += Beginner
                prices.append(Beginner)
            case "2":
                price += Intermediate
                prices.append(Intermediate)
            case "3":
                price += Advanced
                prices.append(Advanced)
            case "4":
                price += Professional
                prices.append(Professional)
            case _:
                return f'unsupported value given for gym membership: "{Athlete.gym_plan}" please inform a member of staff.'
    return [price, prices]


def main():
    loop = True

    while(loop == True):
        print("##########JUDO APP##########\n")
        print("please type a number for service")
        print("1: Register Athlete")
        print("2: View Athletes")
        print("3: delete Athlete")
        print("4: save reciept")
        choice = input("Enter service number:")
        choice = choice.strip()

        if choice[0].isnumeric():
            
            match choice[0]:
                case "1":
                    Athletes.append(Athlete(None, None, None, None, None, True))
                case "2":
                    prices = calculate_cost(Athletes)
                    for instance in Athletes:
                        print(f"\nAthlete {Athletes.index(instance)+1}:")
                        Athlete.print_info()
                        print(f"-Charge: {prices[0]}")

                case "3":
                    for instance in Athletes:
                        print(f"\nAthlete {Athletes.index(instance)+1}:")
                        instance.print_info()
                    delete_attempt = input("Enter the number of the Athlete you want to delete:")
                    delete_attempt = delete_attempt.strip()

                    try:
                        delete_attempt = int(delete_attempt[0])
                        if delete_attempt > 0 and delete_attempt <= len(Athletes):
                            del Athletes[delete_attempt-1]
                            print("Athlete deleted successfully")
                        else:
                            print("Invalid choice, number out of range")
                    except TypeError:
                        print('Answer not Numeric (eg: "3")')
                case "4": #out of scope, remove for submission
                    storage_directory = f"{os.path.realpath(os.path.dirName(__file__))}"
                    valid_fileName_found = False
                    receipt_number = 1

                    while(valid_fileName_found == False):
                        if os.path.exists(f"{storage_directory}\Receipt {receipt_number}.txt"):
                            receipt_number += 1
                        else:
                            valid_fileName_found = True
                            file = open(f"{storage_directory}\Receipt {receipt_number}.txt", "w")
                            file.write("#####Receipt#####\n")
                            for participants in Athletes:
                                file.write(f"-Athlete {participants.Name}")
                                file.write(f"\n  Age {participants.Age}")
                                file.write(f"\n  Weight {participants.Weight}")
                                file.write(f"\n  Sex {participants.Sex}")
                                file.write(f"\n  Weight category {participants.Weight_category}")
                            file.write("\n\n###save this for later to reload###")
                            file.close()
                            print(f"Data saved as Receipt{receipt_number} in\n{storage_directory}\n do not edit the contents to ensure proper loading later on.")
                
                case _:
                    print("Invalid choice")
        #warn user if no 
        else:
            print('Answer not Numeric (eg: "1")')

#calls the "main" function starting the program flow
main()