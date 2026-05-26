def check_investment(i,j,k):
val=i*(1+j)**k
if val>10000:
print("high return")
else:
print("low return")
return val
