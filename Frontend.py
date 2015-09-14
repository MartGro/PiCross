__author__ = 'martin'
import ConfigParser
import PicrossAlgorithms
import GameConfiguration
import time
t=time.time()
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





#print row_possibilities
#print column_possibilities
#for col in column_concurr:
#    print col
#print "\n\n"
#for row in row_concurr:
#    print row
#
#print "\n\n"
#print column_possibilities
#print PicrossAlgorithms.ImprovedReducePossibilities(column_possibilities,row_concurr[4],4)

ct=0
while(PicrossAlgorithms.CheckFinished(row_possibilities)==False or PicrossAlgorithms.CheckFinished(column_possibilities)==False):

             for i in range(row_concurr.__len__()):
                 column_possibilities=PicrossAlgorithms.ImprovedReducePossibilities(column_possibilities,row_concurr[i],i)
                 #print len(row_possibilities[i])

             for i in range(column_concurr.__len__()):
                 row_possibilities=PicrossAlgorithms.ImprovedReducePossibilities(row_possibilities,column_concurr[i],i)

             #print "p1"
             #print column_possibilities
             #print row_possibilities
             #print "p2"
             #print column_concurr
             #print row_concurr
             #print time.time()
             #print ct
             ct+=1
             #print ct
             column_concurr=PicrossAlgorithms.CheckSet(column_possibilities,column_concurr)
             row_concurr=PicrossAlgorithms.CheckSet(row_possibilities,row_concurr)
             #print "while finished"
             column_concurr=map(PicrossAlgorithms.FindConcurrence,column_possibilities)
             row_concurr=map(PicrossAlgorithms.FindConcurrence,row_possibilities)

             #for elem in row_possibilities:
             #   print elem

             #print "\n\n"

             #for elem in column_possibilities:
             #    print elem
             #raw_input()




print ct
print "Execution time: %s" %(time.time()-t)

for col in column_concurr:
    print col
print "\n\n"
for row in row_concurr:
    print row

def printx(x):
    print x