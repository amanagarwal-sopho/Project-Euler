import re
import time
REGEX = re.compile(r'"(\w+)"')

def read_file():
    with open('p042_words.txt') as file:
        for line in file:
            words = REGEX.findall(line)
    return words

def word_value(word):
    sum = 0
    for item in list(word):
        sum += ord(item.upper()) - 64

    return sum

def is_triangular_word(word):
    value = word_value(word)
    x = -1 + (8 * value + 1) ** 0.5
    return x%2 == 0

def main():
    count = 0
    words = read_file()
    for word in words:
        if is_triangular_word(word):
            count += 1

    print(count)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)