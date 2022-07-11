def divide(a,b):
    try:
        assert type(a) == int  
        assert type(b) == int
        return a/b
    except:
        return None



months = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
class Date(object):
    years = 2000
    months = 1
    dates = 1
    
    def __init__(self , month = 1,date = 1,year = 2000):
        self.month, self.day, self.year = month, date, year

    def getmonth(self): return (self.month)
    def getday(self): return (self.day)
    def getyear(self): return (self.year)
    def setmonth(self,m): 
        self.month = m
        return
    def setday(self,d):
        self.day = d
        return
    def setyear(self,y):
        self.year = y
        return
    def __str__(self):
        value = ('{}/{}/{} {} {}'.format(self.month,self.day,self.year,months[self.month],self.day))
        return value
