def binary_search(list, element):
    middle = 0
    start =0 
    end = 0 
    steps = 0 

    while(start<=end):
        print("Step",steps,":",str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element== list[middle]:
            return middle
        elif element== list[middle]:
            end = middle -1
        else:
            start = middle +1

    return -1






