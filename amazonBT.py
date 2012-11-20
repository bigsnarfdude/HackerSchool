import string

def bruteforce_numbers_to_words():
    for a in range(-25, 26):
        for b in range(-25, 26):
            for c in range(-25, 26):
                for d in range(-25, 26):
                    for e in range(-25, 26):
                        magic = [a,b,c,d,e]
                        try:
                            out = [ 1 - reduce(lambda x, y: x+y, magic[1:])]
                            map (lambda x: out.append(out[-1]+x), magic)
                            result = ''.join(map(lambda x: string.uppercase[x], out))
                            if result == 'SCHOOL':
                                return magic
                        except:
                            pass
 
print bruteforce_numbers_to_words()

