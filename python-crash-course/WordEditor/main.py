'''This program allows the user to create and write a file, or read file contents
with the help of a menu interface'''

# Loop program while q is not entered in menu
user_input = 0
while (user_input != "q"):

  # Main menu
  print("------------------------------------------------------")
  print("                   Python Word Editor")
  print("------------------------------------------------------")
  print("1) Create a file")
  print("2) Open a file")
  print("------------------------------------------------------\n")
  
  user_input = input("Enter a number option and press ENTER or type 'q' to quit: ")

  # Menu option 1 (Create file)
  if (user_input == "1"):
    file_input = input("\nStart typing: ")
    file_name = input("\nEnter file name and press ENTER:")
    try:
      new_file = open(f"{file_name}.txt","x")
      new_file = open(f"{file_name}.txt","w")
      new_file.write(file_input)
      new_file.close()
      print("\nFile created.")
    # If file already exists
    except FileExistsError:
        print("\nCannot create file; a file of the same name already exists.")
    finally:
      print("\n")

  # Menu option 2 (Open and read file)
  elif (user_input == "2"):
    file_name = input("\nEnter a file name plus the extension: ")
    try:
      file_read = open(f"{file_name}", "r")
      print(f"\n\n\n                       [OPEN]{file_name}                   ")
      print("=================================================================\n")
      print(file_read.read())
      file_read.close()
    # If file doesn't exist
    except FileNotFoundError:
      print("\nNo such file exists. Please try again.")
    finally:
      print("\n")

  # If no listed command is entered
  elif (user_input != "q"):
    print("\nCommand not recognized. Please try again.\n")

# When q is entered
print("\nProgram ended.")