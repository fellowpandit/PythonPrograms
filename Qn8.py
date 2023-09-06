import util
c = float(input('Enter deg C: '))
f = util.cTOf(c)
print(f'{c}deg C = {f}deg F')
f = float(input('Enter def F:'))
print(f, 'deg F =', util.fTOc(f), 'deg F')
