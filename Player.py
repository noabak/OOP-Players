
class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals =goals
        self.yellow_cards = yellow_cards
        self.red_cards =  red_cards

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

print("Do you want to create a football player or a basketball player data?.")
option=input("F) for football player, B) for basketball player:")
while True:

 if option.upper()=="F":

    first_name = input("Please enter the first name:")
    last_name= input("Please enter the last name:")
    weight_kg= float(input("Please enter the weight in kg:"))
    height_cm=float(input("Please enter the height in cm:"))
    goals= int(input("Please enter number of goals:"))
    yellow_cards=int(input("Please enter the number of yellow cards:"))
    red_cards=int(input("Please enter the number of red cards:"))
    player = FootballPlayer(first_name,last_name,height_cm,weight_kg,goals,yellow_cards,red_cards)

    with open("Players.txt", "a+") as desc_file:
        desc_file.writelines(str(player.__dict__)+"\n")
    print("Your player is successfully created!")
    break

 elif option.upper()=="B":

    first_name = input("Please enter the first name:")
    last_name = input("Please enter the last name:")
    weight_kg = float(input("Please enter the weight in kg:"))
    height_cm = float(input("Please enter the height in cm:"))
    assists= int(input("Please enter the number of assits:"))
    points= int(input("Please enter the number of points:"))
    rebounds= int(input("Please enter the number of rebounds:"))
    player= BasketballPlayer(first_name,last_name,height_cm,weight_kg,points,rebounds,assists)
    with open("Players.txt", "a+") as desc_file:
        desc_file.writelines(str(player.__dict__) + "\n")
    print("Your player is successfully created!")
    break

 else:
    print("The option you entered is not correct!")
    option= input("Please enter a correct option! F) football player, B) basketball player:")






