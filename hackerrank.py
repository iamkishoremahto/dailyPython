# if __name__ == '__main__':
    # student=[]
    # for i in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     student.append([name,score])
    # dict_student=(dict(student))
    # min_val=(min(dict_student.values()))
    # lowlist= [key for key in dict_student if dict_student[key] == min_val]
    # print(lowlist)
    # for key in lowlist:
    #     dict_student.pop(key)
    # min_val=(min(dict_student.values()))
    # lowlist= [key for key in dict_student if dict_student[key] == min_val]

    # lowlist.sort()
    # for item in lowlist:
    #     print(item)

    # if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    # popitem= student_marks.pop(query_name)
    # # mark= ([mark for mark in student_marks if student_marks[name] == query_name])
    # # print(student_marks)
    # avg=(sum(popitem)/len(popitem))
    # print("{:.2f}".format(avg))
    # # print(mark)

def minion_game(string):
    str1=string
    vowels=[]
    cons= []
    vowel_list=[]
    for i in range(len(str1)):
        if "A" in str1[i] or "E" in str1[i] or "I" in str1[i] or "O" in str1[i] or "U" in str1[i] or "a" in str1[i] or "e" in str1[i] or "i" in str1[i] or "o" in str1[i] or "u" in str1[i]:
            vowels.append(str1[i])
        else:
            cons.append(str1[i])
    for j in range(len(vowels)):
        vowel_list.append(vowels[j])
        for k in range(len(cons)):
            str2=vowels[j]
            str2= str2+cons[k]
            vowel_list.append(str2)
    print(vowels)
    print(cons)
    print(vowel_list)
if __name__ == '__main__':
    minion_game("Banana")
