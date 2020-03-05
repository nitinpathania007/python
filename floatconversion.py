
def valid (inputnumber) :
    if not inputnumber[0] in "+-0123456789" :
        return False
    else :
        periodcount = 0

        for c in inputnumber[1:-1] :
            if not c in ".0123456789" :
                return False
            elif c == "." :
                periodcount += 1

        if periodcount != 1 :
            return False
        elif not inputnumber[-1] in "0123456789" :
            return False
        elif inputnumber[1] == "." and inputnumber[0] in "+-" :
            return False
        else :
            return True

def periodindex (inputnumber) :
    pindex = 1

    while inputnumber[pindex] != "." :
        pindex += 1

    return pindex

def extractparts (inputnumber) :
    pi = periodindex(inputnumber)

    if inputnumber[0] in "+-" :
        intpart = inputnumber[1:pi]
    else :
        intpart = inputnumber[:pi] 

    fracpart = inputnumber[pi+1:]

    return (intpart,fracpart)

def inttobinary (intvalue) :

    quotient = int(intvalue)
    output = ""
    
    while quotient != 0 :
        remainder = quotient % 2
        if remainder == 0 :
            outrem = "0"
        else:
            outrem = "1"
        quotient = quotient // 2
        output = outrem + output

    return output

def fractobinary (fracvalue) :

    if fracvalue == "0" :
        return "00000000000000000000000"

    fraction = float("0."+fracvalue)
    output = ""
    count = 24
    onenotfound = True

    while (onenotfound == True) or ((onenotfound == False) and (count > 0)) :
        product = fraction * 2
        if product >= 1 :
            output = output + "1"
            fraction = product - 1
            onenotfound = False
        else :
            fraction = product
            output = output + "0"

        if onenotfound == False :
            count -= 1

    return output

def findaone (bits) :

    bindex = 0

    while bits[bindex] != "1" :
        bindex += 1

    return bindex

def getsignbit (firstchar) :
    if firstchar == "-" :
        return "1"
    else :
        return "0"

def getexpobits (intbits, fracbits) :
    if len(intbits) >= 1 :
        expo = len(intbits) - 1
    else :
        onepos = findaone(fracbits)
        expo = -(onepos + 1)

    expo += 127
    expobits = inttobinary(expo)
    expobits = "0" * (8 - len(expobits)) + expobits

    return expobits

def getmantissabits (intbits, fracbits) :
    if intbits == "" :
        onepos = findaone(fracbits)
        mantissabits = fracbits[onepos+1:onepos+24]
    else :
        catbits = intbits + fracbits
        mantissabits = catbits[1:24]

    return mantissabits



fp = input("Please enter a floating point value to convert: ")

while not valid(fp) :
    fp = input("Error in floating point format. Please try again: ")

intpart, fracpart = extractparts(fp)

intbits = inttobinary(intpart)

fracbits = fractobinary(fracpart)

expobits = getexpobits(intbits,fracbits)

mantissabits = getmantissabits(intbits,fracbits)

signbit = getsignbit(fp[0])

answer = signbit + " " + expobits + " " + mantissabits

print(fp, "is equivalent to", answer)
