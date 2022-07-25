import math
class Association:
    
    def __init__(self, X , Y):
        self.X = X
        self.Y = Y
        self.XY = []
        self.X2 = []
        self.Y2 = []
        self.Corre = 0
    def Correlation(self):
        for i in range(0,len(self.X)):
                self.XY.append(self.X[i]*self.Y[i])

        for i in range(0,len(self.X)):
                self.X2.append(self.X[i]**2)

        for i in range(0,len(self.X)):
                self.Y2.append(self.Y[i]**2)
        self.Corre =float ((len(self.X)*sum(self.XY))-(sum(self.X)*sum(self.Y)))/math.sqrt(((len(self.X)*sum(self.X2))-(sum(self.X)**2))*((len(self.Y)*sum(self.Y2))-(sum(self.Y)**2)))        
        return "The association between two arrays is "+ str(self.Corre)