class Building(object):
    """
    Representation of a room in Adventure
    """

    def __init__(self, name, value, width, length, extra, bonus):
        """ Initialize a building give it an id, name and description """
        self.name   = name
        self.value  = value 
        self.width  = width 
        self.length = length
        self.extra  = extra 
        self.bonus  = bonus

    pass
    
    
class Requirement(object):
    """
    Representation of a room in Adventure
    """

    def __init__(self, name, width, length, pond, water):
        """ Initialize a building give it an id, name and description """       
        self.name   = name       
        self.width  = width 
        self.length = length  
        self.pond   = pond  
        self.water  = water
        
    pass
		