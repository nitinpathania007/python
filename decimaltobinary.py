# Decimal to binary  converter

decimal=input("Please enter the decimal value to convert:")

bad= True

while bad :
    for c in decimal:
# if not (c in "0123456789") :
        index=ord(c)
        if (index < 48) or (index >57) :
            decimal=input("Input error!!Please enter the decimal value to convert:")
            break
    else:
        bad = False

decimal=int(decimal)

quotient = decimal

output = ""

while quotient != 0 :
    remainder = quotient % 2
    outrem = chr(48+remainder)
    quotient = quotient // 2
    output=outrem + output
    
#integer portion of quotient 

print("The binary equivalent of %d is %s" % (decimal,output))


      
