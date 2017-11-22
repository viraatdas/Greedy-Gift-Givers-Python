"""
ID: your_id_here
LANG: PYTHON3
TASK: gift1
"""


fin = open ('gift1.txt', 'r')
fout = open ('gift2.txt', 'w')

a = int (fin.readline())

name = []
for i in range(a):
    name.append(fin.readline())


with open('gift1.txt') as f:
   size=sum(1 for _ in f)

money= [0]*a

p = a+2



pg = fin.readline() #person who is giving

for i in range(a):
    if(name[i] == pg):
        mon = fin.readline()
        p = p+1
        mon = mon.split()
        tot = int(mon[0])
        peo = int(mon[1])
        money[i] = money[i] - peo*int(tot/peo)
        for _ in range(peo):
            pr = fin.readline() #person who is receiving
            op= -1
            while (op<a-1):
                op=op+1
                if (pr == name[op]):
                    money[op] = money[op]+int(tot/peo)




pg = pr  #person who is giving

print (money)

for i in range(a):
    if(name[i] == pg):
        mon = fin.readline()
        p = p+1
        mon = mon.split()
        tot = int(mon[0])
        peo = int(mon[1])
        money[i] = money[i] - peo*int(tot/peo)
        for _ in range(peo):
            pr = fin.readline() #person who is receiving
            op= -1
            while (op<a-1):
                op=op+1
                if (pr == name[op]):
                    money[op] = money[op]+int(tot/peo)




pg = pr

for i in range(a):
    if(name[i] == pg):
        mon = fin.readline()
        p = p+1
        mon = mon.split()
        tot = int(mon[0])
        peo = int(mon[1])
        money[i] = money[i] - peo*int(tot/peo)
        for _ in range(peo):
            pr = fin.readline() #person who is receiving
            op= -1
            while (op<a-1):
                op=op+1
                if (pr == name[op]):
                    money[op] = money[op]+int(tot/peo)



print (money)
pg = fin.readline()


for i in range(a):
    if(name[i] == pg):
        mon = fin.readline()
        p = p+1
        mon = mon.split()
        tot = int(mon[0])
        peo = int(mon[1])
        money[i] = money[i] - peo*int(tot/peo)
        for _ in range(peo):
            pr = fin.readline() #person who is receiving
            op= -1
            while (op<a-1):
                op=op+1
                if (pr == name[op]):
                    money[op] = money[op]+int(tot/peo)



pg=fin.readline()



for i in range(a):
    if(name[i] == pg):
        mon = fin.readline()
        p = p+1
        mon = mon.split()
        tot = int(mon[0])
        peo = int(mon[1])
        money[i] = money[i] - peo*int(tot/peo)
        for _ in range(peo):
            pr = fin.readline() #person who is receiving
            op= -1
            while (op<a-1):
                op=op+1
                if (pr == name[op]):
                    money[op] = money[op]+int(tot/peo)




print (pg)


print (money)

