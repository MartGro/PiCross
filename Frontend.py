__author__ = 'martin'
import ConfigParser
import PicrossAlgorithms
import GameConfiguration
#import sys,os
#sys.path.append(os.path.realpath('..'))
#print sys.path

#config =ConfigParser.RawConfigParser()
#config.read("GameConfiguration.txt")
#side_len=config.get("GameDefinition","side_len")
#rows = config.get("Rows","rows")
#columns= config.get("Columns","columns")
#print rows.split(";")

rows =GameConfiguration.rows
columns=GameConfiguration.columns
print "no.Rows:%s, no.Columns:%s " % (rows.__len__(),columns.__len__())
side_len=GameConfiguration.side_len
row_possibilities = []
for elem in rows:
    row_possibilities.append(PicrossAlgorithms.PossibleArrangements(elem,side_len))

column_possibilities = []
for elem in columns:
    column_possibilities.append(PicrossAlgorithms.PossibleArrangements(elem,side_len))

column_concurr=map(PicrossAlgorithms.FindConcurrence,column_possibilities)
row_concurr=map(PicrossAlgorithms.FindConcurrence,row_possibilities)


print row_possibilities
print column_possibilities
for col in column_concurr:
    print col
print "\n\n"
for row in row_concurr:
    print row