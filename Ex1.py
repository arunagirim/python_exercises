# l=[3,2,6,5,1,4,8,9]
l=list(map(int,input().split(',')))
num1=sum(l[:l.index(5)])+sum(l[l.index(8)+1:])
print(num1)
s=l[l.index(5):l.index(8)+1]
num2=''
for i in s:
	num2+=str(i)
print(num2)
print(num1+int(num2))
