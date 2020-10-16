from collections import defaultdict
import heapq,string,random,time
start_time = time.time()
input=[]
for i in range(0,100000):
    alphabet = string.ascii_lowercase
    rdm_index = random.randrange(0,25)
    input.append(alphabet[rdm_index])
def rearrage(string):
    frequencies =defaultdict(int)
    for letter in string:
        frequencies[letter]+=1
    heap=[]
    for char, count in frequencies.items():
        heapq.heappush(heap,(-count,char))
    count,char =heapq.heappop(heap)
    result=[char]
    while heap:
        last = (count+1,char)
        count,char =heapq.heappop(heap)
        result.append(char)
        
        if last[0]<0:
            heapq.heappush(heap,last)
    if len(result) == len(string):
        return 'sorted'
    else :
        return None

print(rearrage(input))
end_time = time.time()
print(str(end_time - start_time) + "s")
