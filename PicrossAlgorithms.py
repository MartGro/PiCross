import itertools
from bitarray import bitarray

__author__ = 'martin'
import bitarray
#import Experiments

def PossibleArrangements(inputtuple, length):
    #returns a list of bitarrays representing possible arrangements for a certain tuple and length
    #PossibleArrangements((2,1,2),8) = [bitarray('11010110'), bitarray('11010011'), bitarray('11001011'), bitarray('01101011')]
    #print "PA called with inputtuple %s and length %s" % (inputtuple,length)
    arrangements = []
    tuplelen=len(inputtuple)

    lenstorage = []
    positionstorage=[]
    lastpostiton=0

    for x in range(inputtuple.__len__()):
        lenstorage.append(inputtuple[x])

    for x in range(inputtuple.__len__()):
        positionstorage.append(lastpostiton)
        lastpostiton=lastpostiton+lenstorage[x]+1
    #print "p1"
    arrangements.append(CreateBitarray(lenstorage,positionstorage,length))
    ost=DetermineOffsetTable(lenstorage,positionstorage,length)
    #print DetermineOffsetTable(lenstorage,positionstorage,length)

    #print "OSTtoPS: %s" % OffsettableToPositionstorage(positionstorage,ost[1])
    ost=map(lambda f:OffsettableToPositionstorage(positionstorage,f),ost)
    arrangements = map(lambda g:CreateBitarray(lenstorage,g,length),ost)
    return arrangements

def OffsettableToPositionstorage(positionstorage,offsettable):
    return map(lambda x,y:x+y,positionstorage,offsettable)

def CreateBitarray(lenstorage,positionstorage,length):
    ar=bitarray.bitarray(length)
    ar.setall(False)
    for x in range(lenstorage.__len__()):
        ar[positionstorage[x]:positionstorage[x]+lenstorage[x]:1]=True
    return ar


def DetermineOffsetTable(lenstorage,positionstorage,length):
    #print "DOT ENTER"
    #print "lenstorage[-1]=%s;postionstorage[-1]=%s]"%(lenstorage[-1],positionstorage[-1])
    max_offset = abs(length-(lenstorage[-1]+positionstorage[-1]))+1
    #print "Max Offset: %s" % (max_offset)
    table = ImprovedOffsetMap(max_offset,positionstorage.__len__())
    #print "DetermineOST for max_offset: %s  and length: %s -> %s" %\
    #      (max_offset,positionstorage.__len__(),table)
    return table

#print PossibleArrangements((2,1,2),8)

def ImprovedOffsetMap(maxval,length):
    #returns a list of possible offsets given a maximum offset (maxval)
    #and the number of elements in the table(length)
    #ImprovedOffsetMap(3,3)=[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 1], [0, 1, 2], [0, 2, 2], [1, 1, 1], [1, 1, 2], [1, 2, 2], [2, 2, 2]]


    #print "IOM called w/ %s; %s" % (maxval,length)
    val = []
    s = ""
    for i in range(maxval):
        s+=str(i)
    #print s
    for x in itertools.combinations_with_replacement(s,length):
        list(x)
        x=map(lambda f:int(f),x)
        val.append(x)
    return val


def FindConcurrence(inp_arrangements):
    #input: List of bitarrays
    #finds concurrent values in all bitarrays and returns a string with 1 for "is true",
    # 0 for "is wrong" and "u" for "undefined"
    if len(inp_arrangements)==1:
        val = inp_arrangements[0]
        val = bitarray.bitarray.to01(val)
        ret = []
        for el in val:
            ret.append(el)
        return ret
    elif len(inp_arrangements)<=0:
        raise TypeError
        return None

    val=[]
    for element in inp_arrangements:
            val.append(element.tolist())
    bitarraylen=val[0].__len__()
    sol=reduce(CompareListElementwise,val)
    return sol


def CompareListElementwise(l1,l2):
    #takes two lists as input and compares them elementwise
    #output is a list
    if len(l1)!=len(l2):
        raise TypeError
        return None
    else:
        val=[]
        i = itertools.imap(CompareTernaryValues,l1,l2)
        for x in i:
            val.append(x)
        return val


def CompareTernaryValues(x,y):
    #returns 1 if both input values are 1, 0 if both are 0, "u" if both is not the case
    if x==1 and y==1:
        return 1
    if x==0 and y==0:
        return 0
    else:
        return "u"

#print FindConcurrence(PossibleArrangements((2,7,2),14))
#print ImprovedOffsetMap(3,3)