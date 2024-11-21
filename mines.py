"""
le fichier contient la classe mine et flags
"""
class Mine:
    """ la classe mine contient le code de la mine
        La méthode getPos renvoie un tupple avec la position X et Y de la mine
    """
    def __init__(self,posX,posY):
        self._posX = posX
        self._posY = posY
    def getPos(self):  
        return (self._posX,self._posY)
    
class Flag:
    """ la classe qui implémente les drapeaux
        La méthode getPos permet de récupérer un tupple avec la position en X et en Y    
    """
    def __init__(self,posX,posY):
        self._x = x
        self._y = y
