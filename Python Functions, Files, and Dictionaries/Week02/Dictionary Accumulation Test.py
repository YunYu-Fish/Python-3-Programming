# The dictionary Junior shows a schedule for a junior year semester. 
# The key is the course name and the value is the number of credits. 
# Find the total number of credits taken this semester and assign it to the variable credits. 
# Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for n in Junior:
  credits += Junior[n]

# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
  if c not in freq:
    freq[c] = 0
  freq[c] = freq[c] + 1

# Provided is a string saved to the variable name s1. 
# Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
