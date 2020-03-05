# Decimal to Binary Converter

convert = input("Do you want to convert from decimal to binary (Y) or binary to decimal (N)?")

if (convert == "Y") or (convert == "y") :

    decimal = input("Please enter the decimal value to convert: ")

    bad = True

    while bad :

        for c in decimal :
            ind = ord(c)
    # if not (c in "0123456789") :
            if (ind < 48) or (ind > 57) :
                decimal = input("Input error, please enter a decimal value: ")
                break
        else :
            bad = False


    decimal = int(decimal)

    quotient = decimal
    output = ""
    
    while quotient != 0 :
        remainder = quotient % 2
        outrem = chr(48+remainder)
        quotient = quotient // 2
        output = outrem + output
    
    print("The binary equivalent of %d is %s" % (decimal,output))
elif (convert == "N") or (convert == "n") :

    binary = input("Please enter the binary value to convert: ")

    bad = True

    while bad :

        for c in binary :
            ind = ord(c)
    	    # if not (c in "01") :
            # if (c != "1") and (c != "0") :
            # if not ((c == "1") or (c == "0")) :
            if (ind < 48) or (ind > 49) :
                binary = input("Input error, please enter a binary value: ")
                break
        else :
            bad = False

    n = len(binary)
    weight = 2 ** (n-1) 
    sum = 0

    for c in binary :
        if c == "1" :
            sum += weight        
        weight = weight / 2

    print("The decimal equivalent of %s is %d" % (binary,sum))
else:
    print("You are an idiot.")

