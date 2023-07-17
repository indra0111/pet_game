import time

class Pet:
    # initializes name, hunger, happiness and clock variables where name vaiable stores name 
    # of the pet,hunger stores its hunger level, happiness stores its happiness level and 
    # clock stores time since the hunger level has been updated.
    def __init__(self, name, hunger, happiness, clock):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
        self.clock=clock
        
    # updates hunger level by adjusting time and incrementing it by 1 unit for every 5 seconds
    def hunger_update(self):
        self.hunger=min(100,self.hunger+round(0.2*(time.time()-self.clock)))
        self.clock=time.time()
        
    # Each time the pet is fed, its hunger level decreases by 10 units
    def feed(self):
        self.hunger_update()
        self.hunger=max(self.hunger-10, 0)
        print(f"Your pet's hunger level has been decreased to {self.hunger}")
        print("Do you want to feed your pet again?")
        num=int(input("Enter 1 to feed again and 2 to return to previous menu."))
        if num==1:
            self.feed()
        elif num==2:
            return
        else:
            print("Invalid input. Try again.")
        
    # increases pet's happiness by 10 units each time a player plays with it
    def make_happy(self):
        self.happiness=min(self.happiness+10, 100)
        print(f"Your pet's happiness has been increased to {self.happiness}")
        print("Do you want to play wth your pet again?")
        num=int(input("Enter 1 to play again and 2 to return to previous menu."))
        if num==1:
            self.make_happy()
        elif num==2:
            return
        else:
            print("Invalid input. Try again.")
    
    # prints pet's name, hunger and happiness
    def checkStatus(self):
        self.hunger_update()
        print(f"Your pet's name is {self.name}, its hunger level is {self.hunger} and its happiness level is {self.happiness}.")
    
# Game class inherits pets features
class Game(Pet):
    # updates name of the pet
    def start(self):
        name=input("Enter the name of your pet: ")
        self.name=name
    
    # gives player options to feed, play and check status
    def play(self):
        while True:
            num=int(input("Enter 1 to feed, 2 to play, 3 to check status or 4 to return to previous menu: "))
            if num==1:
                self.feed()
            elif num==2:
                self.make_happy()
            elif num==3:
                self.checkStatus()
            elif num==4:
                return
            else:
                print("Invalid input. Try again.")
    
    # ends game by printing final values of pet's happiness and hunger
    def end(self):
        self.hunger_update()
        print(f"The final status of your pet is:\n happiness: {self.happiness}\n hunger: {self.hunger}")
    
  
# Starting the game by creating an object of game class  
game=Game("", 50, 50,time.time())
game.start()
while True:
    key=int(input("Enter 1 to play or 2 to quit: "))
    if(key==1):
        game.play()
    elif key==2:
        game.end()
        break
    else:
        print("Invalid input. Try again.")
