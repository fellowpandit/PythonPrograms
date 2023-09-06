def findLength(ip):
    if ip == '':
        return 0
    return 1+findLength(ip[1:])


def findSmallest(ipl):
    if not ipl:
        return None
    smallest = findSmallest(ipl[1:])
    if smallest is None or ipl[0] < smallest:
        return ipl[0]
    return smallest


ip = input('Enter a sentence: ')
print('Length =', findLength(ip))
ipl = [input('Enter no.s separated bt spaces: ').split()]
# ip_list=eval(input('Enter a list of numbers:'))
print('Smallest =', findSmallest(ipl))
