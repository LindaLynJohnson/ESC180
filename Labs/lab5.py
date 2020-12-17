## Part 1
def list1_start_with_list2(list1, list2):
    if len(list1)>=len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

## Part 2
def match_pattern(list1, list2):
    j = 0
    for i in range(0, len(list1)):
        if i > len(list1) - len(list2) and j == 0:
            return False
        if list1[i] == list2[j]:
            j += 1
            if j == len(list2)-1:
                return True
        else:
            j = 0
    return False

## Part 3
def repeats(list0):
    for i in range(0,len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False

## Part 4

## a
def print_matrix_dim(M):
    #columns x rows
    print(len(M[0]),"x",len(M))

## b
def mult_M_v(M, v):
    if len(M[0]) != len(v):
        return
    rv = [0]*len(M)
    for i in range(len(M)):
        sum = 0
        for j in range(len(M[i])):
            sum += M[i][j] * v[j]
        rv[i] = sum
    return rv

## c
def matrix_mult(M1, M2):
    M3 = []
    if len(M1[0]) != len(M2):
        return
    for i in range (len(M1)):
        M3_row = []    #Makes an empty row
        for j in range(len(M2[0])):
            #print(M1[i],get_column(M2,j))
            M3_row.append(dot_product(M1[i], get_column(M2,j) ) )
        M3.append(M3_row[:])
    return M3

def dot_product(v1,v2):
    product = 0
    for i in range(len(v1)):
        product += v1[i] * v2[i]
    return product

def get_column(M, column):
    c  = []
    for i in range(len(M)): #for each row
        c.append(M[i][column]) #get the value in the column from that row
    return c

if __name__ == '__main__':
    list1, list2=[1,2,3,4,5], [1,2,3,4]
    list0=[1,2,2,3]
    M = [[5, 4, 7], [0, -3, 5]]
    v = [1, 2, 3]
    M1=[[1,0], [0,1]]
    M2=[[2,3], [1,0]]
    print(list1_start_with_list2(list1, list2))
    print(match_pattern(list1,list2))
    print(repeats(list0))
    print_matrix_dim(M)
    print(mult_M_v(M, v))
    print(get_column(M2,0))
    print(matrix_mult(M1,M2))