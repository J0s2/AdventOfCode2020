import os

def leerDatos():

    filename = 'Day 4/input.txt'

    passports = {}

    with open(filename, 'r') as f: 

        pos = 0
        passports[pos] = {}

        for line in f.readlines():

            
            datos = line.split()

            for dato in datos:

                clave, valor = dato.split(':')
                passports[pos].update({clave: valor})
                
                
            if line == '\n':
                pos += 1
                passports[pos] = {}


    return passports

def check_keys(passport):

    if  'byr' in passport.keys() and \
        'iyr' in passport.keys() and \
        'eyr' in passport.keys() and \
        'hgt' in passport.keys() and \
        'hcl' in passport.keys() and \
        'ecl' in passport.keys() and \
        'pid' in passport.keys():

        return True

    else:

        return False



def check_passport1(passport: dict):

    if  check_keys(passport):
        

        return 1

    else:

        return 0

def check_byr(byr:str):

    if 1920 <= int(byr) <= 2002:
        
        return True

    else:

        return False


def check_iyr(iyr:str):

    if 2010 <= int(iyr) <= 2020:
        
        return True

    else:

        return False

def check_eyr(eyr:str):

    if 2020 <= int(eyr) <= 2030:
        
        return True

    else:

        return False

def check_hgt(hgt:str):

    if (hgt.endswith('cm') and 150 <= int(hgt[0:hgt.index('c')]) <= 193) or (hgt.endswith('in') and 59 <= int(hgt[0:hgt.index('i')]) <= 76):
       
        return True

    else:

        return False
        
        


def check_color(hcl:str):

    import re

    if re.search('#[0-9a-f]{6}', hcl):

        return True

    else:


        return False

def check_ecl(ecl:str):

    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:

        return True

    else:

        return False


def check_pid(pid:str):

    

    if len(pid) == 9 and pid.isdigit():

        return True

    else:

        return False

def check_passport2(passport: dict):

    

    if  check_keys(passport) and  check_byr(passport['byr']) and check_iyr(passport['iyr']) and check_eyr(passport['eyr']) \
        and check_hgt(passport['hgt']) and check_color(passport['hcl']) and check_ecl(passport['ecl']) and check_pid(passport['pid']):

        return 1

    else:

        return 0


def main():

    passports = leerDatos()

    valid_passports = 0

    for passport in passports.keys():
        
        valid_passports = valid_passports + check_passport2(passports[passport])

    print('Valid passports: ', valid_passports)

main()


