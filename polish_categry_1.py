f = open("enumeratedCategorical.txt","r")
g = open("train_categoricalLibSVM.txt","w")

a = f.readline()
count = 0

for i in f:
	
	print count
	
	data = ['none'] * 2140 ##the training file contains 2141 values in each line,1 is removed in data, the id  

	x = i.split(",")
	for j in range(1,2141):
		data[j-1] = x[j]

	line = ""

	for i in range(0,2140):
		if data[i] == '':	##substitue all the features without any values with 0
			data[i] = '0'
		if data[i] == '\n':
			data[i] = '0'
		line = line + (str(i)+":"+str(data[i]) + " ")
	
	line = line + "\n"

	if line == "\n":
		line = ""
		break

	
	g.write(line)
	count += 1


	




