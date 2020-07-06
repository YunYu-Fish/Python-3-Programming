# Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,'horeseback riding')

# Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove('London')

# Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('guadalajara')

# Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()

# Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.sort(reverse = True)
z_winners = winners

# Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1.
# Each character in str1 should be its own element in the list chars.
str1 = "I love python"
chars = []
for c in str1:
  chars.append(c)

# For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = 'python!'
app = []
for i in ael:
  app.append(i)