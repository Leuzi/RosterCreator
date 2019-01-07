class Roster(object):

	def __init__(self, Federation, FederationLogo,Competition, Club, Date):
		self.Federation = Federation
		self.FederationLogo = FederationLogo
		self.Competition = Competition
		self.Club = Club
		self.Categories = []
		self.Rules = []
		self.Date = Date
	
	def set_categories(self, categories):
		self.Categories = categories
		
	def set_rules (self, rules):
		self.Rules = rules	