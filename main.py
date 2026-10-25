events = []
count = 0

def add_event(id, price, qty, side):
    global count
    event = (id, price, qty, side)
    events.append(event)
    count += 1

def show_details():
    print("Total events:", len(events))
    print("Total received:", count)

    print("\nEvent Details:")

    for e in events:
        print("ID:", e[0], "Price:", e[1],
              "Qty:", e[2], "Side:", e[3])


for i in range(10):
    price = 100 + (i % 5)
    qty = 10
    side = i % 2

    add_event(i, price, qty, side)

show_details()
