# Created by Nitin Pathania
#Data analysis of 10 books for work count


def to_upper(oldList):
    newList = []
    for element in oldList:
        newList.append(element.upper())
    return newList

def to_percent(oldList):
    newList = []
    for element in oldList:
        newList.append(element.upper())
    return newList


#List containing all the file names
filelist = ["BrothersKaramazov-Dostoyevsky.txt","Copperfield-Dickens.txt","DonQuixote-Cervantes.txt","Hunchback-Hugo.txt","Various-Twain.txt","Middlemarch-Eliot.txt","Moby-Melville.txt","MonteCristo-Dumas.txt","Ulysses-Joyce.txt","WarPeace-Tolstoy.txt"]


filename = "BrothersKaramazov-Dostoyevsky.txt"
#Starting to read file
#file = open(filename, "r")

wordlist=[]
#lines = [line.rstrip('\n') for line in open('filename')]
for name in filelist:
    file = open(name,"r", encoding="utf8")
    
    #Read lines all at once, lines contains all the values in list in certain format
    linesmain=file.read(20000)
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
print (len(newwordlist)) 
#print (newwordlist)

countwords="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

countlist =[]

for i in countwords:
    countnumber=newwordlist.count(i)
    print("counts is",countnumber,"of",i)
    
    
#    countlist.append(i)
    countlist.append(countnumber)


print(countlist)
totallettercount=sum(countlist)
print(totallettercount)

#set(a) & set(b)

     
