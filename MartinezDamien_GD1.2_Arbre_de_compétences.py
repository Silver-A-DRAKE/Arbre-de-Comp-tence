class ArbreComp():

    compteurNoeud = 0
    compteurArbre = 0
    __levelUpSkill = 2

    def __init__(self, name, levelUpSkill):
        self.__skillName = name
        self.__skillPoint = 0
        self.__leftChild = None
        self.__rightChild = None
        self.__levelUpSkill = 2
        ArbreComp.compteurNoeud +=1 
        ArbreComp.compteurArbre +=1 


    def setName (self, name):
        self.__skillName = name

    def setLeftChild(self, leftChild):
        self.__leftChild = leftChild

    def setRightChild(self, rightChild):
        self.__rightChild = rightChild

    def getlevelUpSkill ():
        return ArbreComp.__levelUpSkill

    def getDepth (self):
        #si aucun enfant
        if ( self.__leftChild == None and self.__rightChild == None):
                return 0
        #si enfant a gauche
        if ( self.__leftChild == True and self.__rightChild == None):
            return 1 + self.__leftChild.getDepth()
        #si enfant a droite
        if ( self.__leftChild == None and self.__rightChild == True):
            return 1 + self.__rightChild.getDepth()
        # si deux enfants:
        if ( self.__leftChild == True and self.__rightChild == True):
            return 1 + self.__leftChild.getDepth() + self.__rightChild.getDepth()
    
class SkillTree ():
    def SkillTree (self):
        self.A.lvlUpSkill():
            SkillTree A1
            A.setLeftSkillTree(A1)
            SkillTree A2
            A.setRightSkillTree(A2)

print(A)
print(A.getDepth())

