import time

class Pet:
    
    def __init__(self, name, hunger, happiness, clock):
        self.name=name
        self.happiness=happiness
        self.hunger=hunger
        self.clock=clock
        
    def hunger_update(self):
        self.hunger=min(100,self.hunger+round(0.5*(time.time()-self.clock)))
        self.clock=time.time()
        
    def feed(self):
        self.hunger=max(self.hunger-10, 0)
    
    def make_happy(self):
        self.happiness=min(self.happiness+10, 100)
    
    def checkStatus(self):
        self.hunger_update()
        print(f"Your pet's name is {self.name}, its hunger level is {self.hunger} and its happiness level is {self.happiness}.")
    
class Game(Pet):
    
    def start(self):
        name=input("Enter the name of your pet: ")
        self.name=name
    
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
    
    def end(self):
        self.hunger_update()
        print(f"The final status of your pet is:\n happiness: {self.happiness}\n hunger: {self.hunger}")
    
    
game=Game("", 50, 50,time.time())
game.start()
while(1):
    key=int(input("Enter 1 to play or 2 to quit: "))
    if(key==1):
        game.play()
    elif key==2:
        game.end()
        break
    else:
        print("Invalid input. Try again.")