#open file
file = open("text.txt", "r")

data = file.read()
#convert func
def convert(lst):
    return ''.join(lst).split()


  

lst =  [data] 
d=convert(lst)
for i in d:
    s=list(i)
    
    c=0
    c1=0
    for j in s:
        if j=='f' or j=='c' or j=='k' or j=='r':
            c=c+1
        elif j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            continue
        else:
            c1=c1+1
    if c>c1:
        print("[",i,"]:bad")
    else:
        
        print("[",i,"]:good")
