programming_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"

}
print(programming_dictionary["bug"])

# adding new items to dic
programming_dictionary["Loop"] = " The action of doing something over and over again"
print(programming_dictionary)

# create and empty dic
empty_dictionary = {}

# edit an item in a dic
programming_dictionary["bug"] = "2342342"

# loop dic
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
