# Created by Nitin Pathania
#Data analysis of 10 books for work count
import copy
#countwords variable will store all 26 charcaters
countwords="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

linestoread=200500

#to_upper function will take a list and convert all the value in list to upper case if lower case and return them in new list.
def to_upper(oldList):
    newList = []
    for element in oldList:
        newList.append(element.upper())
    return newList

#to_percent function will take two parameters reportlist and charcount. It will provide back a new list with percentage.
def to_percent(reportlist,charcount):
    newList = []
    for element in reportlist:
        newList.append((element/charcount)*100)
    return newList


def diff_percent(percentlist,weblist):
    #newlistmain=[]
    newList = []
    for i in range(0, len(filelist)):
        for j in range(0, len(countwords)):
            if percentlist[i][j] < weblist[j]:
                diff = weblist[j] - percentlist[i][j]
            else:
                diff = percentlist[i][j] - weblist[j]
            newList.append(diff)
    #newlistmain.append(newList)
    return newList


def wordcount(name):
    wordlist=[]
    #lines = [line.rstrip('\n') for line in open('filename')]

    file = open(name,"r", encoding="utf8")
        
    #Read lines all at once, lines contains all the values in list in certain format
    linesmain=file.read(linestoread)
    for char in linesmain:
        wordlist.append(char)
    #Closing the file
    file.close()

    while '\ufeff' in wordlist:
        wordlist.remove('\ufeff')

    while '\n' in wordlist:
        wordlist.remove('\n')

    #print (len(wordlist)) 
    #print (wordlist)

    newwordlist = to_upper(wordlist)
    totalcharcount=len(newwordlist)
#    print (len(newwordlist)) 
    #print (newwordlist)

#    countwords="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    countlist =[]

    for i in countwords:
        countnumber=newwordlist.count(i)
#        print("counts is",countnumber,"of",i)
        
        
#        countlist.append(i)
        countlist.append(countnumber)


#    print(countlist)
#    totallettercount=sum(countlist)
#    print(totallettercount)

    #set(a) & set(b)
    return countlist,totalcharcount



def sorting_listoflist(liststore):
    pindexlist=[]
     
    for i in range(0,10):
        for j in range(0,len(countwords)):
            pindexlist.append(percentlist[i].index(liststore[i][j]))

#    for i in range(0,len(countwords)):
#        if pindexlist.count(i) > 1:
#            print (pindex(i))


    percentindexlistmain=[]
    for i in range(0,10):
        percentindexlistmain.append(pindexlist[0:26])
        pindexlist[0:26]=[]
        i=i+1
    #print(pindexlist)
    #print(percentindexlistmain)
    

    dpercentlist=[]

    for i in range(0,10):
        for j in percentindexlistmain[i]:
            dpercentlist.append(countwords[j])
    #print(dpercentlist)

    percentlistmain=[]
    for i in range(0,10):
        percentlistmain.append(dpercentlist[0:26])
        dpercentlist[0:26]=[]
        i=i+1
    return percentlistmain,percentindexlistmain

def filesave(name):
    
    file = open(name,"r", encoding="utf8")
        
    #Read lines all at once, lines contains all the values in list in certain format
    linesmain=file.read(linestoread)
    while '\ufeff' in linesmain:
        linesmain.strip('\ufeff')

    while '\n' in linesmain:
        linesmain.strip('\n')
    #Closing the file
    file.close()
    return linesmain


def biagramwordcount(linesmain,letters):
    file = open(name,"r", encoding="utf8")
        
    #Read lines all at once, lines contains all the values in list in certain format
    linesmain=file.read(linestoread)
    #while '\ufeff' in linesmain:
    #    linesmain.strip('\ufeff')

    #while '\n' in linesmain:
    #    linesmain.strip('\n')
    #Closing the file
    file.close()
    #return linesmain
    totalcharcount=linesmain.count(letters)
    #print(totalcharcount)
    return totalcharcount


#List containing all the file names
filelist = ["BrothersKaramazov-Dostoyevsky.txt","Copperfield-Dickens.txt","DonQuixote-Cervantes.txt","Hunchback-Hugo.txt","Various-Twain.txt","Middlemarch-Eliot.txt","Moby-Melville.txt","MonteCristo-Dumas.txt","Ulysses-Joyce.txt","WarPeace-Tolstoy.txt"]

#Starting to read file
#file = open(filename, "r")

reportlist=[]
charcountlist=[]
for name in filelist:

    countlist,charcount=wordcount(name)
    reportlist.append(countlist)
    charcountlist.append(charcount)
#print(reportlist)
#print(charcountlist)

percentlist=[]
#print(sum(reportlist[9]))
for i in range(0,len(reportlist)):
    percent=to_percent(reportlist[i],charcountlist[i])
    percentlist.append(percent)


#print(percentlist)

webpercentlist=[8.04,1.48,3.34,3.82,12.49,2.40,1.87,5.05,7.57,0.16,0.54,4.07,2.51,7.53,7.64,2.14,0.12,6.28,6.51,9.28,2.73,1.05,1.68,0.23,1.66,0.09]

diffpercentlist=[]

differencelist=diff_percent(percentlist,webpercentlist)

difflist=[]
for i in range(0,10):
    difflist.append(differencelist[0:26])
    differencelist[0:26]=[]
    i=i+1

#print(len(difflist[1]))
#print(difflist)


ranklist=[]
for i in range(0,10):
    ranklist.append(sum(difflist[i]))


rankliststore=copy.deepcopy(ranklist)

ranklist.sort()

#print(ranklist)
#print(rankliststore)

indexlist=[]
for i in range(0,10):
    indexlist.append(rankliststore.index(ranklist[i]))

#print(indexlist)

rankbook=[]
print("The rank of books")

for i in indexlist:
    rankbook.append(filelist[i])
    print(filelist[i])


percentliststore=copy.deepcopy(percentlist)

#countwordsstore=copy.deepcopy(countwords)

for i in range(0,10):
    percentliststore[i].sort(reverse=True)

#print(percentliststore)
#print(percentlist)

desc_sorted_list,descindexlist=sorting_listoflist(percentliststore)

#print("The Descending percentage list",desc_sorted_list)


#from most frequent to least frequent
ascpercentliststore=copy.deepcopy(percentlist)

for i in range(0,10):
    ascpercentliststore[i].sort()

#print(ascpercentliststore)
asc_sorted_list,ascindexlist=sorting_listoflist(ascpercentliststore)

#print("The Ascending percentage list",asc_sorted_list)

for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for j in range(0,len(countwords)):
        
        #print("The count of",countwords[j],"is",reportlist[i][j])
        print("The difference in percentage of web and calculated of ",countwords[j],"is",str(difflist[i][j]))
        #print("The percentage of ",countwords[j],"is",percentlist[i][j])
        #print("The descending percentage of ",desc_sorted_list[i][j],"is",percentliststore[i][j])
        #print("The ascending percentage of ",asc_sorted_list[i][j],"is",ascpercentliststore[i][j])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for j in range(0,len(countwords)):
        
        #print("The count of",countwords[j],"is",reportlist[i][j])
        #print("The difference in percentage of web and calculated of ",countwords[j],"is",str(difflist[i][j]))
        print("The percentage of ",countwords[j],"is",percentlist[i][j])
        #print("The descending percentage of ",desc_sorted_list[i][j],"is",percentliststore[i][j])
        #print("The ascending percentage of ",asc_sorted_list[i][j],"is",ascpercentliststore[i][j])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for j in range(0,len(countwords)):

        print("The descending percentage of ",desc_sorted_list[i][j],"is",percentliststore[i][j])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for j in range(0,len(countwords)):

        print("The ascending percentage of ",asc_sorted_list[i][j],"is",ascpercentliststore[i][j])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


webpercentliststoreasc=copy.deepcopy(webpercentlist)
webpercentliststoredesc=copy.deepcopy(webpercentlist)

webpercentliststoreasc.sort()
webpercentliststoredesc.sort(reverse=True)

webindexlistasc=[]
webindexlistdesc=[]
for i in range(0,len(countwords)):
    webindexlistasc.append(webpercentlist.index(webpercentliststoreasc[i]))
    webindexlistdesc.append(webpercentlist.index(webpercentliststoredesc[i]))

#print(webpercentliststoreasc)
#print(webindexlistasc)

letterasc=[]
letterdesc=[]

for i in webindexlistdesc:
    letterdesc.append(countwords[i])

for i in webindexlistasc:
    letterasc.append(countwords[i])

for i in range(0,len(countwords)):
    print("The ascending percentage of web ",letterasc[i],"is",webpercentliststoreasc[i])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0,len(countwords)):
    print("The descending percentage of web",letterdesc[i],"is",webpercentliststoredesc[i])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


#print(descindexlist)
#print(webindexlistdesc)
#print(ascindexlist)
#print(webindexlistasc)

listindexstorage=[]

for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for j in range(0,len(countwords)):
        #if "G"  not in asc_sorted_list[i]:
        #    continue
        #listindexstorage.append(asc_sorted_list[i].index(letterasc[j]))

        
        diffindex=webindexlistasc[j] - ascindexlist[i][j]
        listindexstorage.append(diffindex)
        print("The index difference between ",asc_sorted_list[i][j],"and",letterasc[j],"is",diffindex)

listindexstoragemain=[]
for i in range(0,10):
    listindexstoragemain.append(listindexstorage[0:26])
    listindexstorage[0:26]=[]
    i=i+1
    
#print(listindexstoragemain)

abslistindexstoragemain=copy.deepcopy(listindexstoragemain)
for i in range(0,len(filelist)):
    for j in range(0,len(countwords)):
        if abslistindexstoragemain[i][j] < 0:
            abslistindexstoragemain[i][j] =  - abslistindexstoragemain[i][j]
        else:
            abslistindexstoragemain[i][j] = abslistindexstoragemain[i][j]

#print(abslistindexstoragemain)

sumlistindex=[]

for i in range(0,10):
    sumlistindex.append(sum(abslistindexstoragemain[i]))

#print(sumlistindex)

sumlistindexstorage=copy.deepcopy(sumlistindex)

sumlistindexstorage.sort()


#print(sumlistindexstorage)

rankbookindexchange=[]
print("The rank of books for index change")

indexchangelist=[]
for i in range(0,10):
    if sumlistindex.count(sumlistindexstorage[i]) > 1:
        sumlistindex[i] = sumlistindex[i] - 0.1
    #if sumlistindex.index(sumlistindexstorage[i]) in indexchangelist:
    #    print("Already in list",sumlistindexstorage[i])
    #    print(sumlistindex)
    #    sumlistindex.remove(sumlistindexstorage[i])
    #    print(sumlistindex.index(sumlistindexstorage[i]))
    #    indexchangelist.append((sumlistindex.index(sumlistindexstorage[i])+1))
    #    print(indexchangelist)
    #    break
    #else:    
    indexchangelist.append(sumlistindex.index(sumlistindexstorage[i]))
    
#print(indexchangelist)
for i in indexchangelist:
    rankbookindexchange.append(filelist[i])
    print(filelist[i])


#bigrams

bigram=[]
for i in countwords:
    for j in countwords:
        save=i+j
        bigram.append(save)

#print(bigram)

#linestring=[]
biagcharcountlist=[]
#for name in filelist:
#    linemain=filesave(name)
#    linestring.append(linemain)

#print (linestring)   
for j in range(0,len(filelist)):
    #print(filelist[j])
   # print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for i in bigram:
        biagcharcount=biagramwordcount(filelist[j],i)
        #biagcharcount=biagramwordcount(linestring[j],i)
        #print("The count of ",i,"is",biagcharcount)
        biagcharcountlist.append(biagcharcount)

biagcharcountlistmain=[]
for i in range(0,10):
    biagcharcountlistmain.append(biagcharcountlist[0:len(bigram)])
    biagcharcountlist[0:len(bigram)]=[]
    i=i+1
#print(biagcharcountlistmain)
#print(len(biagcharcountlistmain)
biagcharcountlistmainstore=copy.deepcopy(biagcharcountlistmain)

biagcharcountlistmain1=[]
for i in range(0,10):
    for j in range(0,26):
        biagcharcountlistmain1.append(biagcharcountlistmain[i][0:len(countwords)])
        biagcharcountlistmain[i][0:len(countwords)]=[]
        j=j+1
    i=i+1
#print(biagcharcountlistmain1)
#print(len(biagcharcountlistmain1))
#print(len(biagcharcountlistmain1[0]))
    
for i in range(0,len(filelist)):
    print(filelist[i])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    #for j in range(0,len(bigram)):
    #    print(bigram[j],"=",biagcharcountlistmain1[i][j],end=' ')

    for j in range(0,len(countwords)):
        print('  '+ countwords[j],end=' ')
    print("    ")
    
    for k in range(0,len(countwords)):
        print(countwords[k] ,end=' ')
        for n in range(0,len(countwords)):
            print(biagcharcountlistmain1[k][n],end='   ')
        print("    ")


biagcharcountlistmainstore1=copy.deepcopy(biagcharcountlistmainstore)

#print(biagcharcountlistmainstore1)

for i in range(0,10):
    biagcharcountlistmainstore[i].sort(reverse=True)

storetoplist=[]
for i in range(0,10):
    storetoplist.append(biagcharcountlistmainstore[i][0:10])

print(storetoplist)

maintoplist=[]
for i in range(0,10):
    for j in range(0,10):
        maintoplist.append(biagcharcountlistmainstore1[i].index(biagcharcountlistmainstore[i][j]))
        
                   
#print(maintoplist)

top=[]
for i in range(0,10):
    top.append(maintoplist[0:10])
    maintoplist[0:10]=[]
    i=i+1 
#print(maintoplist)

for j in range(0,len(filelist)):
    print(filelist[j])
    print("#########################~~~~~~~~~~~~~~~~~~~~~~~~~~########################")
    
    for value in top[j]:
        print(bigram[value])
