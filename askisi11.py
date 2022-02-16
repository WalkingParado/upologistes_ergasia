import requests
import math


r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
num = data["round"]

lol = {}
lp = " "
S=0


for i in range(0,20):
   l = requests.get(" https://drand.cloudflare.com/public/"+str(num-i))
   lol[i] = l.json()
   lp += str(hex(int(lol[i]["randomness"],16)))



for o in range(0,10):
   count1 = lp.count(str(o))
   k = (count1/(len(lp) - 20))
   S -= k * math.log(k, 2)

for u in range(ord('a'),ord('g')):
    count2 = lp.count(chr(u))
    y = (count2/(len(lp)-20))
    S -= y * math.log(y, 2)

print("The latest random data is")
print(data)
print("The entropy of the last 20 rounds of random numbers is:")
print(lp)
print(S)

























