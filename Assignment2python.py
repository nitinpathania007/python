#Created by Nitin Pathania

#Data Transmission

#adding a valid function to check whether the input is valid
def valid(string):   
    for i in string:       
        if not(i in "abcdefghijklmnpqrstwxyz"):
            return False
        elif len(string)>2:
            return False
        else:
            return True

#find function will be used to find the zero and one bits counts in any binary string. ch can be 0 or 1
def find(strng, ch):
    index = 0
    countone = ""
    countzero = ""
    while index < len(strng):
        if strng[index] == ch:
            index=str(index)
            countone += index
            index=int(index)
            index += 1
        else:
            index=str(index)
            countzero += index
            index=int(index)
            index += 1
    return countzero,countone

#Th
def findcount(count,countone):
    ccount=0
    for i in count:
        if i in countone:
            ccount += 1
    if (ccount%2) == 1:
        value=1
    else:
        value=0
    return value

def stringtoascii(string):
    convstring=""
    for i in string:
        if ord(i) < 100:
            convstring += "0" + str(ord(i)) + " "
        else:
            convstring += str(ord(i)) + " "
    return convstring

def stringtoasciireturn(string):
    convstring=""
    for i in string:
        convstring += str(ord(i))
    return convstring

def inttobinary (intvalue) :

    quotient = int(intvalue)
    #output is set to o as first bit is always zero for characters with ascii characters.
    output = ""
    
    while quotient != 0 :
        remainder = quotient % 2
        if remainder == 0 :
            outrem = "0"
        else:
            outrem = "1"
        quotient = quotient // 2
        output = outrem + output
    #output is concatenated by first charcater zero as first bit is always zero for characters with ascii characters.
    if len(output) == 7:
        output= "0" + output
    elif len(output) == 6:
        output= "00" + output
    elif len(output) == 5:
        output= "000" + output
    elif len(output) == 4:
        output= "0000" + output
    elif len(output) == 3:
        output= "00000" + output
    elif len(output) == 2:
        output= "000000" + output
    elif len(output) == 1:
        output= "0000000" + output
    else:
        output = output
    return output

def asciitostring(integer):
    charout=chr(integer)
    return charout

def binary12bit(bi,c1,c2,c4,c8):
    binary12bit=str(c1) + str(c2) + bi[0] + str(c4) + bi[1] + bi[2] + bi[3] + str(c8) + bi[4] + bi[5] + bi[6] + bi[7]
    return binary12bit


def binary8bit(b112):
    binary8bit=b112[2]+b112[4]+b112[5]+b112[6]+b112[8]+b112[9]+b112[10]+b112[11]
    return binary8bit


def binarytodec(binary):
    n = len(binary)
    weight = 2 ** (n-1)
    sum=0
    for c in binary:
        if c == "1":
            sum = sum + weight
#           sum += weight
        weight = weight/2
    sum=int(sum)
    return sum

def noise(integer1,integer2):
    integer1=int(integer1)
    integer1=int(integer2)
    addnoise = integer1 | integer2
    return addnoise

def paritycheck(c1,newc1,add):
    sum=0
    if c1!=newc1:
        sum+=add
    else:
        sum=sum
    return sum

def noisechange(string,index):
    if not(index == 0):
        
            string[index]=="1"
        

inputstring = input("Enter the string you want to transmit:")

length=len(inputstring)

#while not valid(inputstring) :
#    inputstring = input("Error! Enter lower case string from a to z you want to transmit:")
if (length)% 2 == 1:
    inputstring = inputstring + " "

def twocharacter(twochar):
    print("i")
convstring=stringtoascii(inputstring)

convstringlist=convstring.split()

binary1=inttobinary(convstringlist[0])
binary2=inttobinary(convstringlist[1])
#print(binary1)
#print(binary2)

countzero1,countone1 = find(binary1,"1")
countzero2,countone2 = find(binary2,"1")

c1="01346"
c2="02356"
c4="1237"
c8="4567"

c1value1=findcount(c1,countone1)
#print(c1value1)
c2value1=findcount(c2,countone1)
#print(c2value1)
c4value1=findcount(c4,countone1)
#print(c4value1)
c8value1=findcount(c8,countone1)
#print(c8value1)
c1value2=findcount(c1,countone2)
#print(c1value2)
c2value2=findcount(c2,countone2)
#print(c2value2)
c4value2=findcount(c4,countone2)
#print(c4value2)
c8value2=findcount(c8,countone2)
#print(c8value2)

binary12bit1 = binary12bit(binary1, c1value1, c2value1, c4value1, c8value1)
binary12bit2 = binary12bit(binary2, c1value2, c2value2, c4value2, c8value2)

#print(binary12bit1)
#print(binary12bit2)

fullbinary = binary12bit1 + binary12bit2


fullbinary1=fullbinary[0:8]
fullbinary2=fullbinary[8:16]
fullbinary3=fullbinary[16:24]
#print(fullbinary1)
#print(fullbinary2)
#print(fullbinary3)

dec1=binarytodec(fullbinary1)
dec2=binarytodec(fullbinary2)
dec3=binarytodec(fullbinary3)
print(dec1)
print(dec2)
print(dec3)

#noise1=noise(dec1,dec3)
#print (noise1)


stringreturn1=asciitostring(dec1)
stringreturn2=asciitostring(dec2)
stringreturn3=asciitostring(dec3)
#print(stringreturn1)
#print(stringreturn2)
#print(stringreturn3)

#adding noise
for i in range(0,8):
    noise=(2**i)
    noisebin=inttobinary(noise)
#    print(noisebin)
    noise1=dec1 | noise
    print(noise1)
    noise2= dec2 | noise
    noise3=dec3 | noise
    
    print(noise2)
    print(noise3)
    stringnoise1=asciitostring(noise1)
    stringnoise2=asciitostring(noise2)
    stringnoise3=asciitostring(noise3)
#    print(stringnoise1)
#    print(stringnoise2)
#    print(stringnoise3)


noise=1
noisebin=inttobinary(noise)
#print(noisebin)
noise1=dec1 | noise
print(noise1)
noise2= dec2 | noise
noise3=dec3 | noise
    
print(noise2)
print(noise3)
stringnoise1=asciitostring(noise1)
stringnoise2=asciitostring(noise2)
stringnoise3=asciitostring(noise3)
print(stringnoise1)
print(stringnoise2)
print(stringnoise3)

#convert back string to binary

convdec1=stringtoasciireturn(stringreturn1)
convdec2=stringtoasciireturn(stringreturn2)
convdec3=stringtoasciireturn(stringreturn3)

convnoise1=stringtoasciireturn(stringnoise1)
convnoise2=stringtoasciireturn(stringnoise2)
convnoise3=stringtoasciireturn(stringnoise3)
#print(convdec1)
#print(convdec2)
#print(convdec3)

print(convnoise1)
print(convnoise2)
print(convnoise3)

backconvbinary1=inttobinary(convdec1)
backconvbinary2=inttobinary(convdec2)
backconvbinary3=inttobinary(convdec3)

backconnoise1=inttobinary(convnoise1)
backconnoise2=inttobinary(convnoise2)
backconnoise3=inttobinary(convnoise3)
#print(backconvbinary1)
#print(backconvbinary2)
#print(backconvbinary3)

#print(backconnoise1)
#print(backconnoise2)
#print(backconnoise3)

backfullbinary = backconvbinary1 + backconvbinary2 + backconvbinary3

backfullbinarynoise = backconnoise1 + backconnoise2 + backconnoise3

backbinary1=backfullbinary[0:12]
backbinary2=backfullbinary[12:24]

backbinarynoise1=backfullbinarynoise[0:12]
backbinarynoise2=backfullbinarynoise[12:24]
print (backbinary1)
print (backbinary2)

print(backbinarynoise1)
print(backbinarynoise2)




binary8bitmain1=binary8bit(backbinary1)
binary8bitmain2=binary8bit(backbinary2)
print(binary8bitmain1)
print(binary8bitmain2)

binary8bitmainnoise1=binary8bit(backbinarynoise1)
binary8bitmainnoise2=binary8bit(backbinarynoise2)
print(binary8bitmainnoise1)
print(binary8bitmainnoise2)

backdec1=binarytodec(binary8bitmain1)
backdec2=binarytodec(binary8bitmain2)
#print(backdec1)
#print(backdec2)

backdecnoise1=binarytodec(binary8bitmainnoise1)
backdecnoise2=binarytodec(binary8bitmainnoise2)
#print(backdecnoise1)
#print(backdecnoise2)

backchar1=asciitostring(backdec1)
backchar2=asciitostring(backdec2)

#print(backchar1)
#print(backchar2)

backcharnoise1=asciitostring(backdecnoise1)
backcharnoise2=asciitostring(backdecnoise2)

#print(backcharnoise1)
#print(backcharnoise2)

fullbackchar=backchar1+backchar2

fullbackcharnoise=backcharnoise1+backcharnoise2

#Converting to 12 bit
countzeronoise1,countonenoise1 = find(binary8bitmainnoise1,"1")
countzeronoise2,countonenoise2 = find(binary8bitmainnoise2,"1")

c1valuenoise1=findcount(c1,countonenoise1)
print(c1valuenoise1)
c2valuenoise1=findcount(c2,countonenoise1)
print(c2valuenoise1)
c4valuenoise1=findcount(c4,countonenoise1)
print(c4valuenoise1)
c8valuenoise1=findcount(c8,countonenoise1)
print(c8valuenoise1)
c1valuenoise2=findcount(c1,countonenoise1)
print(c1valuenoise2)
c2valuenoise2=findcount(c2,countonenoise1)
print(c2valuenoise2)
c4valuenoise2=findcount(c4,countonenoise1)
print(c4valuenoise2)
c8valuenoise2=findcount(c8,countonenoise1)
print(c8valuenoise2)

binary12bitnoise1 = binary12bit(binary8bitmainnoise1, c1valuenoise1, c2valuenoise1, c4valuenoise1, c8valuenoise1)
binary12bitnoise2 = binary12bit(binary8bitmainnoise2, c1valuenoise2, c2valuenoise2, c4valuenoise2, c8valuenoise2)

print(binary12bitnoise1)
print(binary12bitnoise2)

p1=paritycheck(str(c1value1),(binary12bitnoise1[0]),1)
p2=paritycheck(str(c2value1),(binary12bitnoise1[1]),2)
p3=paritycheck(str(c4value1),(binary12bitnoise1[3]),4)
p4=paritycheck(str(c8value1),(binary12bitnoise1[7]),8)

p5=paritycheck(str(c1value2),(binary12bitnoise2[0]),1)
p6=paritycheck(str(c2value2),(binary12bitnoise2[1]),2)
p7=paritycheck(str(c4value2),(binary12bitnoise2[3]),4)
p8=paritycheck(str(c8value2),(binary12bitnoise2[7]),8)
print (p1)
print (p2)
print (p3)
print (p4)
print (p5)
print (p6)
print (p7)
print (p8)

if p1!="0" or p2!="0" or p3!="0" or p4!="0" or p5!="0" or p6!="0" or p7!="0" or p8!="0":
    binary12bitnoise1
print(str(c1value1) == backbinary1[0])

print(str(c2value1) == backbinary1[1])

print(str(c4value1)==backbinary1[3])

print(str(c8value1)==backbinary1[7])

print(str(c1value2)==backbinary2[0])
  
print(str(c2value2)==backbinary2[1])

print(str(c4value2)==backbinary2[3])

print(str(c8value2)==backbinary2[7])

#p1=paritycheck(str(c1value1),(backbinary1[0]),1)
#p2=paritycheck(str(c2value1),(backbinary1[1]),2)
#p3=paritycheck(str(c4value1),(backbinary1[3]),4)
#p4=paritycheck(str(c8value1),(backbinary1[7]),8)

#p5=paritycheck(str(c1value2),(backbinary2[0]),1)
#p6=paritycheck(str(c2value2),(backbinary2[1]),2)
#p7=paritycheck(str(c4value2),(backbinary2[3]),4)
#p8=paritycheck(str(c8value2),(backbinary2[7]),8)
#print (p2)
#print (p3)
#print (p4)
#print (p5)
if str(c1value1) == backbinary1[0]:
    print ("y1")

elif str(c2value1) == backbinary1[1]:
    print ("y2")

elif str(c4value1)==backbinary1[3]:
    print ("y3")

elif str(c8value1)==backbinary1[7]:
    print ("y4")

elif str(c1value2)==backbinary2[0]:
    print ("y5")
  
elif str(c2value2)==backbinary2[1]:
    print ("y6")

elif str(c4value2)==backbinary2[3]:
    print ("y7")

elif str(c8value2)==backbinary2[7]:
    print ("y8")
fullbackcharnoise


print("Original message : ",inputstring)
print("Transmitted string : ", stringreturn1+stringreturn2+stringreturn3)
print("Received noisy message : ",stringnoise1+stringnoise2+stringnoise3)
print("Final Converted message:",fullbackchar)

print("Noise Converted message:",fullbackcharnoise)


