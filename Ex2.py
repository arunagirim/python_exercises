import itertools 
# s='infosys@337'
# s='Hello#81@21349'
s=input()
ss=set()
for i in s:
	if i.isdigit():
		ss.add(i)
m=-1
l=list(itertools.permutations(ss,len(ss)))
for j in l:
	k=''.join(j)
	if int(k)%2==0 and int(k)>m:
		m=int(k)
print(m)
