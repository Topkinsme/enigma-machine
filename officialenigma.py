import random
import theasig as code
global tempoutput

def temp1(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=code.content1["a"][rotor]
    elif templetter=="b":
        tempoutput=code.content1["b"][rotor]
    elif templetter=="c":
        tempoutput=code.content1["c"][rotor]
    elif templetter=="d":
        tempoutput=code.content1["d"][rotor]
    elif templetter=="e":
        tempoutput=code.content1["e"][rotor]
    elif templetter=="f":
        tempoutput=code.content1["f"][rotor]
    elif templetter=="g":
        tempoutput=code.content1["g"][rotor]
    elif templetter=="h":
        tempoutput=code.content1["h"][rotor]
    elif templetter=="i":
        tempoutput=code.content1["i"][rotor]
    elif templetter=="j":
        tempoutput=code.content1["j"][rotor]
    elif templetter=="k":
        tempoutput=code.content1["k"][rotor]
    elif templetter=="l":
        tempoutput=code.content1["l"][rotor]
    elif templetter=="m":
        tempoutput=code.content1["m"][rotor]
    elif templetter=="n":
        tempoutput=code.content1["n"][rotor]
    elif templetter=="o":
        tempoutput=code.content1["o"][rotor]
    elif templetter=="p":
        tempoutput=code.content1["p"][rotor]
    elif templetter=="q":
        tempoutput=code.content1["q"][rotor]
    elif templetter=="r":
        tempoutput=code.content1["r"][rotor]
    elif templetter=="s":
        tempoutput=code.content1["s"][rotor]
    elif templetter=="t":
        tempoutput=code.content1["t"][rotor]
    elif templetter=="u":
        tempoutput=code.content1["u"][rotor]
    elif templetter=="v":
        tempoutput=code.content1["v"][rotor]
    elif templetter=="w":
        tempoutput=code.content1["w"][rotor]
    elif templetter=="x":
        tempoutput=code.content1["x"][rotor]
    elif templetter=="y":
        tempoutput=code.content1["y"][rotor]
    elif templetter=="z":
        tempoutput=code.content1["z"][rotor]
    elif templetter==" ":
        tempoutput=" "

def temp2(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=code.content2["a"][rotor]
    elif templetter=="b":
        tempoutput=code.content2["b"][rotor]
    elif templetter=="c":
        tempoutput=code.content2["c"][rotor]
    elif templetter=="d":
        tempoutput=code.content2["d"][rotor]
    elif templetter=="e":
        tempoutput=code.content2["e"][rotor]
    elif templetter=="f":
        tempoutput=code.content2["f"][rotor]
    elif templetter=="g":
        tempoutput=code.content2["g"][rotor]
    elif templetter=="h":
        tempoutput=code.content2["h"][rotor]
    elif templetter=="i":
        tempoutput=code.content2["i"][rotor]
    elif templetter=="j":
        tempoutput=code.content2["j"][rotor]
    elif templetter=="k":
        tempoutput=code.content2["k"][rotor]
    elif templetter=="l":
        tempoutput=code.content2["l"][rotor]
    elif templetter=="m":
        tempoutput=code.content2["m"][rotor]
    elif templetter=="n":
        tempoutput=code.content2["n"][rotor]
    elif templetter=="o":
        tempoutput=code.content2["o"][rotor]
    elif templetter=="p":
        tempoutput=code.content2["p"][rotor]
    elif templetter=="q":
        tempoutput=code.content2["q"][rotor]
    elif templetter=="r":
        tempoutput=code.content2["r"][rotor]
    elif templetter=="s":
        tempoutput=code.content2["s"][rotor]
    elif templetter=="t":
        tempoutput=code.content2["t"][rotor]
    elif templetter=="u":
        tempoutput=code.content2["u"][rotor]
    elif templetter=="v":
        tempoutput=code.content2["v"][rotor]
    elif templetter=="w":
        tempoutput=code.content2["w"][rotor]
    elif templetter=="x":
        tempoutput=code.content2["x"][rotor]
    elif templetter=="y":
        tempoutput=code.content2["y"][rotor]
    elif templetter=="z":
        tempoutput=code.content2["z"][rotor]
    elif templetter==" ":
        tempoutput=" "

def temp3(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=code.content3["a"][rotor]
    elif templetter=="b":
        tempoutput=code.content3["b"][rotor]
    elif templetter=="c":
        tempoutput=code.content3["c"][rotor]
    elif templetter=="d":
        tempoutput=code.content3["d"][rotor]
    elif templetter=="e":
        tempoutput=code.content3["e"][rotor]
    elif templetter=="f":
        tempoutput=code.content3["f"][rotor]
    elif templetter=="g":
        tempoutput=code.content3["g"][rotor]
    elif templetter=="h":
        tempoutput=code.content3["h"][rotor]
    elif templetter=="i":
        tempoutput=code.content3["i"][rotor]
    elif templetter=="j":
        tempoutput=code.content3["j"][rotor]
    elif templetter=="k":
        tempoutput=code.content3["k"][rotor]
    elif templetter=="l":
        tempoutput=code.content3["l"][rotor]
    elif templetter=="m":
        tempoutput=code.content3["m"][rotor]
    elif templetter=="n":
        tempoutput=code.content3["n"][rotor]
    elif templetter=="o":
        tempoutput=code.content3["o"][rotor]
    elif templetter=="p":
        tempoutput=code.content3["p"][rotor]
    elif templetter=="q":
        tempoutput=code.content3["q"][rotor]
    elif templetter=="r":
        tempoutput=code.content3["r"][rotor]
    elif templetter=="s":
        tempoutput=code.content3["s"][rotor]
    elif templetter=="t":
        tempoutput=code.content3["t"][rotor]
    elif templetter=="u":
        tempoutput=code.content3["u"][rotor]
    elif templetter=="v":
        tempoutput=code.content3["v"][rotor]
    elif templetter=="w":
        tempoutput=code.content3["w"][rotor]
    elif templetter=="x":
        tempoutput=code.content3["x"][rotor]
    elif templetter=="y":
        tempoutput=code.content3["y"][rotor]
    elif templetter=="z":
        tempoutput=code.content3["z"][rotor]
    elif templetter==" ":
        tempoutput=" "

print("Only input lower case letters, don't input punctutions. Spaces are allowed. Only enter rotor numbers between 1 and 26 for all 3 slots. \n")
choice=input("Do you want a random stating rotor position?Input y for Yes and n for no \n")
if choice=="y":
    rotor1=int((random.random()*26)+1)
    rotor2=int((random.random()*26)+1)
    rotor3=int((random.random()*26)+1)
    print("Your rotor number is ",rotor1," ",rotor2," ",rotor3)
elif choice=="n":
    rotor1=int(input("Enter rotor configuration 1"))
    rotor2=int(input("Enter rotor configuration 2"))
    rotor3=int(input("Enter rotor configuration 3"))
rotor1-=1
rotor2-=1
rotor3-=1
tinput=input("Enter the text \n")
length=len(tinput)
count=0
output=""
while count<length:
    templetter=tinput[count]
    temp1(templetter,rotor1)
    temp2(tempoutput,rotor2)
    temp3(tempoutput,rotor3)
    temp2(tempoutput,rotor2)
    temp1(tempoutput,rotor1)
    output+=tempoutput 
    count+=1
    rotor1=rotor1+1
    if rotor1 ==26:
        rotor2+=1
        rotor1=0
        if rotor2==26:
            rotor3+=1
            rotor2=0
            if rotor3==26:
                rotor3=0
                 
print(output)

dummy=input("\n Press any key to exit")

