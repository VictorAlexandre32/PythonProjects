import time
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list1 = ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
list1.sort(reverse=True)
for c in range(1, 18):
    print("----------------- {0}ª rodada -----------------".format(c))
    print(list)
    print(list1)
    list[1], list1[0] = list1[0], list[1]
    list1[0], list1[1] = list1[1], list1[0]
    list1[1], list1[2] = list1[2], list1[1]
    list1[2], list1[3] = list1[3], list1[2]
    list1[3], list1[4] = list1[4], list1[3]
    list1[4], list1[5] = list1[5], list1[4]
    list1[5], list1[6] = list1[6], list1[5]
    list1[6], list1[7] = list1[7], list1[6]
    list1[7], list1[8] = list1[8], list1[7]
    list[8], list1[8] = list1[8], list[8]
    list[7], list[8] = list[8], list[7]
    list[6], list[7] = list[7], list[6]
    list[5], list[6] = list[6], list[5]
    list[4], list[5] = list[5], list[4]
    list[3], list[4] = list[4], list[3]
    list[2], list[3] = list[3], list[2]
    time.sleep(3)
