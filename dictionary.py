#Create a index for a list
bookname=input("Please enter name of book:")

book=open(bookname, "r", encoding="utf8")
linenum=1

indexdict={}

for line in book:
    for word in line.split():
        realword = word.strip("'\".,!#;:@?$%^&*()_-+=")
        lowerword = word.lower()

        if lowerword in indexdict:
            if not linenum in indexdict[lowerword]:
                indexdict[lowerword].append(linenum)
            indexdict[lowerword] = [linenum]
        else:
            indexdict[lowerword] = [linenum]
    linenum += 1

book.close()

print( indexdict['war'])


    
    
    
