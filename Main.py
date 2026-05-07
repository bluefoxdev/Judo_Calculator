


###Global variable###
#Athlete storage#
athletes = []
###

###Service prices###

###pricing for services###
competition_price = 15

private_coaching_price = 20
#prices are per hour in pound sterling

###plan prices###

plans = {
    "Beginner": 25,
    "Intermediate": 45,
    "Advance": 80,
    "Professional": 120,
}
#all prices are treated as pound sterling
########


class Person():
    #initialisation 
    def __init__(self, name, age, weight, sex):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex

    #returns a user friendly version of the sex for display
    def get_sex(self):
        if self.sex == "M":
            return "male"
        else:
            return "female"
    
    #prints an introductory sentance
    def introduction(self):
        return f"Hello, my name is {self.name}, I am {self.age} year old {self.get_sex()}, and I weight {self.weight} kgs."
        
class Athlete(Person):
    #initialisation
    def __init__(self, name, age, weight, sex, gym_plan, competitions, coaching_hours, manual_input):
        #determines if the program or the user is filling initalisation info
        if manual_input == False:
            #program fills out
            self.name = name
            self.age = age
            self.weight = weight
            self.sex = sex
            self.gym_plan = gym_plan
            self.competitions = competitions
            self.coaching_hours = coaching_hours
            #this part is unnecassary due to the removal of reciepts 
            #however it will be useful for an immutible editing system 
        else:
            #user fills out
            print("#####Adding new Athlete#####\n")
            self.name = input("Enter name:")
            self.age = 0
            self.weight = 0
            self.sex = ""
            self.weight_category = ""
            self.gym_plan = ""
            self.competitions = ""
            self.coaching_hours = ""
            #loops until a valid age other than zero entered by user
            while(self.age == 0):
                #ageinput
                Attempt = input('Enter age(eg "34"):')
                #remove all whitespaces from back and front of input
                Attempt = Attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.age = int(Attempt)
                    #if age is just a number and is above 0, it is valid, else prompt user to try again
                    if self.age > 0:
                        break
                    else:
                        print('age must be a positive number and more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('age must be given as number of years alone (no "year" or "yr" and no decimals), please retry.')

            #loops till valid weight is given by user
            while(self.weight == 0):
                #input
                Attempt = input('Enter weight in kgs (eg "34.5"):')
                #remove all whitespaces from back and front of input
                Attempt = Attempt.strip()

                #validates to see if input can be converted to an integer
                try:
                    self.weight = float(Attempt)
                    #if weight is just a number and is above 0, it is valid, else prompt user to try again
                    if self.weight > 0:
                        break
                    else:
                        print('weight must be a positive number more than 0, please retry.')
                #input contains more than just numbers prompt user to retry
                except ValueError:
                    print('weight must be given as a number alone (no "kilograms" or "kgs")')

            #loops till valid sex is given by user
            while(self.sex == ""):
                #user input and input formatting
                Attempt = input('Enter sex(eg "M" or "F"):')
                Attempt = Attempt.strip().upper()
                #checks if the input is M or F, if not warn user and allow it to be reentered
                if Attempt in ["M", "F"]:
                    self.sex = Attempt
                else:
                    print("Invalid sex entered, for the Safety of other athletes either M or F needs to be specified for proper weight classification, please enter M or F")

            #loops till valid gym plan is given by user
            while(self.gym_plan == ""):
                #user input and input formatting
                Attempt = input('Enter desired plan number\n1:Beginner\n2:Intermediate\n3:Advance\n4:Professional\n')
                Attempt = Attempt.strip()
                #checks if the input is a valid number, if not warn user and allow it to be reentered
                if Attempt in ["1", "2", "3", "4"]:
                    self.gym_plan = Attempt
                else:
                    print("Invalid, please enter a number of the desired plan on the list.")
            #loops till valid amount of competitions are given by user
            while(self.competitions == ""):
                Attempt = input('Enter desired amount of competitions from 0 to 2:')
                Attempt = Attempt.strip()
                #checks if the input is a valid number, if not warn user and allow it to be reentered
                if Attempt in ["0", "1", "2"]:
                    self.competitions = Attempt
                else:
                    print("Invalid number of competitions.")

            #loops till valid amount of private tutoring hours is given by user
            while(self.coaching_hours == ""):
                Attempt = input('Enter desired amount of private coaching hours from 0 to 3\n')
                Attempt = Attempt.strip()
                #checks if the input is a valid number, if not warn user and allow it to be reentered
                if Attempt in ["0", "1", "2", "3"]:
                    self.coaching_hours = Attempt
                else:
                    print("Invalid number of hours selected .")

        #assigns weight catagory based on weight and sex
        #Males
        if self.sex == "M" and self.weight < 73:
            self.weight_category = "Male light weight"
        
        elif self.sex == "M" and self.weight < 90:
            self.weight_category = "Male medium weight"
        
        elif self.sex == "M" and self.weight > 90:
            self.weight_category = "Male heavy weight"
        #Females
        elif self.sex == "F" and self.weight < 57:
            self.weight_category = "Female light weight"
        
        elif self.sex == "F" and self.weight < 70:
            self.weight_category = "Female medium weight"
        
        elif self.sex == "F" and self.weight > 70:
            self.weight_category = "Female heavy weight"
        else:
            #this is impossible, but for whatever reason it does happen, it will be caught here
            self.weight_category = "unassigned"
            print(f"warning: no parameters reached for placing in a weight catagory with sex: {self.sex} and weight: {self.weight}, please inform a member of staff.")

        print("Athlete created successfully")

    def introduction(self):
        #little introduction function not needed or used
        return f"Hello, my name is {self.name}, I am {self.age} year old {self.get_sex()} Athlete, and I weight {self.weight} kgs,\nthis puts me in the {self.weight_category} category."
    
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
                return f'unrecognised plan number "{self.gym_plan}" for athlete {self.name}'

    #print all the info of the athlete
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Sex: {self.get_sex()}")
        print(f"Weight category: {self.weight_category}")
        print(f"Gym plan: {self.get_plan()}")
        print(f"Competitions entered: {self.competitions}")
        print(f"Private coaching hours: {self.coaching_hours}")
        

#returns the list of costs and total costs
def calculate_cost(athletes):
    #total price of all athletes plans
    price = 0
    #indivdual prices in order of athletes
    prices = []
    #loop through athletes and assign cost based on chosen plan
    for instance in athletes:
        plan_price = 0
        
        #error catching tests to see if the gym plan number is recognised
        if instance.gym_plan in ["1", "2", "3", "4"]:
            plan_price = plans[instance.get_plan()]
        else:
            #There's no reason way a user can make an inccorect input but if they do somehow, its caught here
            print(instance.get_plan())

        plan_and_services = plan_price+(competition_price*int(instance.competitions))+(private_coaching_price*int(instance.coaching_hours))
        #increase total cost
        price += plan_and_services
        #add cost to list
        prices.append(plan_and_services)

    return [price, prices]


def main():
    loop = True
    #main program loop
    while(loop == True):
        #display main menu and options
        print("##########JUDO APP##########\n")
        print("Please type a number for service")
        print("1: Register Athlete")
        print("2: View athletes")
        print("3: Delete Athlete")
        print("4: Exit")
        
        #user input and formatting
        choice = input("Enter service number:")
        choice = choice.strip()

        #checks if choice is a number
        if choice[0].isnumeric():
            
            #match case with options 
            match choice[0]:
                #create a new athlete
                case "1":
                    #takes user to create an athlete then assigns to athletes array when finished
                    athletes.append(Athlete(None, None, None, None, None, None, None, True))
                #list all athletes
                case "2":
                    #gets the cost for all athletes individually and all together 
                    prices = calculate_cost(athletes)
                    for instance in athletes:
                        print(f"\nAthlete {athletes.index(instance)+1}:")
                        instance.print_info()
                        print(f"-Charge: £{prices[1][athletes.index(instance)]}/Month")
                    print(f"\nTotal: £{prices[0]}/Month")
                    input("Press Enter to go back to menu...")
                
                #delete athlete
                case "3":
                    #lists all athletes for user to see
                    for instance in athletes:
                        print(f"\nAthlete {athletes.index(instance)+1}:")
                        instance.print_info()
                    #prompts user for choice and removes whitespace from sides
                    delete_Attempt = input("Enter the number of the Athlete you want to delete:")
                    delete_Attempt = delete_Attempt.strip()

                    #try and convert user input to int for reading
                    try:
                        #int conversion
                        delete_Attempt = int(delete_Attempt[0])
                        #check if input is above zero and less or equal to number of athletes
                        if delete_Attempt > 0 and delete_Attempt <= len(athletes):
                           #deletes athletes
                            del athletes[delete_Attempt-1]
                            print("Athlete deleted successfully")
                        #warn if number is invalid
                        else:
                            print("Invalid choice, number out of range (must be in range of number of athletes)")
                    #if it cannot be turned into an int warn user
                    except TypeError:
                        print('Answer not Numeric (eg: "3")')
                #quit the program
                case "4":
                    print("Have a good day!")
                    loop = False
                #warn user choice is invalid
                case _:
                    print(f"Invalid choice {choice[0]}")
        #warn user if answer is not numeric
        else:
            print('Answer not Numeric (eg: "1")')

#calls the "main" function starting the program flow
main()