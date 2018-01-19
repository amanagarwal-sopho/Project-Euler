import re
REGEX_NAME = re.compile(r'"(\w+)"')

def readfile():
    file = open('names.txt','r')
    return sorted(file.read().replace('"','').split(','))
    
def alphavalue(name):
    val = 0
    letters = [i for i in name]
    for letter in letters:
        val += ord(letter) - 64
    return val
    
def totalnamescore(names):
    sum = 0
    for name in names :
        sum += alphavalue(name) * (names.index(name)+1)
    return sum

def main():
    names = readfile()
    print(totalnamescore(names))
    

if __name__=='__main__':
    main()
            
        
        
    

        
    