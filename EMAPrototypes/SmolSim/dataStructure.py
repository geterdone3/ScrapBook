#We gone have a grid over the screen, each square is 10x10,
 #and we consider the bin that a thing is in and the nine closest bins

class Node:
    def __init__(self, x=0, y=0, uid, close = 20):
        self.x = x
        self.y = y
        self.uid= uid
        self.closeToMe = close

class Bin:
    #This will represent an object
    class _pointer:
        def __init__(self, objecT = None):
            self.myNode = objecT
            self.key = (str(objecT.x), str(objecT.y))
            self.nearBy = {} #A dict of pointers that this thing is close to

    def __init__(self, width, height, sizeOfBins = 20.0):
        #Set up info about the grid
        self.sizeOfBins = sizeOfBins
        self.xBins = (width//sizeOfBins)+1
        self.yBins = (height//sizeOfBins)+1

        #Map objecTs to _pointers:
        self.objectToPointer = {}

        #List organized by type
        self.byType = {} #A dictionary of dictionaries - key dict name (flower)

        #Organized by local
        #The actual grid - [x][y]{pointPointer}
        self.byLocal = [[ {}*self.yBins ]*self.xBins ]


    def insert(self, objecT): #The object needs at least an x/y and a "close" value
        collectionName = type(objecT)
        newPoint = _pointer(objecT)

        #Add internally
        self.objectToPointer[objecT] = newPoint
        self.byType[collectionName][newPoint.key] = newPoint
        self.byLocal[width//self.sizeOfBins][height//self.sizeOfBins][newPoint.key] = newPoint



        #Setup
        self.getNear(collectionName, objecT)


    def remove(self, objecT):
        collectionName = type(objecT)
        return


    def getNear(self, objecT):
        #If this has been calculated before, just return it
        collectionName = type(objecT)
        if (self.holding[collectionName][( str(objecT.x), str(objecT.y) )]):
            return objecT.nearBy

        #If this function has not been called before, set some shit up
        for row in range(-1,2):
            for col in range(-1,2):
                for point in self.cluster[(objecT.x//self.sizeOfBins)+col][(objecT.y//self.sizeOfBins)+row]:

def main():
    #Let's make some random nodes in a bin
    import random

    #Grid of 500x500 with default bin size of 20
    myBin = Bin(500, 500)

    #Add 100 nodes to this bin
    for i in range(100):
        myBin.insert(Node(random.randrange(0, 500), random.randrange(0, 500)))

    ######################  What I want to be able to do  ######################
    #Cycle through and get all of them, to perform operations
    for node in myBin:
        myBin.remove(node)

    #What makes more syntatic sense?
    ##A:
    for node in myBin:
        if len(myBin.getNear(node)) > 3:
            myBin.remove(node)
    ##B:
    #for node in myBin:
    #    if len(node.getNear()) > 3:
    #        node.delete()
    #B doesn't make sense because then you aren't getting your flower.. You're getting something else

    #All we do is add, remove, fetch a node, and get nodes that are near
     #Looks like:

    # Bin.insert(node)
    # Bin.remove(node)
    # Bin.getNear(node)
    # Bin.getAll(Type(Node)) #(get all of a type?)

    #To do this I need to have two lists
     #One organized by type
     #One organized by local

    #Pointer objects not needed for the by-type list

    #Pointer object needed for locality list to store the NearMe list

    #I also need to map every object to a _pointer - Do I?
     #I can do byType[Type(Node)][(Node.x, Node.y)] - gets a flower
     #VS
     #nodeToPointer[Node] - would get a flower pointer
