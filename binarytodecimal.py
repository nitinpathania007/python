#Binary to Decimal converter
# Decimal to binary converter
convert=input("Do you want to convery from binary to decimal(Y) or binary to decimal(N)?")

if (convert == "Y") or (convert == "y"):

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

elif (convert == "N") or (convert == "n"):
    binary=input("Please enter the binary value to convert:")
    bad= True
#   for i in convert[0:]:
        
    while bad :
        for c in binary:
            
    # if not (c in "0123456789") :
            index=ord(c)
            #if not (c in "01"):
            # if ((c !="1") and (c!="0"))
            # if  not((c =="1") or (c=="0"))
            if (index < 48) or (index >49) :
                decimal=input("Input error!!Please enter the decimal value to convert:")
                break
        else:
            bad = False
    n = len(binary)
    weight = 2 ** (n-1)
    
    sum=0
    for c in binary:
        if c == "1":
            sum = sum + weight
#           sum += weight
        weight = weight/2
    print("The decimal equivalent of %s is %d" % (binary,sum)) 
else:
    print("You are an idiot")
      
