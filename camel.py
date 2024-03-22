import re

def snake_case(name):
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return print(f"snake_case: {name}")          
      

def main():
        camel=input("camelCase: ")
        snake_case(camel)



if __name__ == "__main__":
    main()
