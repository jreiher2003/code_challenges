class Book(object):
	checkedOut = False

	def __init__(self, title, pageCount, ISBN, dayCheckedOut):
		self.title = title
		self.pageCount = pageCount
		self.ISBN = ISBN 
		self.dayCheckedOut = dayCheckedOut


class LibraryCatalogue(object):
	bookCollection = {}
	currentDay = 0
	checkoutPeriod = 7
	lateFee = 0.50
	lateFeePerDay = 1.00
	

l = LibraryCatalogue()
l.bookCollection["jeff"] = 1
print l.bookCollection