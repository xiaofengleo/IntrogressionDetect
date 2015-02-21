#Author:Xiaofeng Liao. Date:20 Feb 2015
#A python script which can extract specific sequences from MAF files. A
#MAF file usually larger than 10 GB. Specifically, this script scan the
#file line by line, pick the lines starts with “s”, which means that
#line is a sequence. In addition, only the alignment block with exactly
#7 sequences are extract. Any alignment with more than or less than 7
#sentences are discarded. The extracted 7 sequences are printed line by
#line without blank lines among them. Among each alignments, a blank
#line is printed to as a separation mark.
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
