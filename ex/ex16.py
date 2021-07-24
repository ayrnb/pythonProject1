filename = "text.txt"
print(f"We're going to erase {filename}")
print("if you don't want that,hit CTRL-C(^C).")
print("If you do want that,hit RETRUN")
input("?")
print("Opening the file...")
targrt=open(filename,'w')
print("Truncating the file.Goodbye!")
targrt.truncate()
  
