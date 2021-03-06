"""class Table(object):
    def __init__(self, food, drink, people): # x is the players, the sushi table, the beer.
        x = self.x  # constantly reloads everything?
        
class Food(object):
    def __init__(self):
        
class SushiDish(Food): # the sushi plate is on the table
    def __init__(self, shrimproll, ):  # can sushi_piece be defined here? the sushi_order is the type of sushi
        sushi_order = self.sushi_order # should contain the time the sushi takes to eat.
    
class Player(object): # contains stored points of player 1 and player 2
    def __init__(self, player, stomach, points): # player is either player 1 or 2
        self.player = player
        self.stomach = stomach
        self.points = points


    def eat(self, sushi):
        self.sushi = sushi
        self.stomach.append(sushi)
        self.points += 1
   
   
class Beer(Food): # contains the beer
    def __init__(self, drink): # drink is the individual beer
        self.drink = drink
   
class VeggieRoll(SushiDish): # contains three pieces of veggie roll, the points gained for each
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
        
class ShrimpRoll(SushiDish): #contains pieces of sushi, + point value
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
    
class TunaRoll(SushiDish):
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece
    
class Edamame(SushiDish):
    def __init__(self, sushi_piece):
        self.sushi_piece = sushi_piece # sushi_piece contains the time the food takes to eat (but this is the same for all sushi?) and the points you recieve once finished eating
""" 



"""class Player(object): 
    def __init__(self, player, stomach, points): 
        self.player = player
        self.stomach = stomach
        self.points = points


    def eat(self, sushi):
        self.sushi = sushi
        self.stomach.append(sushi)
        self.points += 1
        for x in self.stomach:
            print x
        print self.points
        
class Sushi(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def __str__(self):
        return self.name """
       
       
"""class Player(object): 
    def __init__(self, name, stomach, bladder, points, drunkenness): 
        self.name = name
        self.stomach = stomach
        self.points = points
        self.bladder = bladder
        self.drunkenness = drunkenness
        
    def create_organs(self):
        if self.stomach == -10:
            self.stomach = []
        if self.bladder == -10:
            self.bladder = []

    def eat(self, sushi):
        self.sushi = sushi
        self.stomach.append(sushi)
        self.points += sushi.points
        for x in self.stomach:
            print "%s has eaten %s" % (self.name, x)
        print "%s has %d fullness points" % (self.name, self.points)
        
    def drink(self, beer):
        self.beer = beer
        self.bladder.append(beer)
        self.drunkenness += beer.drunkpoints
        for x in self.bladder:
            print "%s has drunk %s" % (self.name, x)
        print "%s is %d percent drunk" % (self.name, self.drunkenness)
            
        
class Sushi(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def __str__(self):
        return self.name
        
class Beer(object):
    def __init__(self, name, drunkpoints):
        self.name = name
        self.drunkpoints = drunkpoints
    def __str__(self):
        return self.name
       
   

edamame = Sushi("edamame", 1)
maki = Sushi("maki", 5)
spiderroll = Sushi("spider roll", 7)
rainbowroll = Sushi("rainbow roll", 10)

sapporo = Beer("Sapporo", 20)

conan = Player("Conan", -10, -10, 0, 0)
conan.create_organs()

claude = Player("Claude", -10, -10, 0, 0)
claude.create_organs()

conan.eat(maki)
conan.eat(spiderroll)
conan.drink(sapporo)
claude.drink(sapporo)
claude.eat(rainbowroll)"""


class Player(object): 
    def __init__(self, name): 
        self.name = name
        self.stomach = []
        self.points = 0
        self.bladder = []
        self.drunkenness = 0
        self.happiness = 0
        
    def vomit(self):
        self.points = 0
        self.drunkenness = 0
        self.bladder = []
        self.stomach = []
        
    def get_happy(self):
        if self.points >= 20 and self.points <= 100 and self.drunkenness >= 30 and self.drunkenness <= 50:
            happiness = 10
        elif self.points < 20 and self.points > 0:
            happiness = 4
        elif self.points > 100:
            happiness = 12
        elif self.drunkenness < 30 and self.drunkenness > 0:
            happiness = 6
        elif self.drunkenness > 50:
            happiness = 11
        elif self.drunkenness == 0:
            happiness = -1
        elif self.points == 0:
            happiness = 0

    def print_happy(self):
        if happiness == 10:
            print "%s has achieved happiness" % self.name
        elif happiness == 4:
            print "%s is still hungry" % self.name
        elif happiness == 12:
            print "%s has eaten too much and vomited" % self.name
            return self.vomit
        elif happiness == 6:
            print "%s still wants more beer." % self.name
        elif happiness == 11:
            print "%s has drank too much beer and vomited" % self.name
            return self.vomit
        elif happiness == -1:
            print "%s wants beer" % (self.name)
        elif happiness == 0:
            print "%s is hungry" % (self.name)
            

    def eat(self, sushi):
        self.sushi = sushi
        self.stomach.append(sushi)
        self.points += sushi.points
        print "%s has eaten %s" % (self.name, self.stomach[-1])
        print "%s has %d fullness points" % (self.name, self.points)
        self.get_happy
        self.print_happy
        
    def drink(self, beer):
        self.beer = beer
        self.bladder.append(beer)
        self.drunkenness += beer.drunkpoints
        for x in self.bladder:
            print "%s has drunk %s" % (self.name, x)
        print "%s is %d percent drunk" % (self.name, self.drunkenness)
        self.get_happy
        self.print_happy
        
class Sushi(object):
    def __init__(self, name, points):
        self.name = name
        self.points = points
    def __str__(self):
        return self.name
        
class Beer(object):
    def __init__(self, name, drunkpoints):
        self.name = name
        self.drunkpoints = drunkpoints
    def __str__(self):
        return self.name
       
edamame = Sushi("edamame", 1)
maki = Sushi("maki", 5)
spiderroll = Sushi("spider roll", 7)
rainbowroll = Sushi("rainbow roll", 100)

sapporo = Beer("Sapporo", 20)

conan = Player("Conan")

claude = Player("Claude")

conan.eat(maki)
conan.eat(rainbowroll)
conan.eat(rainbowroll)
conan.drink(sapporo)
conan.drink(sapporo)
conan.eat(edamame)
conan.get_happy
conan.print_happy


