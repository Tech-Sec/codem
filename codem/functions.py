import barcode 
def barcode_func():
    barcode_classes = {
        '1':'ean8',
        '2':'ean13',
        '3':'ean14',
        '4':'upca',
        '5':'jan',
        '6':'isbn10',
        '7':'isbn13',
        '8':'issn',
        '9':'code39',
        'x':'code128',
        '*':'pzn',
    }
    output = ''
    barcode_class = input('Select a Barcode Class: ')
    for option in barcode_class:
        output+=barcode_classes.get(option)+''
    br = barcode.get_barcode_class(output)
    barcode_data= input('Put your Barcode Number: ')
    barcode_ean8 =br(barcode_data)
    barcode_save_name = input('Put your filename: ')
    barcode_ean8.save(barcode_save_name)


