#Input variables as seen in the code
string = ':\"AL_RT^L*.?+6/46'
long = 28537194573619560

#random string with length 17
inpString = "aaaaaaaaaaaaaaaaa"
arr = []

for i in range(0,len(inpString)):
	#Getting (i%7th) byte of long
	first = (long >> (8*(i % 7))) & 0xff #*((BYTE*)&(x)+y means: yth byte of value x
	#executing the actual xor operation
	second = first ^ ord(string[i])
	arr.append(chr(second))

end = ""

for i in range(0,len(arr)):
	end += arr[i]

print(end)
