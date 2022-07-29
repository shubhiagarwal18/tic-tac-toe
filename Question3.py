n = int(input("Enter the value of n: "))
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
            
#print(NumGenerator(n))
#print(vall)
l = []
s= ""
for number in NumGenerator(n):
	l.append(number)
for i in l :
    s = s + str(i) + ","
print(s[:-1])