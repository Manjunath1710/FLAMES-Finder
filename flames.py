print("FLAMES GAME")

def flames(name1,name2):
    name1=name1.lower().replace(" ","")
    name2=name2.lower().replace(" ","")
    for i in name1:
        if i in name2:
            name1=name1.replace(i,"",1)
            name2=name2.replace(i,"",1)
    count=len(name1)+len(name2)
    flames_list=["Friends","love","Affection","Marriage","Enemy","Siblings"]
    while len(flames_list)>1:
        index=(count%len(flames_list)-1)
        if index>=0:
            right=flames_list[index+1:]
            left=flames_list[:index]
            flames_list=right+left
        else:
            flames_list=flames_list[:len(flames_list)-1]              
    print("Relationship status is:",flames_list[0])

try:
    name1=input("Enter your name:")
    name2=input("Enter your partner's name:")
    flames(name1,name2)
except Exception as e:
    print("An error occurred:", e)
    
