
while(True):
    def dectobin(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= int(userinput[:pointindex])
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=int(userinput)
            fractionpart=''
        integerresult=''
        while(integerpart!=0):
            if integerpart%2==0:
                integerresult +='0'
                integerpart=integerpart//2
                
            else:
                integerresult +='1'
                integerpart=integerpart//2
        integerresult=integerresult[::-1]
        
        lengthfraction=len(fractionpart)
        if lengthfraction !=0:
            
            fractionpart=float(fractionpart)/10**(lengthfraction)
            fractionresult=''
            while(fractionpart!=1):
                fractionpart=fractionpart*2
                if fractionpart>1:
                    fractionpart=fractionpart-1
                    fractionresult+='1'
                elif fractionpart<1:
                    fractionresult+='0'
                else:
                    fractionresult+='1'
            result=integerresult+'.'+fractionresult[:10]
        else:
            result=integerresult
        
        return str(result)
        
    def dectohex(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= int(userinput[:pointindex])
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=int(userinput)
            fractionpart=''
        integerresult=''
        while(integerpart!=0):
            reminder=integerpart%16
            if reminder == 10:
                integerresult=integerresult+'A'
            elif reminder == 11:
                integerresult=integerresult+'B'
            elif reminder == 12:
                integerresult=integerresult+'C'
            elif reminder == 13:
                integerresult=integerresult+'D'
            elif reminder == 14:
                integerresult=integerresult+'E'
            elif reminder == 15:
                integerresult=integerresult+'F'
            else:
                integerresult=integerresult+str(integerpart%16)
            integerpart=integerpart//16
            
            
        integerresult=integerresult[::-1]
        
        lengthfraction=len(fractionpart)
        if lengthfraction !=0:
            
            fractionpart=float(fractionpart)/10**(lengthfraction)
            fractionresult=''
            while(fractionpart!=0):
                fractionpart=fractionpart*16
                if fractionpart>1:
                    intfractionpart=int(fractionpart)
                    
                    if intfractionpart == 10:
                        fractionresult=fractionresult+'A'
                    elif intfractionpart == 11:
                        fractionresult=fractionresult+'B'
                    elif intfractionpart == 12:
                        fractionresult=fractionresult+'C'
                    elif intfractionpart == 13:
                        fractionresult=fractionresult+'D'
                    elif intfractionpart == 14:
                        fractionresult=fractionresult+'E'
                    elif intfractionpart == 15:
                        fractionresult=fractionresult+'F'
                    else:
                        fractionresult=fractionresult+str(intfractionpart)
                
                    fractionpart=fractionpart-int(fractionpart)
                elif fractionpart<1:
                    fractionresult+='0'
                else:
                    fractionresult+='1'
            result=integerresult+'.'+fractionresult[:10]
        else:
            result=integerresult
        
        return str(result)
        
    def dectooct(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= int(userinput[:pointindex])
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=int(userinput)
            fractionpart=''
        integerresult=''
        while(integerpart!=0):
            reminder=integerpart%8
            integerresult=integerresult+str(integerpart%8)
            integerpart=integerpart//8
            
            
        integerresult=integerresult[::-1]
        
        lengthfraction=len(fractionpart)
        if lengthfraction !=0:
            
            fractionpart=float(fractionpart)/10**(lengthfraction)
            fractionresult=''
            while(fractionpart!=0):
                fractionpart=fractionpart*8
                if fractionpart>1:
                    intfractionpart=int(fractionpart)
                    
                    
                    fractionresult=fractionresult+str(intfractionpart)
                
                    fractionpart=fractionpart-int(fractionpart)
                elif fractionpart<1:
                    fractionresult+='0'
                else:
                    fractionresult+='1'
            result=integerresult+'.'+fractionresult[:10]
        else:
            result=integerresult
        
        return str(result)
    
    
    def bintodec(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= userinput[:pointindex]
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=userinput
            fractionpart=''
        integervalue=0
        integerpower=len(integerpart)-1
        
        for i in integerpart:
            if i != '0':
                integervalue = integervalue + 2**integerpower
                
            integerpower = integerpower - 1
        
        fractionvalue=0
        fractionpower=-1
        for i in fractionpart:
            if i != '0':
                fractionvalue = fractionvalue + 2**fractionpower
                
            fractionpower = fractionpower - 1
        result=integervalue+fractionvalue
        return str(result)
    
    def octtodec(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= userinput[:pointindex]
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=userinput
            fractionpart=''
        integervalue=0
        integerpower=len(integerpart)-1
        
        for i in integerpart:
            if i != '0':
                integervalue = integervalue + int(i) * 8**integerpower
                
            integerpower = integerpower - 1
        
        fractionvalue=0
        fractionpower=-1
        for i in fractionpart:
            if i != '0':
                fractionvalue = fractionvalue + int(i) * 8**fractionpower
                
            fractionpower = fractionpower - 1
        result=integervalue+fractionvalue
        return str(result)
    
    def hextodec(userinput):
        pointindex = userinput.find(".")
        if pointindex != -1:
            integerpart= userinput[:pointindex]
            fractionpart= userinput[pointindex+1:]
        else:
            integerpart=userinput
            fractionpart=''
        integervalue=0
        integerpower=len(integerpart)-1
        
        for i in integerpart:
            if i == 'A':
                integervalue = integervalue + 10 * 16**integerpower
            elif i == 'B':
                integervalue = integervalue + 11 * 16**integerpower
            elif i == 'C':
                integervalue = integervalue + 12 * 16**integerpower
            elif i == 'D':
                integervalue = integervalue + 13 * 16**integerpower
            elif i == 'E':
                integervalue = integervalue + 14 * 16**integerpower
            elif i == 'F':
                integervalue = integervalue + 15 * 16**integerpower
            elif i != '0':
                integervalue = integervalue + int(i) * 16**integerpower
                
            integerpower = integerpower - 1
        
        fractionvalue=0
        fractionpower=-1
        for i in fractionpart:
            if i == 'A':
                fractionvalue = fractionvalue + 10 * 16**fractionpower
            elif i == 'B':
                fractionvalue = fractionvalue + 11 * 16**fractionpower
            elif i == 'C':
                fractionvalue = fractionvalue + 12 * 16**fractionpower
            elif i == 'D':
                fractionvalue = fractionvalue + 13 * 16**fractionpower
            elif i == 'E':
                fractionvalue = fractionvalue + 14 * 16**fractionpower
            elif i == 'F':
                fractionvalue = fractionvalue + 15 * 16**fractionpower
            elif i != '0':
                fractionvalue = fractionvalue + int(i) * 16**fractionpower
                
            fractionpower = fractionpower - 1
        result=integervalue+fractionvalue
        return str(result)
    
    
    
    def validation(userinput,firsttype):
        binlist = [".","0","1"]
        hexlist = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","."]
        octlist = ["0","1","2","3","4","5","6","7","."]
        declist = ["0","1","2","3","4","5","6","7","8","9","."]
        indicator2 = True
        
        if firsttype == 'B' or firsttype == 'b':
            for i in userinput:
              indicator = False
              for j in binlist:
                if i == j:
                  indicator = True
              if indicator == False:
                indicator2 = False
                
                break
        
        elif firsttype == 'H' or firsttype == 'h':
            for i in userinput:
              indicator = False
              for j in hexlist:
                if i == j:
                  indicator = True
              if indicator == False:
                indicator2 = False
                
                break
        
        elif firsttype == 'O' or firsttype == 'o':
            for i in userinput:
              indicator = False
              for j in octlist:
                if i == j:
                  indicator = True 
              if indicator == False:
                indicator2 = False
                
                break
        
        elif firsttype == 'D' or firsttype == 'd':
            for i in userinput:
              indicator = False
              for j in declist:
                if i == j:
                  indicator = True
              if indicator == False:
                indicator2 = False
                
                break
        else:
            indicator2 = False
        return indicator2
        
    userinput=input("Enter the Number: ")
    firsttype=input("Enter The Initial Type (B,O,D,H):  ")
    finaltype=input("Enter The Final Type (B,O,D,H):  ")
    validation=validation(userinput,firsttype)
    if validation == False:
        print("The Input Number or Type is Incorrect. Please Check agian!")
    else:
        if (finaltype == 'D' or finaltype == 'd') and (firsttype == 'B' or firsttype == 'b'):
            print(bintodec(userinput))
        elif (finaltype == 'd' or finaltype == 'D') and (firsttype == 'o' or firsttype == 'O'):
            print(octtodec(userinput))
        elif (finaltype == 'd' or finaltype == 'D') and (firsttype == 'h' or firsttype == 'H'):
            print(hextodec(userinput))
        elif (finaltype == 'b' or finaltype == 'B') and (firsttype == 'd' or firsttype == 'D'):
            print(dectobin(userinput))
        elif (finaltype == 'h' or finaltype == 'H') and (firsttype == 'd' or firsttype == 'D'):
            print(dectohex(userinput))
        elif (finaltype == 'o' or finaltype == 'O') and (firsttype == 'd' or firsttype == 'D'):
            print(dectooct(userinput))
        elif (finaltype == 'o' or finaltype == 'O') and (firsttype == 'b' or firsttype == 'B'):
            print(dectooct(bintodec(userinput)))
        elif (finaltype == 'b' or finaltype == 'B') and (firsttype == 'o' or firsttype == 'O'):
            print(dectobin(octtodec(userinput)))
        elif (finaltype == 'B' or finaltype == 'b') and (firsttype == 'h' or firsttype == 'H'):
            print(dectobin(hextodec(userinput)))
        elif (finaltype == 'h' or finaltype == 'H') and (firsttype == 'B' or firsttype == 'b'):
            print(dectohex(bintodec(userinput)))
        elif (finaltype == 'h' or finaltype == 'H') and (firsttype == 'o' or firsttype == 'O'):
            print(dectohex(octtodec(userinput)))
        elif (finaltype == 'O' or finaltype == 'o') and (firsttype == 'h' or firsttype == 'H'):
            print(dectooct(hextodec(userinput)))
        
    
