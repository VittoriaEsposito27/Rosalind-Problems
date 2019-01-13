def fib(n,k):
   ditt = [(0,1),(1,0)]
   for i in range (n-2):
       t=ditt[-1]
       a,b=t
       new=(a+b,a*k)
       ditt.append(new)
   c,d=ditt[-1]
   res=c+d
   return res


print(fib(36,2))
