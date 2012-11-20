import string

def transpose_numbers_letters(list_of_items):                                        
    out = [ 1 - reduce(lambda x, y: x+y, magic[1:])]
    map (lambda x: out.append(out[-1]+x), magic)
    x = ''.join(map(lambda x: string.uppercase[x], out))
    return x

def gen_number():
    for a in range(-25, 26):
        for b in range(-25, 26):
            for c in range(-25, 26):
                for d in range(-25, 26):
                    for e in range(-25, 26):
                        magic = [a,b,c,d,e]
                        try:
                            result = transpose_numbers_letters(magic):
                            if result == 'HACKER':
                                print magic
                        except:
                            pass
gen_number()
