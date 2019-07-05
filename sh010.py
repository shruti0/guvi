putsri = input()
print(''.join([ putsri[x:x+2][::-1] for x in range(0, len(putsri), 2) ]))
