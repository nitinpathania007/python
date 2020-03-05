# Input base to Output base Converter

inbase = input("Please enter the input base (2-16): ")

while not (((len(inbase) == 1) and (inbase[0] in "23456789")) or ((len(inbase) == 2) and (inbase[0] == "1") and (inbase[1] in "0123456"))) :
    inbase = input("Value must be in range 2-16. Try again: ")

outbase = input("Please enter the output base (2-16): ")

while not (((len(outbase) == 1) and (outbase[0] in "23456789")) or ((len(outbase) == 2) and (outbase[0] == "1") and (outbase[1] in "0123456"))) :
    outbase = input("Value must be in range 2-16. Try again: ")

invalue = input("Please enter the input value to convert: ")

digits = "0123456789ABCDEF"
bad = True

while bad :

    for c in invalue :
        if not (c in digits[0:int(inbase)]) :
            invalue = input("Input error, please enter a value in the proper base: ")
            break
        else :
            bad = False

sum = 0
n = len(invalue)
weight = int(int(inbase) ** (n-1))

for c in invalue :
    if c in "123456789" :
        sum += int(c) * weight        
    elif c in "ABCDEF":
        sum += (ord(c)-55) * weight        

    weight = weight // int(inbase) 

quotient = sum
output = ""
    
while quotient != 0 :
    remainder = quotient % int(outbase)
    if remainder < 10 :
        outrem = chr(48+remainder)
    else:
        outrem = chr(55+remainder)
    quotient = quotient // int(outbase)
    output = outrem + output
    
print("The equivalent of %s is %s" % (invalue,output))
