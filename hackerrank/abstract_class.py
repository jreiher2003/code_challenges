from abc import ABCMeta, abstractmethod

class Book(object):
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   

    @abstractmethod
    def display(): pass 

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price 

    def display(self): 
        print "Title: %s" % self.title 
        print "Author: %s" % self.author 
        print "Price: %s" % self.price


new_novel = MyBook("Yo son this is a title", "A$AP Reiher", 29.90)
new_novel.display()