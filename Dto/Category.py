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
		
		members.append([self.CategoryName+':'+str(self.MembersNo)])
		members.append(['C','Licencia','Nombre y apellidos', 'DNI', 'F.Nacimiento', 'Nacionalidad', 'Dorsal'])
		
		for member in self.Members:
			members.append(member.get_member_data())
			
		return members
