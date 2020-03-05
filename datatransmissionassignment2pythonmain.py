#Created by Nitin Pathania

#Data Transmission
#Creating a variable with name calculateagain with value to True to run the program again if need to calculate again. 
transmitagain= True
#Starting calculateagain loop till calculateagain variable value is True , this will keep on running.
while transmitagain :
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

    #find count function is the counting the number of zero and one's and returning the counts back
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
    #This function converts string to its ascii number
    def stringtoascii(string):
        convstring=""
        for i in string:
            if ord(i) < 100:
                convstring += "0" + str(ord(i)) + " "
            else:
                convstring += str(ord(i)) + " "
        return convstring
    #This function converts string  to its ascii while getting back to it
    def stringtoasciireturn(string):
        convstring=""
        for i in string:
            convstring += str(ord(i))
        return convstring
    #This function converts integer to 12 bit binary
    def inttobinary12bit (intvalue) :

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
        elif len(output) == 8:
            output= "0000" + output
        elif len(output) == 9:
            output= "000" + output
        elif len(output) == 10:
            output= "00" + output
        elif len(output) == 11:
            output= "0" + output
        else:
            output = output
        return output
    #this function is used to convert integer to 8-bit binary
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
        elif len(output) == 8:
            output= output
        elif len(output) == 9:
            output= "000" + output
        elif len(output) == 10:
            output= "00" + output
        elif len(output) == 11:
            output= "0" + output
        else:
            output = output
        return output
    #This function is used to convert ascii to string
    def asciitostring(integer):
        charout=chr(integer)
        return charout
    #This function is sued to get 12 bit value from 8 bit
    def binary12bit(bi,c1,c2,c4,c8):
        binary12bit=str(c1) + str(c2) + bi[0] + str(c4) + bi[1] + bi[2] + bi[3] + str(c8) + bi[4] + bi[5] + bi[6] + bi[7]
        return binary12bit

    #This function is used to convert 12 bit value to 8 bit value
    def binary8bit(b112):
        binary8bit=b112[2]+b112[4]+b112[5]+b112[6]+b112[8]+b112[9]+b112[10]+b112[11]
        return binary8bit

    #This function is used to convert binary to decimal
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
    #This function is used to add noise 
    def noise(integer1,integer2):
        integer1=int(integer1)
        integer1=int(integer2)
        addnoise = integer1 | integer2
        return addnoise
    #This function is used to check if c1 old is equal to c1 new after noise addition.
    def paritycheck(c1,newc1,add):
        sum=0
        if c1!=newc1:
            sum+=add
        else:
            sum=sum
        return sum
    #this function is used to get noise out
    def noisechange(string,index):
        index=int(index)
        if not(index == 0):
            if string[index]=="0":
                value="1"
                #noisecore=2**index
            elif string[index]=="1":
                value="0"
        else:
            value="0"
            
        return value
            
            

    #this function take 2 character string input and return the transmitted string after adding noise and again changing to character.
    def twocharacter(inputstring):

        convstring=stringtoascii(inputstring)
    #    convstring2=stringtoascii(inputstring[1])

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
        #print(dec1)
        #print(dec2)
        #print(dec3)

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
            #print(noise1)
            noise2= dec2 | noise
            noise3=dec3 | noise
            
            #print(noise2)
            #print(noise3)
            stringnoise1=asciitostring(noise1)
            stringnoise2=asciitostring(noise2)
            stringnoise3=asciitostring(noise3)
            #print(stringnoise1)
            #print(stringnoise2)
            #print(stringnoise3)


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

        #print(convnoise1)
        #print(convnoise2)
        #print(convnoise3)

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
        #print (backbinary1)
        #print (backbinary2)

        #print(backbinarynoise1)
        #print(backbinarynoise2)

        backdecmain1=binarytodec(backbinary1)
        backdecmain2=binarytodec(backbinary2)
        #print(backdecmain1)
        #print(backdecmain2)

        binary8bitmain1=binary8bit(backbinary1)
        binary8bitmain2=binary8bit(backbinary2)
        #print(binary8bitmain1)
        #print(binary8bitmain2)

        binary8bitmainnoise1=binary8bit(backbinarynoise1)
        binary8bitmainnoise2=binary8bit(backbinarynoise2)
        #print(binary8bitmainnoise1)
        #print(binary8bitmainnoise2)

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
        #print(c1valuenoise1)
        c2valuenoise1=findcount(c2,countonenoise1)
        #print(c2valuenoise1)
        c4valuenoise1=findcount(c4,countonenoise1)
        #print(c4valuenoise1)
        c8valuenoise1=findcount(c8,countonenoise1)
        #print(c8valuenoise1)
        c1valuenoise2=findcount(c1,countonenoise1)
        #print(c1valuenoise2)
        c2valuenoise2=findcount(c2,countonenoise1)
        #print(c2valuenoise2)
        c4valuenoise2=findcount(c4,countonenoise1)
        #print(c4valuenoise2)
        c8valuenoise2=findcount(c8,countonenoise1)
        #print(c8valuenoise2)

        binary12bitnoise1 = binary12bit(binary8bitmainnoise1, c1valuenoise1, c2valuenoise1, c4valuenoise1, c8valuenoise1)
        binary12bitnoise2 = binary12bit(binary8bitmainnoise2, c1valuenoise2, c2valuenoise2, c4valuenoise2, c8valuenoise2)

        #print(binary12bitnoise1)
        #print(binary12bitnoise2)
        
        backdecnoise1211=binarytodec(binary12bitnoise1)
        backdecnoise1221=binarytodec(binary12bitnoise2)
        #print(backdecnoise1211)
        #print(backdecnoise1221)
    
        p1=paritycheck((backbinary1[0]),(binary12bitnoise1[0]),1)
        p2=paritycheck((backbinary1[1]),(binary12bitnoise1[1]),2)
        p3=paritycheck((backbinary1[3]),(binary12bitnoise1[3]),4)
        p4=paritycheck((backbinary1[7]),(binary12bitnoise1[7]),8)

        p5=paritycheck((backbinary2[0]),(binary12bitnoise2[0]),1)
        p6=paritycheck((backbinary2[1]),(binary12bitnoise2[1]),2)
        p7=paritycheck((backbinary2[3]),(binary12bitnoise2[3]),4)
        p8=paritycheck((backbinary2[7]),(binary12bitnoise2[7]),8)

        #print (p1)
        #print (p2)
        #print (p3)
        #print (p4)
        #print (p5)
        #print (p6)
        #print (p7)
        #print (p8)

        if p1!="0" or p2!="0" or p3!="0" or p4!="0" or p5!="0" or p6!="0" or p7!="0" or p8!="0":
            totalsum1=int(p1)+int(p2)+int(p3)+int(p4)
            #print(totalsum1)
            #print (2**(12-totalsum1) + 2**(12-p1) + 2**(12-p4))
            totalsum2=int(p5)+int(p6)+int(p7)+int(p8)
            #print(totalsum2)
        
        value1=noisechange(binary12bitnoise1,p1)
        #print(value1)

        value2=noisechange(binary12bitnoise1,p2)
        #print(value2)

        value3=noisechange(binary12bitnoise1,p3)
        #print(value3)

        value4=noisechange(binary12bitnoise1,p4)
        #print(value4)

        value5=noisechange(binary12bitnoise2,p5)
        #print(value5)
        
        value6=noisechange(binary12bitnoise2,p6)
        #print(value6)
        
        value7=noisechange(binary12bitnoise2,p7)
        #print(value7)
        
        value8=noisechange(binary12bitnoise2,p8)
        #print(value8)

        
        #binary12bitnoise11 = binary12bit(binary8bitmainnoise1, value1, value2, value3, value4)
        #binary12bitnoise12 = binary12bit(binary8bitmainnoise2, value5, value6, value7, value8)
        binary12bitnoise11 = binary12bit(binary8bitmainnoise1, c1value1, c2value1, c4value1, c8value1)
        binary12bitnoise12 = binary12bit(binary8bitmainnoise2, c1value2, c2value2, c4value2, c8value2)
        #print(binary12bitnoise11)
        #print(binary12bitnoise12)

        backdecnoise1212=binarytodec(binary12bitnoise11)
        backdecnoise1222=binarytodec(binary12bitnoise12)
        #print(backdecnoise1212)
        #print(backdecnoise1222)


        noisebackchar1=""
        noisebackchar2=""
        if totalsum1 > 12 or totalsum2 > 12:
            
            print("More than one error due to noise")
        elif (12 >= totalsum1 > 0) or (12 >= totalsum2 > 0):
            
            if backdecnoise1212 != backdecmain1:
                backdecnoise121212 = backdecnoise1212 - (2**(12-totalsum1))
                #print (backdecnoise121212)
                backdecnoise121212=str(backdecnoise121212)
                if backdecnoise121212[0]=='-':
                    backdecnoise121212=backdecnoise121212[1:]
                    backdecnoise121212=int(backdecnoise121212)
                    #print(backdecnoise122222)
                backdecnoise121212=int(backdecnoise121212)
                binarynoisemain1=inttobinary12bit (backdecnoise121212)
                #print (binarynoisemain1)

                noisebinary8bitmain1=binary8bit(binarynoisemain1)            
                #print(noisebinary8bitmain1)
                
                noisebackdec1=binarytodec(noisebinary8bitmain1)        
                #print(noisebackdec1)
                

                noisebackchar1=asciitostring(noisebackdec1)
                if noisebackchar1=="`":
                    noisebackchar1=" "

                #print(noisebackchar1)
            
            if backdecnoise1222 != backdecmain1:
                backdecnoise122222 = backdecnoise1222 - (2**(12-totalsum2))
                backdecnoise122222=str(backdecnoise122222)
                #print (backdecnoise122222)
                if backdecnoise122222[0]=='-':
                    backdecnoise122222=backdecnoise122222[1:]
                    backdecnoise122222=int(backdecnoise122222)
                    #print(backdecnoise122222)
                backdecnoise122222=int(backdecnoise122222)
                binarynoisemain2=inttobinary12bit (backdecnoise122222)
                #print (binarynoisemain2)
                
                noisebinary8bitmain2=binary8bit(binary12bitnoise12)
                #print(noisebinary8bitmain2)
                
                noisebackdec2=binarytodec(noisebinary8bitmain2)
                #print(noisebackdec2)

                noisebackchar2=asciitostring(noisebackdec2)
                #print(noisebackchar2)
                if noisebackchar2=="`":
                    noisebackchar2=" "
        

        
        
        #print(backbinary1[0] == binary12bitnoise11[0])

        #print(backbinary1[1] == binary12bitnoise11[1])

        #print(backbinary1[3]==binary12bitnoise11[3])

        #print(backbinary1[7]==binary12bitnoise11[7])

        #print(backbinary2[0]==binary12bitnoise12[0])
          
        #print(backbinary2[1]==binary12bitnoise12[1])

        #print(backbinary2[3]==binary12bitnoise12[3])

        #print(backbinary2[7]==binary12bitnoise12[7])


        print("Original message took in function : ",inputstring)
        print("Transmitted string : ", stringreturn1+stringreturn2+stringreturn3)
        print("Received noisy message : ",stringnoise1+stringnoise2+stringnoise3)
        #print("Final Converted message:",fullbackchar)

        #print("Noise Converted message:",fullbackcharnoise)
        if fullbackcharnoise[1]=='`':
            fullbackcharnoise=fullbackchar
            #print("Noise Converted message changed space:",fullbackcharnoise)
        else:
            fullbackcharnoise=fullbackcharnoise
            
        if (inputstring != fullbackcharnoise):
            if len(noisebackchar1)==0:
                fullbackcharnoise=fullbackcharnoise
            if len(noisebackchar2)==0:
                fullbackcharnoise=fullbackcharnoise

            if (len(noisebackchar1)==0) and (len(noisebackchar2)!=0):
                fullbackcharnoise=backcharnoise1 + noisebackchar2
            if (len(noisebackchar2)==0) and (len(noisebackchar1)!=0):
                fullbackcharnoise=noisebackchar1 + backcharnoise2
            else:
                fullbackcharnoise=noisebackchar1+noisebackchar2
        else:
            fullbackcharnoise=fullbackcharnoise
    #    return fullbackchar
        print("Noise Converted message changed:",fullbackcharnoise)
        return fullbackcharnoise
    inputstringmain = input("Enter the string you want to transmit:")



    length=len(inputstringmain)

    #while not valid(inputstring) :
    #    inputstring = input("Error! Enter lower case string from a to z you want to transmit:")
    if (length)% 2 == 1:
        inputstringmain = inputstringmain + " "

    returnmessage=""
    returnnoise=""
    for i in range(0,length,2):
        inputmain=inputstringmain[i:i+2]
    #    returnmessage+=twocharacter(inputmain)
        returnnoise+=twocharacter(inputmain)

    print("Original message : ",inputstringmain)
    print("Return noise : ",returnnoise)
    #print("Return message : ",returnmessage)
    
    #Asking input from user if wants to perfom another calculation.
    transmitinput = input("Do you want to transmit again:")
    if (transmitinput=='y') or (transmitinput=='Y'):
        transmitagain=True
    elif (transmitinput=='n') or (transmitinput=='N'):
        transmitagain= False
    else:
        #Helping user with input.
        transmitinput = input("Error!!Please Enter Y or y if you want to transmit again and N or n if you don't want to transmit:")
        if (transmitinput=='y') or (transmitinput=='Y'):
            transmitagain=True
        elif (transmitinput=='n') or (transmitinput=='N'):
            transmitagain= False
        else:
            print("Invalid input!!You have exceeded the maximum limit to try. If you want to calculate again , please restart the program")
            break
