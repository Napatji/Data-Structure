def alphabetSort(inp):
    temp = []
    length = len(inp)
    for i in range(length):
        least = getLeast(inp)
        inp.pop(inp.index(least))
        temp.append(least)    
    for i in temp:
        print(i,end=' ')

def getLeast(inp):
    least = inp[0]
    for i in inp:
        if findAlphabetAscii(least) > findAlphabetAscii(i):
            least = i
    return least
        
def findAlphabetAscii(str):
    num = ['1','2','3','4','5','6','7','8','9']
    for i in str:
        if i not in num:
            return ord(i)

if __name__ == '__main__':
    inp = input('Enter Input : ').split(' ')
    alphabetSort(inp)