from sys import maxsize

class Contact:
    def __init__(self,  firstname = None, middlename= None, lastname= None,
                              title= None, company= None, address= None, home= None,
                              mobile= None, fax= None, work= None, email= None,
                              email2= None, email3= None, homepage= None, bday= None,
                              bmonth= None, byear= None, aday= None, amonth= None, ayear= None,
                              address2= None, phone2= None, notes= None, id =None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self. home = home
        self. mobile = mobile
        self.fax = fax
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
