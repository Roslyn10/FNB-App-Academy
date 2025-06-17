singlequotes = 'Hello World'
print(singlequotes)

doublequotes = "Hello World"
print(doublequotes)

multiplelines = """This is going
over multiple lines"""
print(multiplelines)

# This section is more alittle more advanced string types/uses 

message = "Hello World"
print(message[0])
print(message[1])
print(message[3])
print(message[-2])
print(message[-4])

print(len(message))

message2 = " Hello, World"
print(message2.strip()) # Removes the whitespaces, both leading and trailing
print(message2.lower()) # Converts all charaters to lowercase
print(message2.upper()) # Converts all characters to Uppercase
print(message2.split(',')) # Splits the string into a list based off the comma
message_new = message2.replace('Hello', 'Sup') # Replaces the chosen string with a different string
print(message_new)