# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
rfile=fh.read()
line=rfile.rstrip()
y=line.upper()
print(y)
