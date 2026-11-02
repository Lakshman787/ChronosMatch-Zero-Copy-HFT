events = []
count = 0

def add_event(id, price, qty, side):
    global count
    event = (id, price, qty, side)
    events.append(event)
    count += 1

def show_details():
    buy_count= 0
    sell_count= 0
    total_qty= 0
    total_value= 0
    buy_value= 0
    sell_value= 0
    
    print("Total events:", len(events))
    print("Total received:", count)
    print("\nEvent Details:")

    for e in events:
        if e[3] == 0:
            side="BUY"
            buy_count +=1
            buy_value+=e[1]* e[2]
        else:
            side="SELL"
            sell_count +=1
            sell_value +=e[1]*e[2]
            
         total_qty += e[2]
         total_value += e[1] * e[2]
        
        print("ID:", e[0], "Price:", e[1],
              "Qty:", e[2], "Side:", side)
        
    print("\nBUY event:", buy_count)
    print("SELL event:", sell_count)
    print("total Qty:", total_qty)
    print("total Value:", total_value)
    print("Total Buy Value:", buy_value)
    print("Total sell value:", sell_value)


for i in range(10):
    price = 100 + (i % 5)
    qty = 10
    side = i % 2

    add_event(i, price, qty, side)

show_details()
