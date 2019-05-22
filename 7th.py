#extract number at the end
text = 'X-DSPAM-Confidence:    0.8475'
space=text.find('0')
Espace=text.find('5')
num=text[space:Espace+1]
fnum=float(num)
print(fnum)
