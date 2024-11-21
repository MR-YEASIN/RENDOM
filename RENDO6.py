#coding=utf-8

import os, sys, platform

os.system('xdg-open https://www.facebook.com/profile.php?id=100049277964296')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf RENDOM64.cpython-311.so RENDOM32.cpython-311.so')

except:

    pass

os.system('rm -rf RENDOM64.cpython-311.so RENDOM32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '32bit':

    if not os.path.isfile('RENDOM32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/MR-YEASIN/DATA/main/RENDOM64.cpython-311.so > RENDOM32.cpython-311.so') 

        os.system("chmod 777 RENDOM64*")
        
        import RENDOM64

    else:

        import RENDOM32

elif bit == '32bit':

    if not os.path.isfile('RENDOM32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/MR-YEASIN/DATA/main/RENDOM32.cpython-311.so > RENDOM32.cpython-311.so')

        os.system("chmod 777 RENDOM32*")

        import RENDOM32

    else:

        import RENDOM32
