#coding=utf-8

import os, sys, platform

os.system('xdg-open https://chat.whatsapp.com/IAXLQFSJokUK70XtZzeH5D')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf KING64.cpython-311.so KING32.cpython-311.so')

except:

    pass

os.system('rm -rf KING64.cpython-311.so KING32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('KING64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KRS/DATA/main/KRS64.cpython-311.so > KRS64.cpython-311.so') 

        os.system("chmod 777 KING64*")

        import KING64

    else:

        import KING64

elif bit == '32bit':

    if not os.path.isfile('KING32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-KING/DATA/main/KING32.cpython-311.so > KING32.cpython-311.so')

        os.system("chmod 777 KING32*")

        import KING32

    else:

        import KING32

