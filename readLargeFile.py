import fileinput
list = []
for line in fileinput.input("hg38.7way.maf"):
	if not line in ['\n']:
		if line.startswith("s"):
			list.append(line)
	else:
		if len(list) == 7:
			for item in list:
				print item,
			print '\n',
		list = []
