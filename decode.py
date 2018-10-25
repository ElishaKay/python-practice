#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Usage Example -
python steganography.py -f X.bmp -o Y.bmp -m "Hidden message!"
'''



from optparse import OptionParser


__author__ = "ITC"
__license__ = "GPLv3"

from PIL import Image

try:
   input = raw_input
except NameError:
   pass


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def decode(input_image_file, auto_convert_rgb=False, order_func = fib):
    img = Image.open(input_image_file)
    hidden_bits_order = order_func()
    encoded = img.copy()
    width, height = img.size
    index = 0
    print('width: ',width, 'height: ',height)   
    fo = open('image_logs.txt', 'a')

    len_message_bits=144
    npixels = width * height
    for row in range(height):
        for col in range(width):
            # if index + 3 <= (npixels * 3):
            if index + 3 <= 1000:
                 # Get the colour component.
                pixel = img.getpixel((col, row))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                bit = hidden_bits_order.next() % 8
                print('bit =',bit)
                mask = 1 << bit
                print('mask: ',mask)
                v = v&(~mask)
                # fo.write('current_pixels rgb is:'+str(r)+', '+str(g)+', '+str(b)+'\n')

                index = index+1
                if index ==1000:
                    return
    # fo.close()


def main():
    decode('secret_penguin.bmp')


if __name__ == "__main__" :

    main()





