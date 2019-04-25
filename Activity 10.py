print ("0. The student number is 14369852")

number = 14369852
count = 0
for x in "14369852":
    isPrime = True
    # print("Checking ", x)
    if int(x) > 1:
        for num in range (2, int(x)):
                if int(x) % num == 0:
                    isPrime = False
                    # print (x, " is not a prime")
                    break
    else:
        isPrime = False
    if isPrime:
        count +=1
print ("1. The amount of prime numbers is: ", count)

import random
ranNum = random.randint(25,50)
print ("2. The Random number is: ", ranNum)

import math
dividNum = math.floor(ranNum/count)
print ("3. The number of strings to be generated is: ", dividNum)


print  ("4. List of strings")
print  ("=========================")
import string

alphabet = string.ascii_lowercase
stringList = []
stCount = 0
for st in range (0, dividNum):
    word = ""
    if stCount % 2 != 0:
        letters = 7
    else:
        letters = 5
    word = "".join(random.choice(alphabet)for i in range(letters))
    stringList.append(word)
    stCount += 1
    print (stCount, " - ", word, "(", letters,")")
print  ("=========================")

vAmount = []
vowels = ["a", "e", "i", "o", "u"]
for x in stringList:
    vCount = 0
    for let in x:
        for v in vowels:
            if let == v:
                vCount+=1
                break
    vAmount.append(vCount)

zipped = zip(VAmount, stringList)
# z =[x for_ x in sorted(zipped)]
# print(z)