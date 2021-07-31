import requests

#Finding the Diffrent element's position
def DiffFinder(s1,s2):
    DiffIndex = []
    indexno = 0
    while len(DiffIndex) < 2 and indexno < len(s1) and len(s1) == len(s2):
        if s1[indexno] == s2[indexno]:
            indexno += 1
        else:
            DiffIndex.append(indexno)
            indexno += 1
    if len(DiffIndex) == 1 and len(s1) == len(s2):
        return DiffIndex[0]
    else:
        return 0

Link1 = input('Please input the First Link : ')
Link2 = input('Please input the Second Link : ')

Diffindex = DiffFinder(Link1,Link2)

if Diffindex == 0:
    print('Something went wrong! either the links aren\'t Suitable or entry wrong!')
else:
    if Link1[Diffindex-1] == '0':
        Links = []
        LinkCounter = 1
        NewLink = Link1[:Diffindex-(len(str(LinkCounter))-1)] + str(LinkCounter) + Link1[Diffindex+1:]
        while requests.get(NewLink,stream=True):
            Links.append(NewLink)
            LinkCounter += 1
            NewLink = Link1[:Diffindex-(len(str(LinkCounter))-1)] + str(LinkCounter) + Link1[Diffindex+1:]
        for each in Links:
            print(each)
    else:
        Links = []
        LinkCounter = 1
        NewLink = Link1[:Diffindex] + str(LinkCounter) + Link1[Diffindex+1:]
        while requests.get(NewLink,stream=True):
            Links.append(NewLink)
            LinkCounter += 1
            NewLink = Link1[:Diffindex-(len(str(LinkCounter))-1)] + str(LinkCounter) + Link1[Diffindex+1:]
        for each in Links:
            print(each)
stop = input('Continue... ')
