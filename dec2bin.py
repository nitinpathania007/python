# Decimal to Binary Converter

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

