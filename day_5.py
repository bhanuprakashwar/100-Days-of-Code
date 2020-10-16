import string,random,time
#input=['a','b','c','a','b','a','a','c','c']
start_time = time.time()
input=[]
for i in range(0,1000000):
    alphabet = string.ascii_lowercase
    rdm_index = random.randrange(0,25)
    input.append(alphabet[rdm_index])
def sorting(input):
    #input.sort()
    n=len(input)
    for i in range(0,n-1):
        if input[i] != input[i+1]:
            continue
        else:
            if i+2 == n:
                return 'None'
            for j in range(i+2,n):
                if input[j] != input[i+1]:
                    input[i+1],input[j] = input[j],input[i+1]
                    break
    return 'sorted'
print(sorting(input))
end_time = time.time()
print(str(end_time - start_time) + "s")
