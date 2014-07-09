table = int(input("Which multiplication table would you like? ")) #asks the user what times table theyd like and saves it in the variable "table"
limit = int(input("How high? "))#asks the user how far in the table theyd like to go and saves it in the variable "limit"

for x in range (1,limit+1):#makes the printing start at 1 and end in the limit plus one because python starts at zero
    answer = table * x#timses the user input from "table" by x in the range "1 to limit+1"
    print("Heres your table", x, 'X', table, '=', answer)#prints out each line in a suitable format for the user to make it easy to understand


