"""1.The code creates a text file which contains the following content:

100.12111.23

However, the correct content should be:

100.12

111.23"""

#Solution
"""file = open("../bugfixexercise/data.txt", 'w')

file.write("100.12")
file.write("\n"+"111.23")

file.close()"""




"""2.The code below tries to write the string "100.2" to the text file. 
However, there is an error. Try to fix the error."""

#Solution
"""file = open("../bugfixexercise/data.txt", 'w')
file.write("100.12")
file.close()"""
