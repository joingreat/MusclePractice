class Bug(object):
    legs = 0
    distance = 0

    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    
    def Walk(self):
        self.distance +=1
    
    def ToString(self):
        return self.name + \
             "has" +\
             str(self.legs) +\
             "and taken"+\
             str(self.distance)+\
             "steps. "   