def sumofdivisors(num):
   sod = 1
   
   limit = int(num / 2)

   if num % 2 != 0:
      limit = int(num / 3)

   for i in range(2, limit+1):
      if num % i == 0:
         sod += i

   return sod

def is_amicable(a):
   sod = sumofdivisors(a)
   return sumofdivisors(sod) == a and a != sod

amics = []

for i in range(1, 10000):
      if is_amicable(i):
         amics.append(i)

print(sum(amics))
input()
