# Author: Dominic Savaglio djs7129@psu.edu
# Collaborator: Jack Scallan jgs5472@psu.edu
# Collaborator: Adam Greenberg aqg5910@psu.edu
# Collaborator: Tuan Nguyen tmn5319@psu.edu
# Section: 10R
# Breakout: 3
def sum_n(n):
  if n < 1:
    return 0
  else:
    return n + sum_n(n-1)
def print_n(s,n):
  if n <= 0:
    return;
  else:
    print (s)
    print_n (s, n-1)
def run():
  sum = int(input("Enter an int: "))
  sum_n(sum)
  print(f"sum is {sum_n(sum)}.")
  string = str(input("Enter a string: "))
  print_n(string, sum)
if __name__ == "__main__":
  run()