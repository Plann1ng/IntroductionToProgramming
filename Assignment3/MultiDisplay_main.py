# Import the class
import MultiDisplay as multi

# Calling it and attaching to a variable
md = multi.MultiDisplay()

# Body as in the example
md.set_message("Hello World!")
md.set_count(3)
print(md.to_string())
md.display()

md.set_display("Goodbye cruel world!", 2)
print(md.to_string())
print(f'"Current message:", {md.get_message()}\n')