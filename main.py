import sys
import Generator

def main(jsonFile):
	Generator.Generate(jsonFile)
  
if __name__== "__main__":
	main(sys.argv[1])