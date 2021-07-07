import sys
from module import encode

if __name__ == '__main__':
    text = sys.argv[1]
    delimiter = ' '
    # Checks if the delimiter exist in the prompt
    if len(sys.argv) > 2:
        delimiter = sys.argv[2]

    result = encode(text, delimiter=delimiter)

    print(result)
