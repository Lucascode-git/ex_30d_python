class LibraryMember:
    def __init__(self, firstname, lastname,):
        self.firstname = firstname
        self.lastname = lastname
        self.borrowed = {}
        self.returned = {}
    
    def borrow_book(self, title, date):
        self.borrowed[title]=date
    def return_book(self, title, date):
        self.returned[title]=date
    def total_borrowed(self):
        return len(self.borrowed)
    def total_returned(self):
        return len(self.returned)
    def books_in_hand(self):
        return [book for book, date in self.borrowed.items() if book not in self.returned]
    def member_info(self):
        in_hand = self.books_in_hand()
        return f'''\n++++++++++++++++++++++++++++++++++++++++++++++++
----------------- {self.firstname} {self.lastname} ------------------\n
Book currently borrowed: {' // '.join(in_hand)}
Book to return: {len(in_hand)}\n
Number of book borrowed since registration: {self.total_borrowed()}
Number total of book returned: {self.total_returned()}
\n++++++++++++++++++++++++++++++++++++++++++++++++'''
    
lm = LibraryMember('Lucas', 'MARIE')
lm.borrow_book('Python crash course', '25/07/26')
lm.borrow_book('Why are we spleeping', '20/09/2024')
lm.borrow_book('Ego is the ennemy', '15/08/26')
lm.return_book('Python crash course', '25/09/26')
print(lm.member_info())