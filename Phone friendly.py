import random
global tempoutput

content1={}
content1["a"] = ["y","s","w","q","y","w","e","x","w","c","s","l","b","e","p","w","w","m","v","p","o","a","e","z","s","n"]
content1["b"] = ["m","e","u","c","u","p","d","r","v","y","l","e","a","n","s","j","o","x","t","g","v","b","i","y","p","u"]
content1["c"] = ["s","p","f","b","h","o","q","y","u","a","i","u","d","r","j","o","t","g","k","x","d","c","s","d","k","w"]
content1["d"] = ["n","x","l","m","l","j","b","q","y","q","e","x","c","i","e","f","s","u","i","k","c","d","n","c","i","t"]
content1["e"] = ["w","b","y","k","i","t","a","n","m","x","d","b","i","a","d","z","h","y","f","l","n","e","a","m","y","x"]
content1["f"] = ["x","l","c","w","n","h","u","i","o","m","u","n","u","h","n","d","y","l","e","m","h","f","p","w","l","s"]
content1["g"] = ["z","m","q","n","v","s","t","l","j","h","y","o","j","l","q","y","n","c","z","b","z","g","t","v","t","p"]
content1["h"] = ["i","w","v","o","c","f","w","u","x","g","n","p","t","f","z","l","e","w","m","z","f","h","o","x","j","m"]
content1["i"] = ["h","u","t","t","e","l","m","f","p","w","c","w","e","d","v","u","u","s","d","t","s","i","b","q","d","r"]
content1["j"] = ["q","r","m","p","m","d","r","w","g","s","k","z","g","q","c","b","x","k","x","o","y","j","r","r","h","k"]
content1["k"] = ["r","t","r","e","p","n","n","s","n","l","j","v","p","y","l","n","r","j","c","d","x","k","y","p","c","j"]
content1["l"] = ["o","f","d","s","d","i","y","g","s","k","b","a","v","g","k","h","q","f","r","e","r","l","v","n","f","v"]
content1["m"] = ["b","g","j","d","j","y","i","p","e","f","p","t","x","o","u","p","z","a","h","f","w","m","w","e","z","h"]
content1["n"] = ["d","z","o","g","f","k","k","e","k","r","h","f","s","b","f","k","g","q","w","w","e","n","d","l","v","a"]
content1["o"] = ["l","v","n","h","q","c","p","t","f","p","r","g","z","m","y","c","b","p","y","j","a","o","h","u","x","q"]
content1["p"] = ["t","c","z","j","k","b","o","m","i","o","m","h","k","w","a","m","v","o","q","a","q","p","f","k","b","g"]
content1["q"] = ["j","y","g","a","o","r","c","d","z","d","z","r","r","j","g","v","l","n","p","r","p","q","z","i","r","o"]
content1["r"] = ["k","j","k","x","z","q","j","b","t","n","o","q","q","c","t","s","k","v","l","q","l","r","j","j","q","i"]
content1["s"] = ["c","a","x","l","t","g","v","k","l","j","a","y","n","x","b","r","d","i","u","v","i","s","c","t","a","f"]
content1["t"] = ["p","k","i","i","s","e","g","o","r","v","v","m","h","v","r","x","c","z","b","i","u","t","g","s","g","d"]
content1["u"] = ["v","i","b","v","b","z","f","h","c","z","f","c","f","z","m","i","i","d","s","y","t","u","x","o","w","b"]
content1["v"] = ["u","o","h","u","g","x","s","z","b","t","t","k","l","t","i","q","p","r","a","s","b","v","l","g","n","l"]
content1["w"] = ["e","h","a","f","x","a","h","j","a","i","x","i","y","p","x","a","a","h","n","n","m","w","m","f","u","c"]
content1["x"] = ["f","d","s","r","w","v","z","a","h","e","w","d","m","s","w","t","j","b","j","c","k","x","u","h","o","e"]
content1["y"] = ["a","q","e","z","a","m","l","c","d","b","g","s","w","k","o","g","f","e","o","u","j","y","k","b","e","z"]
content1["z"] = ["g","n","p","y","r","u","x","v","q","u","q","j","o","u","h","e","m","t","g","h","g","z","q","a","m","y"]
content2={}
content2["a"] = ["d","i","l","m","u","t","o","d","z","z","k","e","n","v","k","o","p","o","g","u","c","y","z","l","x","b"]
content2["b"] = ["e","o","g","s","c","s","z","u","r","r","f","w","o","f","x","e","l","t","q","g","z","l","x","j","u","a"]
content2["c"] = ["u","e","h","d","b","y","t","i","i","e","h","q","f","i","z","n","h","s","i","o","a","o","e","i","n","g"]
content2["d"] = ["a","j","z","c","k","v","g","a","q","s","e","x","t","m","w","i","n","z","p","t","g","n","r","q","q","j"]
content2["e"] = ["b","c","x","f","f","q","f","o","t","c","d","a","k","h","v","b","g","h","l","s","j","k","c","g","s","l"]
content2["f"] = ["j","k","q","e","e","o","e","k","g","j","b","j","c","b","n","x","m","i","n","v","o","z","l","k","o","u"]
content2["g"] = ["t","q","b","n","m","i","d","j","f","y","n","r","x","y","s","s","e","p","a","b","d","j","k","e","w","c"]
content2["h"] = ["v","m","c","k","l","m","l","p","l","m","c","u","p","e","j","y","c","e","w","x","p","q","w","m","l","x"]
content2["i"] = ["n","a","w","l","x","g","k","c","c","l","v","p","s","c","p","d","u","f","c","l","k","x","u","c","k","y"]
content2["j"] = ["f","d","u","t","s","k","w","g","v","f","w","f","u","l","h","q","w","r","r","q","e","g","v","b","r","d"]
content2["k"] = ["s","f","t","h","d","j","i","f","w","t","a","l","e","o","a","v","o","x","m","n","i","e","g","f","i","p"]
content2["l"] = ["q","p","a","i","h","r","h","y","h","i","r","k","r","j","m","r","b","u","e","i","w","b","f","a","h","e"]
content2["m"] = ["o","h","v","a","g","h","y","t","n","h","y","s","z","d","l","u","f","y","k","y","u","r","o","h","v","w"]
content2["n"] = ["i","w","o","g","o","w","v","s","m","o","g","o","a","x","f","c","d","q","f","k","q","d","y","s","c","v"]
content2["o"] = ["m","b","n","p","n","f","a","e","p","n","z","n","b","k","t","a","k","a","t","c","f","c","m","y","f","t"]
content2["p"] = ["x","l","r","o","y","z","r","h","o","v","s","i","h","t","i","t","a","g","d","r","h","w","t","x","y","k"]
content2["q"] = ["l","g","f","w","z","e","x","v","d","w","t","c","w","s","u","j","y","n","b","j","n","h","s","d","d","z"]
content2["r"] = ["y","z","p","x","t","l","p","z","b","b","l","g","l","w","y","l","z","j","j","p","x","m","d","t","j","s"]
content2["s"] = ["k","x","y","b","j","b","u","n","u","d","p","m","i","q","g","g","t","c","v","e","v","v","q","n","e","r"]
content2["t"] = ["g","v","k","j","r","a","c","m","e","k","q","y","d","p","o","p","s","b","o","d","y","u","p","r","z","o"]
content2["u"] = ["c","y","j","v","a","x","s","b","s","x","x","h","j","z","q","m","i","l","y","a","m","t","i","z","b","f"]
content2["v"] = ["h","t","m","u","w","d","n","q","j","p","i","z","y","a","e","k","x","w","s","f","s","s","j","w","m","n"]
content2["w"] = ["z","n","i","q","v","n","j","x","k","q","j","b","q","r","d","z","j","v","h","z","l","p","h","v","g","m"]
content2["x"] = ["p","s","e","r","i","u","q","w","y","u","u","d","g","n","b","f","v","k","z","h","r","i","b","p","a","h"]
content2["y"] = ["r","u","s","z","p","c","m","l","x","g","m","t","v","g","r","h","q","m","u","m","t","a","n","o","p","i"]
content2["z"] = ["w","r","d","y","q","p","b","r","a","a","o","v","m","u","c","w","r","d","x","w","b","f","a","u","t","q"]
content3={}
content3["a"] = ["m","d","o","t","y","p","z","v","w","u","f","g","g","s","m","o","v","e","d","y","o","x","f","m","n","e"]
content3["b"] = ["t","u","l","p","w","g","n","l","f","o","v","u","q","e","h","w","o","d","f","i","d","f","c","w","i","r"]
content3["c"] = ["o","g","y","m","d","d","u","e","j","w","p","j","v","r","e","y","z","n","j","g","m","v","b","x","f","j"]
content3["d"] = ["e","a","e","h","c","c","i","w","l","t","q","l","k","p","f","s","j","b","a","j","b","g","q","n","s","y"]
content3["e"] = ["d","z","d","g","h","z","m","c","t","i","y","q","f","b","c","r","r","a","t","k","n","i","m","z","u","a"]
content3["f"] = ["q","w","q","n","q","i","x","q","b","s","a","y","e","w","d","k","w","j","b","u","i","b","a","o","c","q"]
content3["g"] = ["p","c","w","e","t","b","y","o","h","x","k","a","a","h","w","t","k","r","p","c","t","d","v","i","y","n"]
content3["h"] = ["r","n","p","d","e","o","k","k","g","v","u","t","s","g","b","x","y","w","x","s","r","o","s","u","p","k"]
content3["i"] = ["l","j","r","o","n","f","d","u","y","e","n","k","j","l","j","m","s","z","q","b","f","e","l","g","b","p"]
content3["j"] = ["x","i","n","q","u","x","o","r","c","n","l","c","i","y","i","z","d","f","c","d","p","l","w","v","x","c"]
content3["k"] = ["w","s","t","y","v","s","h","h","p","l","g","i","d","v","z","f","g","y","y","e","q","r","u","q","t","h"]
content3["l"] = ["i","v","b","r","m","y","s","b","d","k","j","d","t","i","r","p","x","p","z","m","y","j","i","p","o","o"]
content3["m"] = ["a","r","z","c","l","w","e","p","q","p","w","p","x","n","a","i","p","s","o","l","c","y","e","a","q","w"]
content3["n"] = ["s","h","j","f","i","t","b","x","s","j","i","w","p","m","p","q","t","c","s","r","e","w","p","d","a","g"]
content3["o"] = ["c","x","a","i","x","h","j","g","r","b","s","z","z","q","y","a","b","u","m","w","a","h","z","f","l","l"]
content3["p"] = ["g","y","h","b","s","a","v","m","k","m","c","m","n","d","n","l","m","l","g","t","j","q","n","l","h","i"]
content3["q"] = ["f","t","f","j","f","u","r","f","m","y","d","e","b","o","x","n","u","v","i","z","k","p","d","k","m","f"]
content3["r"] = ["h","m","i","l","z","v","q","j","o","z","x","x","y","c","l","e","e","g","w","n","h","k","t","s","w","b"]
content3["s"] = ["n","k","u","x","p","k","l","y","n","f","o","v","h","a","u","d","i","m","n","h","v","u","h","r","d","v"]
content3["t"] = ["b","q","k","a","g","n","w","z","e","d","z","h","l","z","v","g","n","x","e","p","g","z","r","y","k","u"]
content3["u"] = ["z","b","s","w","j","q","c","i","v","a","h","b","w","x","s","v","q","o","v","f","x","s","k","h","e","t"]
content3["v"] = ["y","l","x","z","k","r","p","a","u","h","b","s","c","k","t","u","a","q","u","x","s","c","g","j","z","s"]
content3["w"] = ["k","f","g","u","b","m","t","d","a","c","m","n","u","f","g","b","f","h","r","o","z","n","j","b","r","m"]
content3["x"] = ["j","o","v","s","o","j","f","n","z","g","r","r","m","u","q","h","l","t","h","v","u","a","y","c","j","z"]
content3["y"] = ["v","p","c","k","a","l","g","s","i","q","e","f","r","j","o","c","h","k","k","a","l","m","x","t","g","d"]
content3["z"] = ["u","e","m","v","r","e","a","t","x","r","t","o","o","t","k","j","c","i","l","q","w","t","o","e","v","x"]



def temp1(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=content1["a"][rotor]
    elif templetter=="b":
        tempoutput=content1["b"][rotor]
    elif templetter=="c":
        tempoutput=content1["c"][rotor]
    elif templetter=="d":
        tempoutput=content1["d"][rotor]
    elif templetter=="e":
        tempoutput=content1["e"][rotor]
    elif templetter=="f":
        tempoutput=content1["f"][rotor]
    elif templetter=="g":
        tempoutput=content1["g"][rotor]
    elif templetter=="h":
        tempoutput=content1["h"][rotor]
    elif templetter=="i":
        tempoutput=content1["i"][rotor]
    elif templetter=="j":
        tempoutput=content1["j"][rotor]
    elif templetter=="k":
        tempoutput=content1["k"][rotor]
    elif templetter=="l":
        tempoutput=content1["l"][rotor]
    elif templetter=="m":
        tempoutput=content1["m"][rotor]
    elif templetter=="n":
        tempoutput=content1["n"][rotor]
    elif templetter=="o":
        tempoutput=content1["o"][rotor]
    elif templetter=="p":
        tempoutput=content1["p"][rotor]
    elif templetter=="q":
        tempoutput=content1["q"][rotor]
    elif templetter=="r":
        tempoutput=content1["r"][rotor]
    elif templetter=="s":
        tempoutput=content1["s"][rotor]
    elif templetter=="t":
        tempoutput=content1["t"][rotor]
    elif templetter=="u":
        tempoutput=content1["u"][rotor]
    elif templetter=="v":
        tempoutput=content1["v"][rotor]
    elif templetter=="w":
        tempoutput=content1["w"][rotor]
    elif templetter=="x":
        tempoutput=content1["x"][rotor]
    elif templetter=="y":
        tempoutput=content1["y"][rotor]
    elif templetter=="z":
        tempoutput=content1["z"][rotor]
    elif templetter==" ":
        tempoutput=" "

def temp2(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=content2["a"][rotor]
    elif templetter=="b":
        tempoutput=content2["b"][rotor]
    elif templetter=="c":
        tempoutput=content2["c"][rotor]
    elif templetter=="d":
        tempoutput=content2["d"][rotor]
    elif templetter=="e":
        tempoutput=content2["e"][rotor]
    elif templetter=="f":
        tempoutput=content2["f"][rotor]
    elif templetter=="g":
        tempoutput=content2["g"][rotor]
    elif templetter=="h":
        tempoutput=content2["h"][rotor]
    elif templetter=="i":
        tempoutput=content2["i"][rotor]
    elif templetter=="j":
        tempoutput=content2["j"][rotor]
    elif templetter=="k":
        tempoutput=content2["k"][rotor]
    elif templetter=="l":
        tempoutput=content2["l"][rotor]
    elif templetter=="m":
        tempoutput=content2["m"][rotor]
    elif templetter=="n":
        tempoutput=content2["n"][rotor]
    elif templetter=="o":
        tempoutput=content2["o"][rotor]
    elif templetter=="p":
        tempoutput=content2["p"][rotor]
    elif templetter=="q":
        tempoutput=content2["q"][rotor]
    elif templetter=="r":
        tempoutput=content2["r"][rotor]
    elif templetter=="s":
        tempoutput=content2["s"][rotor]
    elif templetter=="t":
        tempoutput=content2["t"][rotor]
    elif templetter=="u":
        tempoutput=content2["u"][rotor]
    elif templetter=="v":
        tempoutput=content2["v"][rotor]
    elif templetter=="w":
        tempoutput=content2["w"][rotor]
    elif templetter=="x":
        tempoutput=content2["x"][rotor]
    elif templetter=="y":
        tempoutput=content2["y"][rotor]
    elif templetter=="z":
        tempoutput=content2["z"][rotor]
    elif templetter==" ":
        tempoutput=" "

def temp3(templetter,rotor):
    global tempoutput
    if templetter=="a":
        tempoutput=content3["a"][rotor]
    elif templetter=="b":
        tempoutput=content3["b"][rotor]
    elif templetter=="c":
        tempoutput=content3["c"][rotor]
    elif templetter=="d":
        tempoutput=content3["d"][rotor]
    elif templetter=="e":
        tempoutput=content3["e"][rotor]
    elif templetter=="f":
        tempoutput=content3["f"][rotor]
    elif templetter=="g":
        tempoutput=content3["g"][rotor]
    elif templetter=="h":
        tempoutput=content3["h"][rotor]
    elif templetter=="i":
        tempoutput=content3["i"][rotor]
    elif templetter=="j":
        tempoutput=content3["j"][rotor]
    elif templetter=="k":
        tempoutput=content3["k"][rotor]
    elif templetter=="l":
        tempoutput=content3["l"][rotor]
    elif templetter=="m":
        tempoutput=content3["m"][rotor]
    elif templetter=="n":
        tempoutput=content3["n"][rotor]
    elif templetter=="o":
        tempoutput=content3["o"][rotor]
    elif templetter=="p":
        tempoutput=content3["p"][rotor]
    elif templetter=="q":
        tempoutput=content3["q"][rotor]
    elif templetter=="r":
        tempoutput=content3["r"][rotor]
    elif templetter=="s":
        tempoutput=content3["s"][rotor]
    elif templetter=="t":
        tempoutput=content3["t"][rotor]
    elif templetter=="u":
        tempoutput=content3["u"][rotor]
    elif templetter=="v":
        tempoutput=content3["v"][rotor]
    elif templetter=="w":
        tempoutput=content3["w"][rotor]
    elif templetter=="x":
        tempoutput=content3["x"][rotor]
    elif templetter=="y":
        tempoutput=content3["y"][rotor]
    elif templetter=="z":
        tempoutput=content3["z"][rotor]
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

