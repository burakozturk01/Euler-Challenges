charscores = { "A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,
               "F": 6,  "G": 7,  "H": 8,  "I": 9, "J": 10,
               "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
               "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
               "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
             }

def wordscore(word):
   score = 0
   for char in word:
      score += charscores[char]
   return score

def partition(start, end, array):
   pivot_index = start
   pivot = array[pivot_index]

   while start < end:
      while start < len(array) and array[start] <= pivot:
         start += 1
      while array[end] > pivot:
         end -= 1
      if start < end:
         array[start], array[end] = array[end], array[start]
         
   array[end], array[pivot_index] = array[pivot_index], array[end]

   return end

def strsort(start, end, array):
   if start < end:
      p = partition(start, end, array)

      strsort(start, p - 1, array)
      strsort(p + 1, end, array)

f = open("names.txt", "r")
names = f.read().split(",")
f.close()
names = [n.split("\"")[1] for n in names]

strsort(0, len(names)-1, names)

score = sum([wordscore(names[i])*(i+1) for i in range(len(names))])

print(score)
input()
