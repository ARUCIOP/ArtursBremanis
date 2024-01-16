
'''def sumOfNums(array):
    res=0
    for num in nums:
        res+=num
    return(res)

nums=[1,2,3,4,5,6]
print(sumOfNums(nums))'''

#ir funkcija kas celsija grādus pārceļ par feranhaitiem
#celsija grādus ievadi pats
sākt = 1
while sākt == 1:
    a = float(input('ievadi grādus celsijā: '))
    def gradi():
        rez = (a*9/5)+32
        print(rez)
    gradi()
    a=str(input('Vai vēlaties turpināt?(j/n):'))
    if a=="j":
        atkārtot=1
    else:
        atkārtot=0
    sākt = atkārtot
else:
    print('attā')