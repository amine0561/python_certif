def display_total_cost(items):
    total_cost = sum(menu.get(item, 0) for item in items)
    print(f"Total: ${total_cost:.2f}")

menu = {
    "Burrito": 7.50,
    "Large Quesadilla": 9.50,
    "Super Quesadilla": 10.50,
    # Add more items to the menu if needed
}

def taqueria():
    items = []
    while True:
        try:
            item = input("Item: ").strip().title()
            if not item:
                display_total_cost(items)
                continue
            items.append(item)
            display_total_cost(items)
        except EOFError:
            break

if __name__ == "__main__":
    taqueria()
