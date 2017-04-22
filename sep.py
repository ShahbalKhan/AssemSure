import pandas as pd 

f = open("../balanced_train_joined.csv","r")
g = open("50_balanced_train.csv","w")

a = f.readline()
g.write(a)


count = 0
line_counter = 0


for i in f:
	x = i.split(",")
	if x[969] == "0":
		count += 1
	if count == 4:
		g.write(i)
		line_counter += 1
		count = 0
	if x[969] == "1":
		g.write(i)
		line_counter += 1

print line_counter

f.close()
g.close()
