# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
fileplan = open('travel_plans.txt','r')
contents = fileplan.read()
num = 0
for char in contents:
  num += 1

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
# Find the total number of words in the file and assign this value to the variable num_words.
file_emotion = open('emotion_words.txt','r')

contents = file_emotion.read()
#print(contents)
cont = contents.strip().split()
#print(cont)
num_words = 0
for wrd in cont:
    num_words += 1

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
file_school = open('school_prompt.txt','r')

lines = file_school.readlines()
num_lines = 0
for lin in lines:
    num_lines += 1


# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
file_school = open('school_prompt.txt','r')

contents = file_school.read()
contents.strip()
beginning_chars = ''
for char in contents[:30]:
    beginning_chars = beginning_chars + str(char)

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
three = []
with open('school_prompt.txt','r') as f:
    for line in f:
        print(line.split())
    three = [line.split()[2] for line in f]

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions = []
with open('emotion_words.txt','r') as f:
          emotions = [line.split()[0] for line in f]

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
first_chars = ''
with open('travel_plans.txt','r') as f:
    first_chars = f.read(33)

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
f = open('school_prompt.txt','r')
words = f.read().strip().split()
p_words = []
for wrd in words:
    if 'p' in wrd:
        p_words.append(wrd)


