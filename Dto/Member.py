class Member:
    
    def __init__(self, Captain,Licence,FullName,ID,BirthDate,Country,Number):
        self.Captain = Captain
        self.Licence = Licence
        self.FullName = FullName
        self.ID = ID
        self.BirthDate = BirthDate
        self.Country = Country
        self.Number = Number
        
    
    def get_member_data(self):
    	return [self.Captain, self.Licence, self.FullName, self.ID, self.BirthDate, self.Country, self.Number]
        
