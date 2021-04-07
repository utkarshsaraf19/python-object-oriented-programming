def format_string( string, formatter= None):
    class DefaultFormatter:
        def format(self,string):
            return str(string).title()
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)

if __name__ == "__main__":
    hello_string = "Hello World How are you"
    print(format_string(string=hello_string))