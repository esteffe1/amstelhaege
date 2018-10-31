class amstel:

    # class attribute
    species = "houses"

    # instance attribute
    def __init__(self, name, width, length, value):
        self.name = name
        self.width = width
        self.length = length
        self.value = value
        
    def area(self):
        self.area = self.length * self.width
        
        return self.area