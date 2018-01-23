def increasing(L):
    final_result = []
    temp_result = []
    temp_pos = 1
    counter = 1
    for i in range(len(L)):
        if len(temp_result) == 0:
            temp_result = [L[i]]
            temp_suma = L[i]
        else:
            if L[i] >= L[i-1]:
                temp_result.append(L[i])
                temp_suma += L[i]
            else:
                if len(temp_result) > len(final_result):
                    final_result = temp_result
                    temp_result = [L[i]]
                    final_pos = temp_pos
                    temp_pos = counter
                    suma = temp_suma
                    temp_suma = L[i]
                else:
                    temp_result = [L[i]]
                    temp_pos = counter
                    temp_suma = L[i]
        counter += 1
    if len(temp_result) > len(final_result):
        final_result = temp_result
        temp_result = [L[i]]
        final_pos = temp_pos
        temp_pos = counter
        suma = temp_suma
        temp_suma = L[i]       
    return [final_result, final_pos, suma]

def decreasing(L):
    final_result = []
    temp_result = []
    temp_pos = 1
    counter = 1
    for i in range(len(L)):
        if len(temp_result) == 0:
            temp_result = [L[i]]
            temp_suma = L[i]
        else:
            if L[i] <= L[i-1]:
                temp_result.append(L[i])
                temp_suma += L[i]
            else:
                if len(temp_result) > len(final_result):
                    final_result = temp_result
                    temp_result = [L[i]]
                    final_pos = temp_pos
                    temp_pos = counter
                    suma = temp_suma
                    temp_suma = L[i]
                else:
                    temp_result = [L[i]]
                    temp_pos = counter
                    temp_suma = L[i]
        counter += 1
    if len(temp_result) > len(final_result):
        final_result = temp_result
        temp_result = [L[i]]
        final_pos = temp_pos
        temp_pos = counter
        suma = temp_suma
        temp_suma = L[i]
    return [final_result, final_pos, suma]

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    incr = increasing(L)
    decr = decreasing(L)
    if len(incr[0]) > len(decr[0]):
        return incr[2]
    elif len(incr[0]) < len(decr[0]):
        return decr[2]
    else:
        if incr[1] < decr[1]:
            return incr[2]
        else:
            return decr[2]
        
print(longest_run([1, 2, 3, 2, -1]))    