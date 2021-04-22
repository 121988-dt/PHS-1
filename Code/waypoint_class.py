class Waypoint:
    """ A simple class that contains waypoint information """


    def __init__(self, x,y,z,wp_type):
        self.x = x
        self.y = y
        self.z = z
        self.wptype = wp_type


    def getX(self):
        return self.x 
    def getY(self):
        return self.y 
    def getZ(self):
        return self.z
    def getWPType(self):
        return self.wptype

    def setX(self,new_x):
        self.x = new_x
        return
    def setY(self,new_y):
        self.y = new_y
        return
    def setZ(self,new_z):
        self.z = new_z
        return
    def setType(self,new_type):
        self.wptype = new_type
        return       