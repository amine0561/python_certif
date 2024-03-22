def shorten():
    inp = input("Input: ")
    no_vowels = inp.translate(str.maketrans('', '', 'aeiouAEIOU'))
    print(f"Output: {no_vowels}")

def main():
    print("This program will shorten the words you give to it")
    shorten()

if __name__ == "__main__":
    main()
