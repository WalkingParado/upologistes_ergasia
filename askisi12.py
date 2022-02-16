import requests


r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
num = data["round"]

lol={}
lp = ""
count1 = 0
max1 = 0
count2 = 0
max2 = 0

for i in range(0,100):
   l = requests.get(" https://drand.cloudflare.com/public/"+str(num-i))
   lol[i] = l.json()
   b = bin(int(lol[i]["randomness"],16))
   lp += str(b)

bo = len(lp)

for i in range(1,bo):
   if (lp[i-1] == "1") and (lp[i] == "1"):
      count1 += 1
      if count1>max1:
         max1=count1
   else:
      count1=0

for i in range(1,bo):
   if (lp[i-1] == "0") and (lp[i] == "0"):
      count2 += 1
      if count2>max2:
         max2=count2
   else:
      count2=0

print("The max number of repeating ones is")
print(str(max1+1))
print("The max number of repeating zeroes is")
print(str(max2+1))


















