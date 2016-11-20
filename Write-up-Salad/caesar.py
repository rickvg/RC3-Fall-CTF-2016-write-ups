import sys

# Prepared alphabet for Caesar Cipher. Can be changed.
caesaralpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar(input_string, rot):
    print("Rotating characters by: " + sys.argv[1])
    output_string = ""
    for i in range(0, len(input_string)):
        introtation = int(rot)
        if caesaralpha.index(input_string[i].upper()) + introtation >= len(caesaralpha):
            intavailable = len(caesaralpha) - caesaralpha.index(input_string[i].upper())
            introtation = introtation - intavailable
        else:
            introtation += caesaralpha.index(input_string[i].upper())
        output_string += caesaralpha[introtation]
    return output_string

strFileInp = open(sys.argv[2], 'rb')
	
out = ""
strInp = strFileInp.read().decode("utf-8").rstrip("\n")
if sys.argv[1] == "all":
    for i in range(1,len(caesaralpha)):
        out += "ROT " + str(i) + ": " + caesar(strInp, i) + "\n"
else:
    out = "ROT " + sys.argv[1] + ": " + caesar(strInp, sys.argv[2])
out = out.encode("utf-8")

print("Output: " + out.decode("utf-8"))