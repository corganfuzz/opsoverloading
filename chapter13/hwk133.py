import os

if __name__ == "__main__":
    filename = input('Enter a filename: ')
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            scores = [int(n) for n in f.read().split()]
            total = sum(scores)
            average = total / len(scores)
            f.closed
            print('There are {} scores'.format(len(scores)))
            print('The total is {}'.format(total))
            print('The average is {}'.format(average))
    else:
        print('File "{}" does not exist!'.format(filename))
