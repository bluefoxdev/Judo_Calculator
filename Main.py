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

plans = {
    "Beginner": 25,
    "Intermediate": 45,
    "Advanced": 80,
    "Professional": 120,
}
########


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
        else:
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
            self.Weight_category = ""#
            self.gym_plan = ""
            #loops until a valid age other than zero entered by user
            while(self.Age == 0):
                #ageinput
                Attempt = input('Enter Age(eg "34"):')
                #remove all whitespaces from back and front of input
                Attempt = Attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.Age = int(Attempt)
                    #if age is just a number and is above 0, it is valid, else prompt user to try again
                    if self.Age > 0:
                        break
                    else:
                        print('Age must be a positive number and more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('Age must be given as number of years alone (no "year" or "yr"), please retry.')

            #loops till valid Weight is given by user
            while(self.Weight == 0):
                #input
                Attempt = input('Enter Weight in kgs (eg "34.5"):')
                #remove all whitespaces from back and front of input
                Attempt = Attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.Weight = float(Attempt)
                    #if Weight is just a number and is above 0, it is valid, else prompt user to try again
                    if self.Weight > 0:
                        break
                    else:
                        print('Weight must be a positive number more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('Weight must be given as a number alone (no "kilograms" or "kgs")')

            #loops till valid Sex is given by user
            while(self.Sex == ""):
                #user input and input formatting
                Attempt = input('Enter Sex(eg "M" or "F"):')
                Attempt = Attempt.strip().upper()
                #checks if the input is M or F, if not warn user and allow it to be entered
                if Attempt in ["M", "F"]:
                    self.Sex = Attempt
                else:
                    print("Invalid Sex entered, for the Safety of other athletes either M or F needs to be specified for proper weight classification, please enter M or F")

            while(self.gym_plan == ""):
                Attempt = input('Enter desired plan number\n1:Beginner\n2:Intermediate\n3:Advanced\n4:Professional\n')
                Attempt = Attempt.strip()

                if Attempt[0] in ["1", "2", "3", "4"]:
                    self.gym_plan = Attempt
                else:
                    print("Invalid, please enter a number of the desired plan on the list.")

        #assigns Weight catagory based on weight and sex
        #Males
        if self.Sex == "M" and self.Weight < 73:
            self.Weight_category = "Male Light Weight"
        
        elif self.Sex == "M" and self.Weight < 90:
            self.Weight_category = "Male medium Weight"
        
        elif self.Sex == "M" and self.Weight > 90:
            self.Weight_category = "Male Heavy Weight"
        #Females
        elif self.Sex == "F" and self.Weight < 57:
            self.Weight_category = "Female Light Weight"
        
        elif self.Sex == "F" and self.Weight < 70:
            self.Weight_category = "Female medium Weight"
        
        elif self.Sex == "F" and self.Weight > 70:
            self.Weight_category = "Female Heavy Weight"
        else:
            #this is impossible, but for whatever reason it does happen, it will be caught here
            self.Weight_category = "unassigned"
            print(f"warning: no parameters reached for placing in a weight catagory with sex: {self.Sex} and weight: {self.Weight}, please inform a member of staff.")

        print("Athlete created successfully")

    def introduction(self):
        return f"Hello, my Name is {self.Name}, I am {self.Age} year old {self.get_Sex()} Athlete, and I Weight {self.Weight} kgs,\nthis puts me in the {self.Weight_category} category."
    
    def get_plan(self):
        match self.gym_plan:
            case "1":
                return "Beginner"
            case "2":
                return "Intermediate"
            case "3":
                return "Advance"
            case "4":
                return "Professional"
            case _:
                return f'unrecognised plan number "{self.gym_plan}" for athlete {self.Name}'

    #print all the info of the athlete
    def print_info(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Weight: {self.Weight}")
        print(f"Sex: {self.get_Sex()}")
        print(f"Weight category: {self.Weight_category}")
        print(f"Gym plan: {self.get_plan()}")
        

#returns the list of costs and total costs
def calculate_cost(Athletes):
    #total price of all athletes plans
    Price = 0
    #indivdual prices in order of athletes
    Prices = []
    #loop through athletes and assign cost based on chosen plan
    for instance in Athletes:
        try:
            Plan_price = plans[instance.get_plan()]
        except KeyError:
            #print error message if unrecognised plan
            print(instance.get_plan())
        #increase total
        Price += Plan_price
        #add cost to list
        Prices.append(Plan_price)
    return [Price, Prices]


def main():
    loop = True
    #main program loop
    while(loop == True):
        print("##########JUDO APP##########\n")
        print("Please type a number for service")
        print("1: Register Athlete")
        print("2: View Athletes")
        print("3: Delete Athlete")
        print("4: Save reciept") #out of scope, remove for submission
        print("5: Exit")
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
                        instance.print_info()
                        print(f"-Charge: £{prices[1][Athletes.index(instance)]}")
                    print(f"\nTotal: £{prices[0]}")

                case "3":
                    for instance in Athletes:
                        print(f"\nAthlete {Athletes.index(instance)+1}:")
                        instance.print_info()
                    delete_Attempt = input("Enter the number of the Athlete you want to delete:")
                    delete_Attempt = delete_Attempt.strip()

                    try:
                        delete_Attempt = int(delete_Attempt[0])
                        if delete_Attempt > 0 and delete_Attempt <= len(Athletes):
                            del Athletes[delete_Attempt-1]
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
                
                case "5":
                    print("Have a good day!")
                    loop = False
                case _:
                    print(f"Invalid choice {choice[0]}")
        #warn user if answer is not numeric
        else:
            print('Answer not Numeric (eg: "1")')

#calls the "main" function starting the program flow
main()