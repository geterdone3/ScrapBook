#Known Bugs:
    #None!

import random
import math
import decimal
randomStartSeed = None

ACTIVE = True
TICKSINADAY = 48.0
SPEED = 1.0
TIMERS = []
FLOWERS = []
STARTINGFLOWERS = 200

class Counter:
    def __init__(self, time, x, y, colorC = (0, 0, 0), label = '', clock = 0, periods = 0, textSize = 50.0):
        self.label = label #Label to be displayed
        self.x = x
        self.y = y
        self.colorC = colorC #Color of label
        self.timeUp = time #The amount of time in a period
        self.clock = clock #The internal clock start
        self.periodsPassed = periods #The number of times the period has been reached
        self.textSize = textSize
        
    def tick(self):
        #Tick up the clock
        self.clock += SPEED
        
        #See if we met our time, weird math for overflow
        if self.clock >= self.timeUp:
            self.periodsPassed += self.clock // self.timeUp
            self.clock = self.clock % self.timeUp
            
    def draw(self):
        textFont(FONT, self.textSize)
        fill(*self.colorC)
        textAlign(LEFT)
        
        if self.label == "":
            drawText = str(int(self.periodsPassed))
            if SPEED < 1:
                drawText += " (" + str(SPEED) + "x)"
            else:
                drawText += " (" + str(int(SPEED)) + "x)"
            #Make a function for this stuff later
            
            text(drawText, self.x, self.textSize+self.y)
        else:
            drawText = self.label + ": " + str(int(self.periodsPassed))
            if SPEED < 1:
                drawText += " (" + str(SPEED) + "x)"
            else:
                drawText += " (" + str(int(SPEED)) + "x)"
            #Make a function for this stuff later
            text(drawText, self.x, self.textSize+self.y)
dayCounter = Counter(TICKSINADAY, 0, 0, label = "Day") #(255, 255, 255)


class Landmass:
    def __init__(self, width, height):
        self.landColor = (100, 200, 100)
        if width<=height:
            self.radius = (width/5)*4
        if width>height:
            self.radius = (height/5)*4

    def draw(self, widthh, heighth):
        fill(*self.landColor)
        noStroke()
        ellipse(widthh/2, heighth/2, self.radius, self.radius)


class Dandelion:
    def __init__(self, x, y, germinationTime = 10.0, adultTime = 22.0, flowerSize = 15.0, growthRadius = 20.0, colorC = (0, 0, 0), deathChance = 0.0005, currentGrowth = 0.0, lifeExpectancyMax = 60.0):
        #Notes:
            #Fully grown color: (235, 226, 0)
            #Growing Color:     (0  , 0  , 0)
            
        #Coding Stuff
        self.x = x
        self.y = y
        
        #Gene Stuff
        self.flowerSize = flowerSize
        self.colorC = colorC
        
        #Growing Stuff
        self.germinationTime = germinationTime*TICKSINADAY
        self.adultTime = adultTime*TICKSINADAY
        self.growthRadius = growthRadius
        self.currentGrowth = currentGrowth
        
        #Birthing Stuff
        minSeedTime = 0
        maxSeedTime = 0
        
        #Dying Stuff
        self.dead = False
        self.deathChance = deathChance
        self.lifeExpectancyMax = lifeExpectancyMax*TICKSINADAY
        
        #My Random Seed (haha.. It's pun)
        self.lifeSpan = random.randrange(100)/100.0
        
    def doIDie(self):
        #Random death
        if (self.lifeSpan) < ((-0.1*self._calcDeX() / (self._calcDeX() - 1.0))**4.0):
            self.dead = True
            return
        
        
        deathScore = 0.0 #Probablity of death
        for flower in FLOWERS:
            if not flower == self:
                flowerDistance = sqrt( (self.x - flower.x)**2.0 + (self.y - flower.y)**2.0 )
                if flowerDistance < self.growthRadius: #If a flower is inside my zoooonnnneee!!
                    deathScore += (self.growthRadius - flowerDistance)*self.deathChance

        #Check death
        if random.randrange(100)/100.0 < deathScore:
            self.dead = True
        
    def gestationPeriod(self):
        if not self.colorC == (235, 226, 0) and self.currentGrowth >= self.germinationTime and self.currentGrowth <= self.adultTime and (random.randrange(100)/100.0) < (-0.1*self._calcGeX() / (self._calcGeX() - 1.0))**4.0:
            self.colorC = (235, 226, 0)
        else:
            self.currentGrowth += 1.0
        
    def _calcGeX(self):
        return ((self.adultTime - self.germinationTime)-(self.adultTime - self.currentGrowth)) / (self.adultTime - self.germinationTime)
    
    def _calcDeX(self):
        return (self.lifeExpectancyMax-(self.lifeExpectancyMax-self.currentGrowth)) / self.lifeExpectancyMax
    
    def _calcSeX(self): #Finish this
        return (self.lifeExpectancyMax-(self.lifeExpectancyMax-self.currentGrowth)) / self.lifeExpectancyMax
    
    def seeding(self):
        pass
        
    def draw(self):
        fill(*self.colorC)
        noStroke()
        ellipse(self.x, self.y, self.flowerSize, self.flowerSize)
    
    def tick(self):
        for i in range(int(SPEED)):
            self.doIDie()
            self.gestationPeriod()
            self.seeding()
            
            
def generateFlowers(n, width, height):
    for i in range(n):
        x = random.randrange(0, width)
        y = random.randrange(0, height)
        while sqrt( (x - (width/2.0) )**2.0 + (y - (height/2.0) )**2.0 ) >= (land.radius/2)-5:
            x = random.randrange(0, width)
            y = random.randrange(0, height)
        global FLOWERS
        FLOWERS.append(Dandelion(x, y))


def keyPressed():
    if key==CODED:
        #Adjust Simulation speed
        if keyCode == RIGHT: #FASTER
            global SPEED
            SPEED *= 2.0
        if keyCode == LEFT: #SLOWER
            global SPEED
            SPEED /= 2.0
            if SPEED < 0.25:
                SPEED = 0.25
            
    if key == ' ':
        global ACTIVE
        ACTIVE = not ACTIVE
    
    
def setup():
    size(1500, 1500)
    pixelDensity(displayDensity())
    
    #Create font
    global FONT
    FONT = createFont("Arial", 50, True)
    
    ### Generate World ###
    global land
    land = Landmass(width, height)
    
    #Initialize random start
    random.seed(randomStartSeed)
    generateFlowers(STARTINGFLOWERS, width, height)
    
    
def draw():
    background(60,100,220)
    
    ### Draw Everything ###
    land.draw(width, height)
    dayCounter.draw()
    global FLOWERS
    for flower in FLOWERS:
        flower.draw()
    
    ### Pause Stuffs
    if not ACTIVE:
        fill(0, 0, 0, 75)
        rect(0, 0, width, height)
    
    ### Active Stuffs
    if ACTIVE:
        dayCounter.tick()
        for flower in FLOWERS:
            if flower.dead:
                FLOWERS.remove(flower)
            flower.tick()
            
    