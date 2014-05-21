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
       
       
class Player(object): 
    def __init__(self, name, stomach, bladder, points, drunkenness): 
        self.name = name
        self.stomach = stomach
        self.points = points
        self.bladder = bladder
        self.drunkenness = drunkenness


    def eat(self, sushi):
        self.sushi = sushi
        self.stomach.append(sushi)
        self.points += sushi.points
        for x in self.stomach:
            print "%s has eaten %s" % (self.name, x)
        print "%s has %d points" % (self.name, self.points)
        
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
       
   
stom = [] # empty list for stomach  this list should be created in Player for each player rather than being stored here.
blad = [] # empty list for player bladder this list should be created in Player rather than being stored here.

edamame = Sushi("edamame", 1)
maki = Sushi("maki", 5)
spiderroll = Sushi("spider roll", 7)
rainbowroll = Sushi("rainbow roll", 10)

sapporo = Beer("Sapporo", 20)

Conan = Player("Conan", stom, blad, 0, 0)
claude = Player("Claude", stom, blad, 0, 0)

Conan.eat(maki)
Conan.eat(spiderroll)
Conan.drink(sapporo)
claude.drink(sapporo)
