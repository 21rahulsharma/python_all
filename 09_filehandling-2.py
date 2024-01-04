f=open('sample_textfile.txt','w')
f.write("File Handling is loading")
f.write(" It's getting easier")
#write function for a pre-existing file deletes its content and add what is written within the f.write() function
#So its better to open with append mode to update it 
#'w' creates a new fie if no such file exists with that name 
f.close()