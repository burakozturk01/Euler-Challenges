import math as m

def isAbundant(num):
   summ = 0

   for i in range(2, m.ceil(m.sqrt(num)) + 1):
      if num % i == 0:
         summ += i + num / i
         
   return summ > num

# Can it be written as sum of two abundants
def canAbundant(num, abundants):
   for ab in abundants:
      if (num - ab) in abundants:
         return True
   return False

abundants = [i for i in range(12, 28124) if isAbundant(i)]
print(len(abundants))

i = 1
summ = 0

j = 0
subAbun = []
while i < 28123:
   while j < len(abundants) and abundants[j] <= i:
      subAbun.append(abundants[j])
      print(i, abundants[j])
      j += 1
   if not canAbundant(i, subAbun):
      summ += i
      print(i, summ)
   i += 1
