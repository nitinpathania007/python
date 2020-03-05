#List containing all the file names
filelist = ["BrothersKaramazov-Dostoyevsky.txt","Copperfield-Dickens.txt","DonQuixote-Cervantes.txt","Hunchback-Hugo.txt","Various-Twain.txt","Middlemarch-Eliot.txt","Moby-Melville.txt","MonteCristo-Dumas.txt","Ulysses-Joyce.txt","WarPeace-Tolstoy.txt"]

for name in filelist:

    bookname = name
#    bookname = input("Please enter name of book: ")
    book = open(bookname, "r", encoding="utf8")
    #Read lines all at once, lines contains all the values in list in certain format
    while '\ufeff' in book:
        book.strip('\ufeff')

    while '\n' in book:
        book.strip('\n')
        
    linenum = 1
    indexdict = {}

    for line in book :
        for word in line.split() :    
            realword = word.strip("'\".,!?#:;@$~")
            lowerword = word.lower()
            
            if lowerword in indexdict :
                if not linenum in indexdict[lowerword] :
                    indexdict[lowerword].append(linenum)
            else :
               indexdict[lowerword] = [linenum]

        linenum += 1

    book.close()

    print(indexdict)

