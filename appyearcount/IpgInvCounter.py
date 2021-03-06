import re, csv, os, glob
from collections import Counter
import os

overallcount = Counter() # This will count the number of inventors in each year while running the entire script

def IpgInvCounter(xmlfilename = 'ipg050201.xml'):
    splitfiles = open(xmlfilename, 'r').read().split('<application-reference ') # split it with tags
    pathpiece = xmlfilename.split('/') # put the file directory into pieces
    filename = pathpiece[-1] # name of the xml file
    fileyear = pathpiece[-2] + '/' if len(pathpiece) > 1 else '' # year of the xml file

    c = Counter()
    for f in splitfiles:
        m = re.search(re.escape("<date>") + "(.*?)" + re.escape("</date"), f).group(1)[0:4]
        c[m] = c[m]+1
        overallcount[m] = overallcount[m] + 1
    
    csvfilepath = os.path.dirname(os.path.abspath(__file__)) + '/'+fileyear + filename.replace("xml", "csv") # path that will save its csv file

    print 'wrote to', csvfilepath

    writer = csv.writer(open(csvfilepath, 'wb'))
    for k, v in c.items():
        writer.writerow([k,v])

if __name__ == "__main__":
    start = 2004
    end = 2011
    for year in range(start,end): # patent from [start,end)
        print 'parsing for year: '+str(year)
	xmlfiles = glob.glob('/data/patentdata/patents/'+str(year)+'/ipg*.xml')
        for xmlf in xmlfiles:
            print 'parsing for file: '+xmlf
            IpgInvCounter(xmlf)
    
    writer = csv.writer(open('overallcount', 'wb'))
    
    for k, v in sorted(overallcount.items()):
        writer.writerow([k,v])
    

    #Below code was wrote in order to test in local
    #IpgInvCounter()
    #IpgInvCounter('ipa130131.xml')
