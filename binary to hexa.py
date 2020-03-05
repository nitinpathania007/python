#input base to outpute base converter

inbase=input("Please enter the input base *2-16):")
while not (((len (inbase) ==1 ) and (inbase[0] in "23456789") or (len (inbase==2) and (inbase[0] == "1") and (inbase[1] in "0123456")))):
    outbase = input("value must be in range 2-16.Try again:")

invalue = input(" Please enter the input value to convert:")

digits="0123456789ABCDEF"
bad = True

while bad :

    for c in decimal :
        if not ( c in digits [0:inbase]) :
            invalue =input("input error, please enter a value in a proper base
    
