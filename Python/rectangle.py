
class Rectangle :
    'This is Rectangle class'
    
    def __init__(self, width, height):
         
        self.width= width
        self.height = height
    
     
     
    def getWidth(self):        
        return self.width
     
     
    def getHeight(self):        
        return self.height
 
    
    def getDT(self):
         
        return self.width * self.height
 
    
    
    def getCV(self):
	return (self.width + self.height) * 2
