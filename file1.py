class IOString():
    def __init__(self):
        self.str = ""

    def get_String(self):
        self.str1 = input("enter string : ")

    def print_string(self):
        print("result is :", self.str1.upper())

str1 = IOString()


str1.get_String()
str1.print_string()