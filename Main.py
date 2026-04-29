


###Global variable###
#Athlete storage#
Athletes = []
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
    def __init__(self, Name, Age, Weight, Sex, gym_plan, competitions, coaching_hours, manual_input):
        #determines if the program or the user is filling initalisation info
        if manual_input == False:
            #program fills out
            self.Name = Name
            self.Age = Age
            self.Weight = Weight
            self.Sex = Sex
            self.gym_plan = gym_plan
            self.competitions = competitions
            self.coaching_hours = coaching_hours
            #this part is unnecassary due to the removal of reciepts 
            #however it will be useful for an immutible editing system 
        else:
            #user fills out
            print("#####Adding new Athlete#####\n")
            self.Name = input("Enter Name:")
            self.Age = 0
            self.Weight = 0
            self.Sex = ""
            self.Weight_category = ""
            self.gym_plan = ""
            self.competitions = ""
            self.coaching_hours = ""
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
                    print('Age must be given as number of years alone (no "year" or "yr" and no decimals), please retry.')

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
                #checks if the input is M or F, if not warn user and allow it to be reentered
                if Attempt in ["M", "F"]:
                    self.Sex = Attempt
                else:
                    print("Invalid Sex entered, for the Safety of other athletes either M or F needs to be specified for proper weight classification, please enter M or F")

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
        #little introduction function not needed or used
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
        print(f"Competitions entered: {self.competitions}")
        print(f"Private coaching hours: {self.coaching_hours}")
        

#returns the list of costs and total costs
def calculate_cost(Athletes):
    #total price of all athletes plans
    Price = 0
    #indivdual prices in order of athletes
    Prices = []
    #loop through athletes and assign cost based on chosen plan
    for instance in Athletes:
        Plan_price = 0
        
        #error catching tests to see if the gym plan number is recognised
        if instance.gym_plan in ["1", "2", "3", "4"]:
            Plan_price = plans[instance.get_plan()]
        else:
            #There's no reason way a user can make an inccorect input but if they do somehow, its caught here
            print(instance.get_plan())

        Plan_a_services = Plan_price+(competition_price*int(instance.competitions))+(private_coaching_price*int(instance.coaching_hours))
        #increase total cost
        Price += Plan_a_services
        #add cost to list
        Prices.append(Plan_a_services)

    return [Price, Prices]


def main():
    loop = True
    #main program loop
    while(loop == True):
        #display main menu and options
        print("##########JUDO APP##########\n")
        print("Please type a number for service")
        print("1: Register Athlete")
        print("2: View Athletes")
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
                    #takes user to create an athlete then assigns to Athletes array when finished
                    Athletes.append(Athlete(None, None, None, None, None, None, None, True))
                #list all athletes
                case "2":
                    #gets the cost for all athletes individually and all together 
                    prices = calculate_cost(Athletes)
                    for instance in Athletes:
                        print(f"\nAthlete {Athletes.index(instance)+1}:")
                        instance.print_info()
                        print(f"-Charge: £{prices[1][Athletes.index(instance)]}/Month")
                    print(f"\nTotal: £{prices[0]}/Month")
                    input("Press Enter to go back to menu...")
                
                #delete athlete
                case "3":
                    #lists all athletes for user to see
                    for instance in Athletes:
                        print(f"\nAthlete {Athletes.index(instance)+1}:")
                        instance.print_info()
                    #prompts user for choice and removes whitespace from sides
                    delete_Attempt = input("Enter the number of the Athlete you want to delete:")
                    delete_Attempt = delete_Attempt.strip()

                    #try and convert user input to int for reading
                    try:
                        #int conversion
                        delete_Attempt = int(delete_Attempt[0])
                        #check if input is above zero and less or equal to number of athletes
                        if delete_Attempt > 0 and delete_Attempt <= len(Athletes):
                           #deletes athletes
                            del Athletes[delete_Attempt-1]
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