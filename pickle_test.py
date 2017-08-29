# https://pythontips.com/2013/08/02/what-is-pickle-in-python/

import pickle

a = ['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb') 

# this writes the object a to the
# file named 'testfile'
# dump and load are two important function for pickle. The first one is dump, which dumps an object to a file object and the second one is load, which loads an object from a file object.

pickle.dump(a,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'rb') 
# load the object from the file into var b
b = pickle.load(fileObject)

if a==b :
    print("Pickle works!")
else:
    print("Pickle not work!")