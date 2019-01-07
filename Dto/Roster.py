class Roster(object):

	def __init__(self, Federation, FederationLogo,Competition, Club, Initials, Date, DateDoc, Categories = [], Rules = []):
		self.Federation = Federation
		self.FederationLogo = FederationLogo
		self.Competition = Competition
		self.Club = Club
		self.Initials = Initials
		self.Date = Date
		self.DateDoc = DateDoc
		self.Categories = Categories
		self.Rules = Rules
	
	def set_categories(self, categories):
		self.Categories = categories
		
	def set_rules (self, rules):
		self.Rules = rules
		
	def get_categories(self):
	
		categories = []
		
		for category in self.Categories:
			categories.append(category.get_category())
			
		return categories
