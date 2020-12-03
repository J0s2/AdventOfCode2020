import pandas as pd
import sys

def tocsv(input_file):


    filename = input_file

    with open(filename, 'r') as f: 
    
        contenido = f.read()
        contenido = contenido.replace('-', ',').replace(' ',',').replace(':', '')

    cabecera = 'rango_min,rango_max,letra,password\n'

    filename_new = 'passwords.csv'

    with open(filename_new,'w') as passwords:
    

        passwords.write(cabecera)
        passwords.write(contenido)

    f.close()

    return 'passwords.csv'

    

def check_password(row):

    if row['rango_min'] <= row['password'].count(row['letra']) <= row['rango_max']:
        return 1
    else:
        return 0

    
def check_password2(row):

    posicion1 = row['rango_min'] - 1
    posicion2 = row['rango_max'] - 1

    if (row['password'][posicion1] == row['letra'] and row['password'][posicion2] != row['letra']) or \
       (row['password'][posicion1] != row['letra'] and row['password'][posicion2] == row['letra']):
        return 1
    else:
        return 0


passwords_file = tocsv('input.txt')

df = pd.read_csv(passwords_file)


df['check_password'] = df.apply(check_password, axis=1)
df['check_password2'] = df.apply(check_password2, axis = 1)

print('****************************************')
print('Solución 1: ', df['check_password'].sum())
print('Solución 2: ', df['check_password2'].sum())
print('****************************************')
