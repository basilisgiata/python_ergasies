import random,itertools
from operator import itemgetter

#oi kanones tou paixnidiou ine fiveofakind,fourofakind,fullhouse,threeofakind,twopair,onepair,highcard

deck = list(itertools.product(range(2,15),['Spade','Heart','Diamond','Club']))
deck=deck+deck
print("Handing out cards...")
print("11=Jack,12=Queen,13=King,14=Ace")
random.shuffle(deck)
x1=[]
x2=[]
print("Player 1 got")
for i in range(5):
   x1.append(deck[i] )
x1=sorted(x1, key=itemgetter(0))
print(x1)
print("Player 2 got")
for i in range(10):
    if i>=5:  
     x2.append(deck[i] )
x2=sorted(x2, key=itemgetter(0))
print(x2)
def check(x1):
    x=[i[0] for i in x1]
    if x[0]==x[4]:
        return int(x[0]+x[1]+x[2]+x[3]+x[4]+40000)
    if x[0]==x[3] or x[1]==x[4]:
        return int((x[1]*4)+30000)
    if (x[0]==x[2] and x[3]==x[4]):
        return int(3*x[0]+2*x[3]+20000)
    if x[0]==x[1] and x[2]==x[4]:
        return int(3*x[2]+2*x[0]+20000)
    if x[0]==x[2] or x[1]==x[3] or x[2]==x[4]:
        return int(3*x[2]+1000)
    if (x[0]==x[1] and x[2]==x[3])or(x[1]==x[2] and x[3]==x[4])or(x[0]==x[1] and x[3]==x[4]):
        return int(2*(x[1]+x[3])+100)
    c=1
    for j in range (4):
        if x[j]==x[j+1]:
            c=c+1
            if c==2:
                return int(2*x[j]+14)
        
    return x[4]
     
       

x=check(x1)
y=check(x2)

if x>y:
    print("Player 1 wins")
elif x<y:
    print("Player 2 wins")
else:
    for i in range(4):
        if int(x1[4-i][0])>int(x2[4-i][0]):
            print("Player 1 wins cause of High Card")
            break
        elif x1[4-i][0]<x2[4-i][0]:
            print("Player 2 wins  cause of High Card")
            break
