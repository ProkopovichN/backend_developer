import openpyxl
import array
d = dict()

s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []
s10 = []
s11 = []
s12 = []


d['STU_ID'] = s1
d['FIO'] = s2
d['BIRTHDATE'] = s3
d['SEX'] = s4
d['EMAIL'] = s5
d['FACULTY'] = s6
d['FORBUCH'] = s7
d['URPODG'] = s8
d['KURS'] = s9
d['FINANCE_SOURCE'] = s10
d['CITIZEN'] = s11
d['NUMBER'] = s12

list = openpyxl.open("Sample.xlsx",read_only=False)

s = list.active

len_s = s.max_row

for col in range(2, len_s + 1):
        d['STU_ID'].append(s[col][0].value)
        d['FIO'].append(s[col][1].value)
        d['BIRTHDATE'].append(str(s[col][2].value)[:-8])
        d['SEX'].append(s[col][3].value)
        d['EMAIL'].append(s[col][4].value)
        d['FACULTY'].append(s[col][5].value)
        d['FORBUCH'].append(s[col][6].value)
        d['URPODG'].append(s[col][7].value)
        d['KURS'].append(s[col][8].value)
        d['FINANCE_SOURCE'].append(s[col][9].value)
        d['CITIZEN'].append(s[col][10].value)
        d['NUMBER'].append(s[col][11].value)

print('Список всей базы данных')
print('STU_ID' + ' ' + 'FIO' + ' ' * 31 + 'BIRTHDATE' + ' ' * 3 + 'SEX' + ' ' * 6 + 'EMAIL' + ' ' * 28 + 'FACULTY' + ' ' * 2 + 'FORBUCH' + ' ' * 7 + 'URPODG' + ' ' * 36 + 'KURS' + ' ' * 2 + 'FINANCE_SOURCE' + ' ' * 12 + 'CITIZEN' + ' ' * 15 + 'NUMBER')
for i in range(0, len_s-1):
        print(str(d['STU_ID'][i]) + ' ' + str(d['FIO'][i]).ljust(34,' ') + str(d['BIRTHDATE'][i]) + ' ' + str(d['SEX'][i]) + ' ' * 2 + str(d['EMAIL'][i]).ljust(33, ' ') + str(d['FACULTY'][i]).ljust(9, ' ') + str(d['FORBUCH'][i]).ljust(14, ' ') + str(d['URPODG'][i]).ljust(42, ' ') + str(d['KURS'][i]).ljust(6, ' ') + str(d['FINANCE_SOURCE'][i]).ljust(26, ' ') + str(d['CITIZEN'][i]).ljust(22, ' ') + str(d['NUMBER'][i]))

print()
n = 1
a = 'CITIZEN'
b = 'Российская Федерация'
while(n <= 2):
    print('Пример ' + str(n))
    print('Параметры - ' + a + ':' + b)
    print('STU_ID' + ' ' + 'FIO' + ' ' * 31 + 'BIRTHDATE' + ' ' * 3 + 'SEX' + ' ' * 6 + 'EMAIL' + ' ' * 28 + 'FACULTY' + ' ' * 2 + 'FORBUCH' + ' ' * 7 + 'URPODG' + ' ' * 36 + 'KURS' + ' ' * 2 + 'FINANCE_SOURCE' + ' ' * 12 + 'CITIZEN' + ' ' * 15 + 'NUMBER')
    for i in range(0, len(d[a])):
        if (d[a][i] == b):
            print(str(d['STU_ID'][i]) + ' ' + str(d['FIO'][i]).ljust(34,' ') + str(d['BIRTHDATE'][i]) + ' ' + str(d['SEX'][i]) + ' ' * 2 + str(d['EMAIL'][i]).ljust(33, ' ') + str(d['FACULTY'][i]).ljust(9, ' ') + str(d['FORBUCH'][i]).ljust(14, ' ') + str(d['URPODG'][i]).ljust(42, ' ') + str(d['KURS'][i]).ljust(6, ' ') + str(d['FINANCE_SOURCE'][i]).ljust(26, ' ') + str(d['CITIZEN'][i]).ljust(22, ' ') + str(d['NUMBER'][i]))
    a = 'FACULTY'
    b = 'ИКТИБ'
    n += 1
    print()
