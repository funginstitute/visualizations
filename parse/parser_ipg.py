import re, sys
from collections import Counter


def main(argv):
	argv = argv.split(" ")
	if len(argv) > 2:
		argv = argv[0:-1]
	count = Counter() #dictionary contains all the count
	for file in argv:
		print str(file + " hi")
		data = open(str(file), 'r').read()
		year = {}
		f = open('./count.csv','w')
		datasplit = data.split("<application-reference ")
		for string in datasplit[0:]:
			result = (re.search(re.escape('<date>') + "(.*)" + re.escape('</date>'), string).group(1))
			result = result[0:4]
			count[result] += 1
	for key, value in count.iteritems():
		f.write(key + ' ' + str(value) + '\n')
	

if __name__ == '__main__':
	main(sys.argv[1])
	print "here"
	print sys.argv[1]
