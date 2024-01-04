#Use open function to read the contents of a file
f=open('sample_textfile.txt','r') #Accepts 2 parameters (by default the mode is 'r')
data=f.read()
print(data)
f.close()