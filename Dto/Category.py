class Category:
    
	def __init__(self, CategoryName, Members = []):
		self.CategoryName = CategoryName
		self.Members = Members
		self.MembersNo = len(Members)

	def set_members(self, members):
		self.Members = members
		self.MembersNo = self.Members
