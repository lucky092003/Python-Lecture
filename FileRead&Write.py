#file = open("example.txt","w")
#file.write("hello,this is a test.")
#file.close ()

filename = "example.txt"
file = open(filename, "r")
filecontent = file.read()
file.close()

print(filecontent)
