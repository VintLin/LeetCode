'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
'''
def singNum(N):
    for i in range(len(N)-1):
        print('i:', i)
        for j in range(len(N)-1, i, -1):
             print('j',j)
             if(N[i] == N[j]):
                 N[i] = N[0]
                 N[j] = N[0]
                 print('i:'+str(i)+'j:'+str(j))
                 print('[i]:'+str(N[i])+'[j]:'+str(N[j]))
                 break
             elif(i != 0 and N[i] == N[0]):
                 break
             elif(j == i+1):
                 print(j)
                 return N[i]
    return N[len(N) - 1] 

