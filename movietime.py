#Created by Nitin Pathania


#Printing out best movies across two databases that have a user specified genre and ratings

#Importing sys
import sys


#first file imdb.txt open and split it by space.
file1 = open("imdb.txt", "r")

imdblist=[]

for line in file1 :

    word=line.split()
    #add the splitted words to a list called imdblist making list of list.
    imdblist.append(word)

#close the file  
file1.close()   

len1=len(imdblist)

#first file movielens.txt open and split it by comma.
file2 = open("movielens.txt", "r")
 
movielenslist=[]

for line in file2 :

    word1=line.split(",")
    #add the splitted words to a list called movielenslist making list of list.
    movielenslist.append(word1)
           
#close the file  
file2.close()

len2=len(movielenslist)

#Adding all values present in both files in one dictionary. Both files are checked for movie id if it present in both
#The imdb value is mulplied by 2 and then average of imdb and other rating is taken to find combined movie ratings, which is added in dictionary as a value with other information.
maindict={}
for i in range(0, len1):
    for j in range(0, len2):
        if imdblist[i][1]==str(movielenslist[j][1]):
            #print(imdblist[i][1])
            #print(movielenslist[j][1])
            dictadd=[movielenslist[j][0],imdblist[i][0],(float(movielenslist[j][2])+(float(imdblist[i][2])*2))/2]
            maindict[movielenslist[j][1]]=dictadd
         
#print (maindict)

dictlen=len(maindict)

#variables containing all types of genres and movierating present
genre=["comedy","action","romance"]
movierating=["G","PG","R"]


dict1={}

#dict1 contains all the data with key as combined ratings with provided genre and movie rating in command line.
if (sys.argv[1] in genre) and (sys.argv[2] in movierating):
    for k,v in maindict.items():
        if (v[0]==sys.argv[1]) and (v[1]==sys.argv[2]):
            rating=v[2]
            v.remove(v[2])
            v.append(k)
            dict1[rating]=v
    #print(dict1)
    #print(len(dict1))
else:
    #If wrong input is typed this will throw error and quit the program.
    print("You have entered an incorrect input!")
    sys.exit()
main=list(dict1)
#main contains dict1 keys and sort it in descending order
main.sort(reverse=True)
#print(main)


#dict2 will contain all values for combined rating according to descending order in a dictionary.
dict2={}

for i in main:
    dict2[i]=dict1[i]

#print(len(dict1))
#print(len(dict2))
#print(dict2)


#proper formatting of value according to length is taken care of for beautiful table view.
print("Movie ID    Combined Movie Ratings")
for k,v in dict2.items():
    if len(v[2])==2:
        print(v[2],end="           ")
        print(k)
    elif len(v[2])==1:
        print(v[2],end="            ")
        print(k)
    else:
        print(v[2],end="          ")
        print(k)
#print(dictlen)
