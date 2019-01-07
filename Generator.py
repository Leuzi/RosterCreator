import json
from Dto.Roster import Roster
from Dto.Category import Category
from Dto.Member import Member
from pprint import pprint

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def Generate(jsonFile):
	
	data = open_json_file(jsonFile)
	
	roster = create_roster(data)
	
	print_roster(roster)	

def open_json_file(jsonFile):
	data = []
	
	print("Loading data")
	
	with open(jsonFile) as f:
		data = json.load(f)
		
	pprint(data)
	
	print("Data loaded")
	
	return data
	
def create_roster(data):

	print("Loading roster")

	roster = Roster(data['Federation'],data['FederationLogo'],data['Competition'],data['Club'],data['Date'])
	categories = []
	
	for category in data['Categories']:
		newCategory = Category(category['CategoryName'])
		members = []
		
		for member in category['Members']:
			newMember = Member(member['C'],member['Licence'],member['FullName'],member['ID'],member['BirthDate'],member['Country'],member['Number'])
			members.append(newMember)
			
		newCategory.set_members(members)
		
		categories.append(newCategory)
		
	roster.set_categories(categories)
	
	print("Roster loaded")
	
	return roster
	
def print_roster(roster):
	doc = SimpleDocTemplate("complex_cell_values.pdf", pagesize=letter)
	# container for the 'Flowable' objects
	elements = []
	 
	styleSheet = getSampleStyleSheet()
	 
	I = Image('replogo.gif')
	I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
	I.drawWidth = 1.25*inch
	P0 = Paragraph('''
				   <b>A pa<font color=red>r</font>a<i>graph</i></b>
				   <super><font color=yellow>1</font></super>''',
				   styleSheet["BodyText"])
	P = Paragraph('''
		<para align=center spaceb=3>The <b>ReportLab Left
		<font color=red>Logo</font></b>
		Image</para>''',
		styleSheet["BodyText"])
	data= [['A', 'B', 'C', P0, 'D'],
		   ['00', '01', '02', [I,P], '04'],
		   ['10', '11', '12', [P,I], '14'],
		   ['20', '21', '22', '23', '24'],
		   ['30', '31', '32', '33', '34']]
	 
	t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
						('BOX',(0,0),(1,-1),2,colors.red),
						('LINEABOVE',(1,2),(-2,2),1,colors.blue),
						('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
						('BACKGROUND', (0, 0), (0, 1), colors.pink),
						('BACKGROUND', (1, 1), (1, 2), colors.lavender),
						('BACKGROUND', (2, 2), (2, 3), colors.orange),
						('BOX',(0,0),(-1,-1),2,colors.black),
						('GRID',(0,0),(-1,-1),0.5,colors.black),
						('VALIGN',(3,0),(3,0),'BOTTOM'),
						('BACKGROUND',(3,0),(3,0),colors.limegreen),
						('BACKGROUND',(3,1),(3,1),colors.khaki),
						('ALIGN',(3,1),(3,1),'CENTER'),
						('BACKGROUND',(3,2),(3,2),colors.beige),
						('ALIGN',(3,2),(3,2),'LEFT'),
	])
	t._argW[3]=1.5*inch
	 
	elements.append(t)
	# write the document to disk
	doc.build(elements)