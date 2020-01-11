import re


def text_match(text):
    print(re.findall(r"\w*z", text))


print(text_match("The quick brzown fox jumps over tzhe lazy dog."))
print(text_match("Python Exercises."))
print(re.findall("[a-z][A-Z]", "aZ ZAZxSAD hvV ASx"))

# https://www.w3schools.com/python/python_regex.asp
# *  ->  0 or more occurence
# \w  ->  word
# [a-z][A-Z]  ->  two character sequence first lowercase the uppercase
# ^ -> start    $ -> end
# [xya97xzc(&)]  ->  any of those character


def match_num(string):
    text = re.compile("^5[-+=][0-9]*1$")
    if text.match(string):
        return True
    else:
        return False


print(match_num("5-2345861"))
print(match_num("6-2345861"))

print((lambda str: re.sub("[a-z]", "!", str))("hdsfjkJGXhjvmGFhjvKUY"))

# Check if the string contains "a" followed by exactly two "l" characters:
print(re.findall("al{2}", "poallllsllsal"))

