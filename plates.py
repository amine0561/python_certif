def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s[:2].isalpha():
        return False
    
    if any(char in ' .,;:!?' for char in s):
        return False
    
    if not s[2:].isdigit() or s[2] == '0':
        return False
    
    return True

main()
