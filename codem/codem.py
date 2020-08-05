import barcode 
import qrcode
from functions import *
try:
    print(
    ''' 
    Select an option:

    [1] QR code      [2] Barcode
    ''')
    #QR CODE SETUP
    command = input('> ') 
    if command == '1':
        data = input('Put your Data: ') 
        qr=qrcode.make(data)
        filename=input('Enter Filename: ')
        qr.save(filename)
    #BARCODE SETUP
    elif command == '2':
        print('''
    [1] EAN-8       [2] EAN-13         [3] EAN-14
    [4] UPC-A      [5] JAN             [6] ISBN-10
    [7] ISBN-13   [8] ISSN         [9] Code 39
    [x] Code 128    [*] PZN 
    ''')
        barcode_func()
    else:
        print('WRONG COMMAND ENTERED')
except KeyboardInterrupt:
    print('''Shutting down
     ____   ____     ___     ____     __    __
    |      |    |   |    |  |        |  |  |  |
    |      |    |   |    |  |----    |  |__|  |
    |____  |____|   |____|  |____    |        | ''')
except TypeError:
    print('Choose  a correct Barcode Class')

