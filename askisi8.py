import random

def chesspie(l, k):
  count1=0
  count2=0
  for i in range(100):
   board = [['-' for i in range(k)] for i in range(l)]
   r1 = random.randint(0, l-1)
   r2 = random.randint(0, k-1)
   r3 = random.randint(0, l-1)
   r4 = random.randint(0, k-1)
   while (r1 == r3) and (r2 == r4):
           r3 = random.randint(0, l-1)
           r4 = random.randint(0, k-1)
   board[r1][r2] = 'T'
   board[r3][r4] = 'B'
   if (r1==r3) or (r2==r4):
           count1+=1
   if (r1 - r3 == r2 - r4) or (-abs(r1) + r3 == r2 - r4):
           count2+=1
  return count1,count2

print("The wins of towers and bishops are " + str(chesspie(8, 8)))
print("The wins of towers and bishops are " + str(chesspie(7, 7)))
print("The wins of towers and bishops are " + str(chesspie(7, 8)))





