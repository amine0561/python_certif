def fuel():
    while True:
        try :
            fraction=input("Fraction (X/Y):")
            if x > z:
                raise ValueError("X cannot be greater than Y")
            x, z=fraction.split("/")
            output=(int(x)/int(z))*100
        except (ValueError):
            print("X, Y must be integers")
        except ZeroDivisionError:
            print("Y can not be 0")
        else:
            if output<=1:
                print("E")
                break
            elif output>=99:
                print("F")
                break
            else :
                return print(round(output),"%")

def main():
    fuel()


if __name__ == "__main__":
    main()