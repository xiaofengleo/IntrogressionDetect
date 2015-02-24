#Author:Xiaofeng Liao. Date:20 Feb 2015
#A python script which can extract specific sequences from MAF files. A
#MAF file usually larger than 10 GB. Specifically, this script scan the
#file line by line, pick the lines starts with s, which means that
#line is a sequence. In addition, only the alignment block with exactly
#7 sequences are extract. Any alignment with more than or less than 7
#sentences are discarded. The extracted 7 sequences are printed line by
#line without blank lines among them. Among each alignments, a blank
#line is printed to as a separation mark.
import fileinput
list = []
for line in fileinput.input("hg38.7way.maf"):
	if not line in ['\n']:#if the line is not empty, go on check it
		if line.startswith("s"):#if it starts with s
			#split the line and get the 7th section, the text
			sections = line.split()
			text = sections[6]#get the 7th section, 0 indexd
			list.append(text)
	else:#if the line is empty, then output the contents in the list
		if len(list) == 7:
			maxLen = 0
			for item in list:
				if len(item)>maxLen:
						maxLen = len(item)
			for item in list:
				if len(item)<maxLen:
					item.ljust(maxLen,'0')
				print item
			print '\n',#add a blank line as a separation
		list = []
