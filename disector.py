import csv

file = 'data.csv'
elementsInEachFile = 5000
readFile = []

with open(file, 'r') as file:
	csv1 = csv.reader(file)

	for item in csv1:
		readFile.append(item)
  
def divide_chunks(readFile, n):
	for i in range(0, len(readFile), n): 
		yield readFile[i:i + n]
  
x = list(divide_chunks(readFile, elementsInEachFile))

for i in range(len(x)):
	with open(f'chunk-{i + 1}.csv', 'w', newline = '') as file:
		writer = csv.writer(file)
		for element in x[i]:
			writer.writerow(element)




