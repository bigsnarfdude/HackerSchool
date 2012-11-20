#! /usr/bin/env python

import string
out_1 = []
out_2 = []
magic_1 = [101,94,96,104,98,111]
magic_2 = [-16, -21, 7, 0, -3]

def first_function(magic_1):
    [ out_1.append(chr(number)) for number in [ x+3 for x in magic_1]]
    y = ''.join(out_1).upper()

    return y


def second_function(magic_2):                                        
    out_2 = [ 1 - reduce(lambda x, y: x+y, magic_2[1:])]
    map (lambda x: out_2.append(out_2[-1]+x), magic_2)
    x = ''.join(map(lambda x: string.uppercase[x], out_2))

    return x

if __name__ == "__main__":  
    print first_function(magic_1), second_function(magic_2)
