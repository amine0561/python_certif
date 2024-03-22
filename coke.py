def coke():
    amount_due=50
    inserted_coin=0
    while inserted_coin < 50 :

        coin=int(input("Insert coin (25cents/10 cents/5cents) :"))
        inserted_coin+=coin 

        if inserted_coin < amount_due:
            print(f"Amount Due : {amount_due-inserted_coin}")
        else :
            print(f"change owed : {inserted_coin-amount_due}")
            print("enjoy your coke ! ")


def main():
    print("This machine sells Coca-Cola(Coke) bottles")
    print("The price of a bottle is 50 cents")
    coke()

if __name__ == "__main__":
    main()