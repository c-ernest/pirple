import os

# Define file extension. Append this to the name entered by user
file_format = '.txt'

file_name = input('Please enter a file name to proceed. If the file does not exist a new file shall be created with content: ')

try:
      file = open(file_name+file_format)
except IOError:
      print(file_name, " FILE DOES NOT EXIST")

      file = open(file_name+file_format, 'w')

      info = input("PLEASE ENTER INFORMATION: ")
      file.write(str(info))
      file.write('\n')

      file.close()
      print(file_name, " FILE HAS BEEN CREATED")

else:
      print(file_name, " FILE HAS BEEN FOUND")

      def ask(file):

            try:
                  
                  print("What do you want to do with the file Read/Delete/Append to the file: ")
                  print("A. Read the file")
                  print("B. Delete the file")
                  print("C. Append to the file")
                  print("D. Change a line in the file")
                  print("E. Quit")
                  choice = input("TYPE HERE: ")               
            except Exception as err:
                  print("ERROR: make your choice from A - E.")
                  print(str(err))

            # Read the file
            if choice == "A" or "a":
                  file = open(file_name+file_format, 'r')
                  content = file.read()
                  print("FILE CONTENT")
                  print("------------")
                  print(content)
                  file.close(),
                  ask(file)

            # Delete the file
            elif choice == "B" or "b":
                  file.close()
                  os.remove(file_name+file_format)
                  print(file_name, "FILE HAS BEEN DELETED")

            # Append to the file
            elif choice == "C" or "c":
                  file = open(file_name+file_format, 'a')
                  info2 = input("What do you want to append to the file: ")
                  file.write(str(info2))
                  file.write('\n')
                  file.close()
                  print(info2, " HAS BEEN APPENDED")
                  ask(file)

            # Change a line in the file
            elif choice == "D" or "d":
                  f1 = open(file_name+file_format, 'r+')

                  file = f1.readlines()
                  print(len(file))
                  line = input("Enter line Number: ")
                  try:
                        int(line)
                  except ValueError:
                        print("ERROR: Enter a number not a string")
                        print('\n')
                        ask(file)

                  # Check the input against the length of the list
                  if int(line) > len(file):
                        print("Line does not exist")
                        ask(file)

                  line = int(line)

                  new_line = (line-1)
                  new_input = input("Enter new string: ")

                  file2 = str(file).strip('[]')
                  file[new_line] = file[new_line].replace('\n','\\n')

                  x = file2.replace(file[new_line], new_input).split(", ")
                  new_list = []

                  for element in x:
                        mun = element.replace('\\n','')
                  with open(file_name+file_format, 'w', -1, 'utf-8') as new_file:
                        for element in x:
                              mun = element.replace('\\n','')
                              num = mun.strip("'")
                              new_file.writelines(str(num))
                              new_file.write('\n')
                  f1.close()
                  ask(file)

            # exit the program
            elif choice == "E" or "e":
                  exit()
      ask(file)
                  

      
      
