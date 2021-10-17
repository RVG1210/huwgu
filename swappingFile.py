# Project by J AJITESH

# function to swap data from  files
def SwapFileData():
     # taking the names of the files from the user
     swap1 = input("Enter 1st file name to Swap:-  ")
     swap2 = input("Enter 2nd file name to Swap:-  ")
     
     # Open the 1st file in read format and save the data in a variable
     with open(swap1, 'r') as a:
         read_a = a.read()
     
     # Open the 2nd file in read format and save the data in a variable
     with open(swap2, 'r') as b:
         read_b = b.read()

     # Open 1st file in write mode, removes its data and adds data from 2nd file
     with open(swap1, 'w') as a:
         a.write(read_b)

     # Open 2nd file in write mode, removes its data and adds data from 2nd file
     with open(swap2, 'w') as b:
         b.write(read_a)


print()
# Title of the project
print('Swapping File Data - Project')
# Develpoed details
print('This project is developed by J AJITESH')
print()

#Call the function to execute the program
SwapFileData()

print()
# Confirmation Message and thank the user.
print("Data Swapped Successfully")
print()
print("Thank you for using Swapping File Data")
# Helps to re-run the project
print("Run the terminal again to reswap the data in the files.")
