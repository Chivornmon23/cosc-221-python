#Keyword arguments = an argument preceded by an identifier helps with readability order
#              of arguments doesn't matter 
#               1. positional   2. default      3. KEYWORD      4. arbitrary

def hello(greeting, title, first, last): 
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr. ", first="Spongebob", last="Squarepants")
