#############################
# LONGEST COMMON SUBSEQUENCE#
#############################
'trobar la seqüència de caràcters seguits més llarga en dues seqüències'
# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y):
    m = len(X)
    n = len(Y)
    # lookup table stores solution to already computed subproblems;
    # i.e., `T[i][j]` stores the length of LCS of substring
    # `X[0…i-1]` and `Y[0…j-1]`
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    # LCS will be the last entry in the lookup table
    return T[m][n]

# Function to return all LCS of substrings `X[0…m-1]`, `Y[0…n-1]`
def LCS(X, Y, m, n, lookup):
 
    # if the end of either sequence is reached
    if m == 0 or n == 0:
        # create a list with one empty string and return
        return ['']
 
    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
 
        # ignore the last characters of `X` and `Y` and find all LCS of substring
        # `X[0…m-2]`, `Y[0…n-2]` and store it in a list
        lcs = LCS(X, Y, m - 1, n - 1, lookup)
 
        # append current character `X[m-1]` or `Y[n-1]`
        # to all LCS of substring `X[0…m-2]` and `Y[0…n-2]`
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (X[m - 1])
 
        return lcs
 
    # we reach here when the last character of `X` and `Y` don't match
 
    # if a top cell of the current cell has more value than the left cell,
    # then ignore the current character of string `X` and find all LCS of
    # substring `X[0…m-2]`, `Y[0…n-1]`
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(X, Y, m - 1, n, lookup)
 
    # if a left cell of the current cell has more value than the top cell,
    # then ignore the current character of string `Y` and find all LCS of
    # substring `X[0…m-1]`, `Y[0…n-2]`
    if lookup[m][n - 1] > lookup[m - 1][n]:
        return LCS(X, Y, m, n - 1, lookup)
 
    # if the top cell has equal value to the left cell, then consider both characters
 
    top = LCS(X, Y, m - 1, n, lookup)
    left = LCS(X, Y, m, n - 1, lookup)
 
    # merge two lists and return
    return top + left

 
# Function to fill the lookup table by finding the length of LCS
# of substring `X` and `Y`
def LCSLength(X, Y, lookup):
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            # if current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
 
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
 
# Function to find all LCS of string `X[0…m-1]` and `Y[0…n-1]`
def findLCS(X, Y):
 
    # lookup[i][j] stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(len(Y) + 1)] for y in range(len(X) + 1)]
 
    # fill lookup table
    LCSLength(X, Y, lookup)
 
    # find all the longest common subsequences
    lcs = LCS(X, Y, len(X), len(Y), lookup)
 
    # since a list can contain duplicates, "convert" it to a set and return
    return set(lcs)
 
 
if __name__ == '__main__':
 
    X = 'ABCBDAB'
    Y = 'BDCABA'
 
    lcs = findLCS(X, Y)
    print(lcs)
#############################
#MAXIMUM LENGTH SNAKE SEQUENCE#
#############################

# Construct maximum length snake sequence from the given tail and `L[]` matrix
def constructPath(L, grid, tail):
 
    (i, j) = tail
    path = [tail]
 
    # start from snake's tail till snake's head
    while L[i][j]:
        if i - 1 >= 0 and L[i][j] - L[i - 1][j] == 1 and abs(grid[i - 1][j] - grid[i][j]) == 1: 
            # si no estic a la primera columna i moure'm cap a la l'esquerra sumo o resto un 1
            path.append((i - 1, j)) # afegeix al camí el número on estic
            i = i - 1 # i resta-li a la i un, volent dir que tirem cap a l'esquerra, estem refent el camí
        elif j - 1 >= 0 and L[i][j] - L[i][j - 1] == 1 and abs(grid[i][j - 1] - grid[i][j]) == 1:
            # si ens trobem que el de sobre és + o - 1, l'afegim a la cua i pugem amunt 
            path.append((i, j - 1))
            j = j - 1
 
    return path

# Function to find the maximum length of snake sequence in a given matrix
def findMaxLengthSnakeSequence(grid):
    # base case
    if not grid or not len(grid):
        return
 
    # `L[i][j]` stores the maximum length of the snake sequence
    # ending at cell (i, j)
    L = [[0 for x in range(len(grid))] for y in range(len(grid))]
    # fem una taula plena de zeros 
    
    # stores the maximum length of the snake sequence
    max_so_far = 0
 
    # Pair to store coordinates of a snake's tail
    tail = None
 
    # process the matrix in a bottom-up fashion
    for i in range(len(grid)):
        for j in range(len(grid)):
            # compare the current cell with the top cell and check the
            # absolute difference
            if i - 1 >= 0 and abs(grid[i - 1][j] - grid[i][j]) == 1:
                L[i][j] = L[i - 1][j] + 1
                if max_so_far < L[i][j]:
                    max_so_far = L[i][j]
                    tail = (i, j)
 
            # compare the current cell with the left cell and check the
            # absolute difference
            if j - 1 >= 0 and abs(grid[i][j - 1] - grid[i][j]) == 1:
                # `L[i][j]` can be non-zero at this point, hence take the maximum
                L[i][j] = max(L[i][j], L[i][j - 1] + 1)
                if max_so_far < L[i][j]:
                    max_so_far = L[i][j]
                    tail = (i, j)
 
    # construct the maximum length snake sequence
    return constructPath(L, grid, tail)
 
 
def printSnakeSequence(grid, path):
    # base case
    if not grid or not len(grid):
        return
 
    print('The maximum length snake sequence ', end='')
    # use reverse range to print the List (from snake's head to tail)
    print(' — '.join([str(grid[x][y]) for x, y in path][::-1]))
    print('The length is', len(path) - 1)
 
 
if __name__ == '__main__':
 
    grid = [
        [7, 5, 2, 3, 1],
        [3, 4, 1, 4, 4],
        [1, 5, 6, 7, 8],
        [3, 4, 5, 8, 9],
        [3, 2, 2, 7, 6]
    ]
 
    path = findMaxLengthSnakeSequence(grid)
    printSnakeSequence(grid, path)