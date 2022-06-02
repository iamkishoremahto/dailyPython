# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())

# ans=(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (x+y+z) != n))
# print(ans)

# if (x+y+z) != n:
#     print(list([i,j,k] for i in range (x+1) for j in range (y+1) for k in range(z+1)))

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     st= set(arr) 
#     max_num= max(st)
#     st.remove(max_num)
#     max_num= max(st)
#     print(max_num)
#     print(st)
    

from operator import itemgetter
from typing import OrderedDict


if __name__ == '__main__':
    student=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        # ls=[name,score]
        student.append([name,score])
    
        
        
       
    disct1=(dict(student))
    dict2= OrderedDict(sorted(disct1.values()))
    print(dict2)
    # print(dict(student.sort))
    # dicts= dict(student)
