import json
from Dto.Roster import Roster
from Dto.Category import Category
from Dto.Member import Member
from pprint import pprint

import io

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus.tables import TableStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image

def Generate(jsonFile):
	
	data = open_json_file(jsonFile, )
	
	roster = create_roster(data)
	
	print_roster(roster)	

def open_json_file(jsonFile):
	data = []
	
	print("Loading data")
	
	with open(jsonFile, encoding="utf-8") as f:
		data = json.load(f)
		
	pprint(data)
	
	print("Data loaded")
	
	return data
	
def create_roster(data):

	print("Loading roster")

	roster = Roster(data['Federation'],data['FederationLogo'],data['Competition'],data['Club'], data['Initials'] ,data['Date'], data['DateDoc'])
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
	doc = SimpleDocTemplate(get_document_name(roster), pagesize=A4, rightMargin=3*cm,leftMargin=3*cm, topMargin=5*cm,bottomMargin=2*cm)
	elements = []
	 
	data = roster.get_categories()[0]
	
	
	#Configure style and word wrap
	s = getSampleStyleSheet()
	s = s["BodyText"]
	s.wordWrap = 'CJK'
	data2 = [[Paragraph(cell, s) for cell in row] for row in data]
	t=Table(data2, colWidths=[0.7*cm, 4.2*cm, 6*cm, 2.4*cm, 2.6*cm, 2.8*cm, 1.5*cm], repeatRows=1)
	
	
	data_len = len(data)
	
	for each in range(data_len):
		if each % 2 == 0:
		    bg_color = colors.whitesmoke
		else:
		    bg_color = colors.white

		t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))
		
	#TODO: Get this line right instead of just copying it from the docs
	style = TableStyle([('SPAN',(0,0),(6,0)),
						('BACKGROUND',(0,0),(6,1),colors.lightgrey),						
						('FONTSIZE', (1, 0), (1, 1), 18),
						('TEXTFONT', (1, 0), (1, 1), 'Times-Bold'),
		                   ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		                   ('BOX', (0,0), (-1,-1), 0.25, colors.black),
		                   ])
	t.setStyle(style)
	#Send the data and build the file
	elements.append(t)
	doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)
	 

def get_document_name(roster):
	return "Roster_"+roster.Initials+"_"+roster.Competition+"_"+roster.DateDoc+".pdf"
	
def header_footer(canvas, doc):
	# Save the state of our canvas so we can draw on it
	canvas.saveState()
	im = Image.open("logoFafa.jpeg")
	styles = getSampleStyleSheet()

	canvas.drawInlineImage(doc,im,canvas,doc.leftMargin, doc.height + doc.topMargin)
	
	# Header
	header = Paragraph('Federación Andaluza de Fútbol Americano', styles['Normal'])
	w, h = header.wrap(doc.width, doc.topMargin)
	header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
	
	header = Paragraph('Rosters Oficiales', styles['Normal'])
	w, h = header.wrap(doc.width, doc.topMargin)
	header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
	
	
	
	# Footer
	footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
	w, h = footer.wrap(doc.width, doc.bottomMargin)
	footer.drawOn(canvas, doc.leftMargin, h)

	# Release the canvas
	canvas.restoreState()