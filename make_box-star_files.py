## Star file with no header
## First two columns are X and Y
## Column 7 is the micrograph name
import os

Xcoordinate = 0
Ycoordinate = 1
micrographname = 6

for x in ["T00","T10","T20","T30","T40","T50"]:
	f = open(x + "_Particles.lst","r")
	j = f.readlines()
	data = {}
	for i in j:
		k = i.split()
		micrograph = k[micrographname].split("/")[1]
		if micrograph in data:
			data[micrograph].append(k[Xcoordinate] + " " + k[Ycoordinate])
		else:
			data[micrograph] = []
			data[micrograph].append(k[Xcoordinate] + " " + k[Ycoordinate])
	f.close()

	for i in data:
		f = open(x + "/" + i[:-4] + "_centeredpicks.star","w")
		f.write("data_" + "\n\n")
		f.write("loop_" + "\n")
		f.write("_rlnCoordinateX #1" + "\n")
		f.write("_rlnCoordinateY #2" + "\n")
		os.system("ln -s ../../../../../../../../../leginon/yztan/17jan21b/rawdata/" + i[:-7] + ".mrc " + x + "/" + i)
		for j in data[i]:
			f.write(j + "\n")
		f.close()
		