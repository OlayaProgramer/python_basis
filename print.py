# print is use when I need to show by console some text or result of operation.

# I can print different types of data like strings, numbers and other kind of data
# examle of print a String
print("Hello world")

# example of print a number
print(5)

# example of print a operation
print(5 + 9)
print(5 - 9)
print(5 * 9)
print(5 / 9)

# example of print adding extra information
print("The example" + " another text")
print("The example 1, I can not concatenate with the sign plus a string with number") # "string" + 5 -> number can't concatenate
print("The result of the operation is", (5 + 9), "use the coma is important for concatenate a number with strings")
print("There is an interesting point in it way to use print, because in javascript or java use the sign plus (+) to concatenate the string with another information")
print("but here in python is with coma (,), but only with operations, and itself give the space of separation, in javascript or java I have to add the space by concatenate the results")

# example of print with format
print(f"It is a good idea to show information in console when need add operation like sum {5} + {9} = {5 + 9} and add more information, it do easier than use coma")

# example of print with separator
print("This text", "is separate with coma", "and the coma give the space need to understad")
print("also we can use", "other kings of separation", "like / and it will be use like separator", sep="/")
print("or", "can", "be", "it \\n", sep="\n")
print("root node", "parent", "child", "last node", sep=" -> ")

# example of print without line break
print("when I need to preven", "the line break", sep=", ", end=" ")
print("you can use", "the end parameter", "it help to preven the last caracter in the print to be \\n", sep=", ", end=" ")
print()

# print can add text into a file when I need
# example of sintaxis print("Here is the text to introduce to the file", file=name_of_file) when you use a "file=" you give indication on what file you can add text
import io
fake_file = io.StringIO()
#print('hello world', file=fake_file)
print(fake_file.getvalue())


with open("example.txt", mode="w") as file_:
    print("I learn Python", file=file_) # if you use the print to write inside the file, all content will be replace with the new content

# example of buffering
import time
for i in reversed(range(1, 4)):
    print(i, end="...", flush=True)
    time.sleep(1)
print("Go!")

# without flush active is show when the time is over
for i in reversed(range(1, 4)):
    print(i, end="...")
    time.sleep(1)
print("Go!")