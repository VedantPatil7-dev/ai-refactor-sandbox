def compute(q,w):
res=q*0.18
final=q+res-w
if final>500:
print("limit exceeded")
else:
print("ok status")
return final
