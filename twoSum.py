nu= [2, 3, 7, 9]
t= 11
def twsm(self, nums, target):
    for i in nums:
        x= target-i
        if x in nums:
            nums.append(i)
    return nums

#compplete the code this code is wrong