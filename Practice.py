list = []
x = int(input ("enter: "))
y = str(x)
idx = 0
while idx < len(y):
    z= y[idx]
    list.append(z)
    idx += 1

num2 = list.copy()
num2.reverse()
if (list == num2):
    print ("palindrome")
else: print ("not palindrome")