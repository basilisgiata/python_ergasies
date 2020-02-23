#open file
file = open("text.txt", "r")

data = file.read()
#convert func
def convert(lst):
    return ''.join(lst).split()
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
      
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1

lst =  [data] 
d=convert(lst)
print(d)
p=""
for n,i in enumerate(d):
    s=list(i)
    c=0
    
    for j in s:
        c=c+1
    if c>3:
        k=s[0]
        s.append(k)
        s.append('ay')
        s.pop(0)
    i=listToString(s)
    
    p +=i+" "
print("Converting...")
print (p)

#o kodikas doulevi opos prepei otan iparxoun mono kena anamesa stis leksis dld
#prin kai meta ta simia stiksis prepei na exoun keno

 
