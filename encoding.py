encodingNum=100
input = open("source.txt","r", encoding='utf-8')
output = open("security.txt", "w", encoding="utf-8")
for inStr in input.readlines():
    out_str = ""
    for s in inStr:
        tmp = ord(s) + encodingNum
        out_str += chr(tmp)
    output.writelines(out_str)

input.close()
output.close()