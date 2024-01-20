import sys

def factors(file):
    with open(file, 'r') as f:
        for line in f:
            n = int(line.strip())
            for i in range(2, n):
                if n % i == 0:
                    print(f'{n}={i}*{n//i}')
                    break

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
    else:
        factors(sys.argv[1])
