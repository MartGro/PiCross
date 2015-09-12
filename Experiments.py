
__author__ = 'martin'
import PicrossAlgorithms as PA


def Incrementer(number,base,len):
    #print "IncCall w/ :%s,%s,%s" %(number,base,len)
    val=[]
    for i in range(int(number)):
        #print "inc rout nr %s"%i
        lis=BaseConversion(i,base,len)
        if lis==sorted(lis):
            val.append(lis)
    return val

def BaseConversion(number,base,len):
    if base == 0:
        return [0 for i in range(len)]
    elif  base == 1:
        print "Enter"
        stor=[]
        for i in range(number):
            stor.append(1)
        while stor.__len__()<len:
            stor.append(0)
        stor.reverse()
        return stor
    else:
        flag=False
        stor = []
        while flag!=True:
            stor.append(number%base)
            number=int(number/base)
            if number<1:
                flag=True
        while stor.__len__()<len:
            stor.append(0)
        stor.reverse()
        return stor


