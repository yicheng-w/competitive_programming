def get_list_type(l):
    ascending = l[1] > l[0]
    for i in range(2, len(l)):
        #print(i)
        if (ascending):
            if l[i] < l[i - 1]:
                return "NEITHER"
        else:
            if l[i] > l[i - 1]:
                return "NEITHER"
    if ascending:
        return "INCREASING"
    else:
        return "DECREASING"

if __name__ == '__main__':
    count = int(input())
    while (count):
        names = []
        for i in range(0, count):
            names.append(input())
        #print(names)
        print(get_list_type(names))
        a = input()
        if a == '':
            count = 0
        else:
            count = int(a)
