import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
	ord('\t') : ' ',
	ord('\f') : ' ',
	ord('\r') : None #Delete
}

a = s.translate(remap)
print(a)

cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode)
							if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)

b.translate(cmb_chars)
print(b)

