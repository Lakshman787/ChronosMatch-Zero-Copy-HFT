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

for i in range(10):
    add_event(i, 100 + i % 5, 10, i % 2)

show_details()
