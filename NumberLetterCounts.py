def write_numbers(N):
   if N < 0:
      return -1
   
   numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]

   if N <= 15:
      return numbers[1:N+1]

   for i in range(6,10):
      numbers.append(numbers[i] + "teen")

   if N < 20:
      return numbers[1:N+1]

   numbers.append("twenty")

   for i in range(1,10):
      numbers.append(numbers[20] + numbers[i])

   if N < 30:
      return numbers[1:N+1]

   numbers.append("thirty")

   for i in range(1,10):
      numbers.append(numbers[30] + numbers[i])

   if N < 40:
      return numbers[1:N+1]

   numbers.append("forty")

   for i in range(1,10):
      numbers.append(numbers[40] + numbers[i])

   if N < 50:
      return numbers[1:N+1]

   numbers.append("fifty")

   for i in range(1,10):
      numbers.append(numbers[50] + numbers[i])

   if N < 60:
      return numbers[1:N+1]

   numbers.append("sixty")

   for i in range(1,10):
      numbers.append(numbers[60] + numbers[i])

   if N < 70:
      return numbers[1:N+1]

   numbers.append("seventy")

   for i in range(1,10):
      numbers.append(numbers[70] + numbers[i])

   if N < 80:
      return numbers[1:N+1]

   numbers.append("eighty")

   for i in range(1,10):
      numbers.append(numbers[80] + numbers[i])

   if N < 90:
      return numbers[1:N+1]

   numbers.append("ninety")

   for i in range(1,10):
      numbers.append(numbers[90] + numbers[i])

   if N < 100:
      return numbers[1:N+1]

   numbers.append("onehundred")

   for i in range(1,100):
      numbers.append(numbers[100] + "and" + numbers[i])

   if N < 200:
      return numbers[1:N+1]

   numbers.append("twohundred")

   for i in range(1,100):
      numbers.append(numbers[200] + "and" + numbers[i])

   if N < 300:
      return numbers[1:N+1]

   numbers.append("threehundred")

   for i in range(1,100):
      numbers.append(numbers[300] + "and" + numbers[i])

   if N < 400:
      return numbers[1:N+1]

   numbers.append("fourhundred")

   for i in range(1,100):
      numbers.append(numbers[400] + "and" + numbers[i])

   if N < 500:
      return numbers[1:N+1]

   numbers.append("fivehundred")

   for i in range(1,100):
      numbers.append(numbers[500] + "and" + numbers[i])

   if N < 600:
      return numbers[1:N+1]

   numbers.append("sixhundred")

   for i in range(1,100):
      numbers.append(numbers[600] + "and" + numbers[i])

   if N < 700:
      return numbers[1:N+1]

   numbers.append("sevenhundred")

   for i in range(1,100):
      numbers.append(numbers[700] + "and" + numbers[i])

   if N < 800:
      return numbers[1:N+1]

   numbers.append("eighthundred")

   for i in range(1,100):
      numbers.append(numbers[800] + "and" + numbers[i])

   if N < 900:
      return numbers[1:N+1]

   numbers.append("ninehundred")

   for i in range(1,100):
      numbers.append(numbers[900] + "and" + numbers[i])

   if N < 1000:
      return numbers[1:N+1]

   numbers.append("onethousand")

   if N == 1000:
      return numbers[1:N+1]
   

thousand_numbers = write_numbers(int(input("Count up-to ? ")))
print(thousand_numbers)

letters = 0

for number in thousand_numbers:
   letters += len(number)

print(letters)
input()
