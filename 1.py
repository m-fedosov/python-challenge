string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
         "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
letter = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
for i in string:
    if i in letter:
        if i == 'y':
            i = 'a'
        elif i == 'z':
            i = 'b'
        else:
            i = letter[letter.index(i) + 2]
    answer += i
print(answer)

print('map'.translate(string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')))
