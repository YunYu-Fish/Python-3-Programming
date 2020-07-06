# There's a function we are providing in for you in this problem called square.
# It takes one integer and returns the square of that integer value.
# Write code to assign a variable called xyz the value 5*5 (five squared).
# Use the square function, rather than just multiplying with *.
def square(num):
    return num*num

xyz = square(5)
print(xyz)

# Write a code to assign the number of characters in the string'rv' to a variable num_chars.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

num_chars = 0
for c in rv:
    num_chars += 1
print(num_chars)
