#to collect all the lines you encounter until you find an empty line, 
#and then return the lines you have collected so far. 
def lines(file):
	for line in file:
		yield line
		yield '\n'

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []

