class Category:
    
	def __init__(self, CategoryName, Members = []):
		self.CategoryName = CategoryName
		self.Members = Members
		self.MembersNo = len(Members)

	def set_members(self, members):
		self.Members = members
		self.MembersNo = len(self.Members)
		
	def get_category(self):
		members= []
		
		members.append(['<b>'  + self.CategoryName+':</b>' + '<b>' + str(self.MembersNo) + '</b>'])
		members.append(['<b>C</b>', '<b>Licencia</b>', '<b>Nombre y apellidos</b>', '<b>DNI</b>', '<b>F.Nacimiento</b>', '<b>Nacionalidad</b>', '<b>Dorsal</b>'])
		
		for member in self.Members:
			members.append(member.get_member_data())
			
		return members
