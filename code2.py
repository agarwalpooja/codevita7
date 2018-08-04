import numpy
dic={
    1:'AAA',
    2:'BBB',
    3:'Others',
}
q=[]
#print(dic[1])
n,m = input().strip(' ').split(' ')
n = int(n)
m= int(m)
a = [[0]*m for _ in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]
#print(a)
if(n<m):
    c= n
else:
    c=m
for b in range(2,c):
    if(n%b==0 and m%b ==0):
        q.append(b)
q= numpy.array(q)        
b = numpy.max(q)
#print(b)
d=int((n*m)/(b*b))
#print(d)
a=numpy.array(a)
a1=[]
cc=0
dd=0
nb= n/ b
mb= m/b
for i in range(int(nb)):
    
    for j in range(int(mb)):
        print([x[cc:cc+b] for x in a[dd:dd+b]])
        dd=dd+b
        cc=cc+b
        
    #     sp=a[0:2][0:2]
    #     print(sp)
    #     a1.append(sp)
    # cc=cc+b
# a1 = numpy.split(a,d,axis=1) 
print(a1)
cm=[]
print(len(a1))
for i in range(len(a1)):
    c1=[0,0,0,0]
    for j in range(len(a1[i])):
        if(a1[i][j]== 1):
            c1[1] =c1[1]+1
        elif(a1[i][j]==2):
            c1[2] = c1[2]+1
        elif(a1[i][j]==3):
            c1[3]=c1[3]+1
    cm.append(numpy.argmax(numpy.array(c1)))
print(cm)
# c2=numpy.array([0,0,0,0])
# for j in range(len(cm)):
#     if(cm[j]== 1):
#         c2[1] =c2[1]+1
#     elif(cm[j]==2):
#         c2[2] = c2[2]+1
#     elif(cm[j]==3):
#         c2[3]=c2[3]+1
# ref=numpy.argmax((numpy.array(c2))
#c1 = numpy.array(c1)
# # str= " InitialMajorityParty:Seats = {}:{} "
# # print(str.format(dic[ref],numpy.max(c2)))

# # h = int(input().strip(' '))
# # for i in range(h):
# #     x,y,z = input().strip(' ').split(' ')
# #     #print(x+y+z)
# max= numpy.max(c2)