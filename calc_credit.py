inflation_value = [1.59282448436825, -0.453509101198007, 2.32467171712441,
1.26125440724877, 1.78252628571251, 2.32938454145522, 1.50222984223283,
1.78252628571251, 2.32884899407637, 0.616921348207244, 2.35229588637833,
0.337779545187098, 1.57703524727525, -0.292781442607648, 2.48619659017508,
0.267110317834564, 1.41795267229799, 1.05424326726375, 1.4805201044812,
1.57703524727525, -0.077420690314702, 1.16573339872354, -0.404186717638335,
1.49970852083123]
month = ['styczniu', 'lutym', 'marcu', 'kwietniu', 'maju', 'czerwcu', 'lipcu',
'sierpniu', 'wrześniu', 'październiku', 'listopadzie', 'grudniu']*2

try:
 credit = float(input('Podaj początkową wysokość kredytu: '))
 percent = float(input('Podaj wysokość oprocentowania: '))
 installment = float(input('Podaj wartość raty: '))
except:
    print('Jedna z wartości jest ujemna, zerowa lub jest tesktem!')
    quit()

for i in range(24):
   calc = (1+((inflation_value[i]+percent)/1200))*credit-installment
   calc_less = credit-calc
   credit = calc
   print(f'W {month[i]} twoja pozostała kwota kredytu to {calc}' +
   f'to {calc_less} mniej niz w poprzednim miesiącu \n')
