from datetime import datetime
class Book:
    def __init__(self,title,author,pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year
    def getAgeOfTheBook(self):
        return ((datetime.now().year) - (self.pub_year))
    
p1 = Book("Learn Python", "Paarivendan", 1991)
print("Age of the Book : ", p1.getAgeOfTheBook())