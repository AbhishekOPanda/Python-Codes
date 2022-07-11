from cs515 import map, reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def add(x, y):
    #Returns x + y
    return x + y
    
def numToBinary(n):
    #The binary representation of the integer n is returned as a string.
    if n == 0: 
        return ''
    elif n % 2 == 0:
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'

def binaryPadder(s):
    #This function returns a binary number with the correct bit length.
    if len(s) >= COMPRESSED_BLOCK_SIZE:
        return s
    else:
        return binaryPadder('0'+s)
    
def binaryToNum(s):
    #The integer that corresponds to the binary representation in s is returned.
    if s == '':
        return 0
    else:
        return binaryToNum(s[0:-1]) *2 + int(s[-1])
    
def compress(S):
    #Returns a new binary string that is the input's run-to-length encoding from a binary string
    
    def compressHelp1(S):
        #Returns the number of times the first integer appears in a row.
        if S == '':
            return 0
        elif len(S) == 1:
            return 1
        elif S[0] == S[1]:
            return 1 + compressHelp1(S[1:])
        else:
            return 1
    
    def compressHelp2(S):
        #Returns a list of the values of the successive integers in order of appearance.
        if S == '':
            return []
        return [compressHelp1(S)] + compressHelp2(S[compressHelp1(S):])

    def compressHelp3(L):
        #Breaks up the numbers so that they don't exceed the maximum run length.
        if L == []:
            return []
        if L[0] > MAX_RUN_LENGTH:
            L[0] = L[0] - MAX_RUN_LENGTH
            return [MAX_RUN_LENGTH, 0] + compressHelp3(L)
        return [L[0]] + compressHelp3(L[1:]) 

    if S == '':
        return ''
    elif S[0] == '1':
        return '0' * COMPRESSED_BLOCK_SIZE + reduce(add, map(binaryPadder, map(numToBinary, compressHelp3(compressHelp2(S)))))
    else:
        return reduce(add, map(binaryPadder, map(numToBinary, compressHelp3(compressHelp2(S)))))


def uncompress(S):
    #Returns S in its original uncompressed form.
    
    def uncompressHelp(n, s):
        if s == '':
            return ''
        elif n == 1:
            return binaryToNum(s[:5]) * '1' + uncompressHelp(0, s[5:])
        elif n == 0:
            return binaryToNum(s[:5]) * '0'+"," + uncompressHelp(1, s[5:])
    
    if S == '':
        return 0
    return uncompressHelp(0, S)

def compression(s):
    #Calculates the compressed string to regular string ratio.
    return len(compress(s))/len(s)
