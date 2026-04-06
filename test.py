# Movie Theatre Booking System (Simple)

capacity = 350
sold = 0
bookings = 0
rejected = 0

while sold < capacity:
    tickets = int(input("Tickets to book (1-15, 0 to exit): "))
    if tickets == 0:   # stop
        break
    if tickets < 1 or tickets > 15 or sold + tickets > capacity:
        print("BOOKING REJECTED - Invalid ticket count or no seats.")
        rejected += 1
        continue

    valid = True
    for i in range(tickets):
        age = int(input(f"Age for ticket {i+1}: "))
        if age < 12:
            valid = False
    if not valid:
        print("BOOKING REJECTED - Age restriction.")
        rejected += 1
        continue

    sold += tickets
    bookings += 1
    print(f"BOOKING CONFIRMED - {tickets} tickets.")

    if sold >= capacity:
        print("Theatre FULL.")
        break

# Final Report
print(f"Final Report: Total Bookings {bookings} Total Tickets Sold {sold}, Rejected Bookings {rejected} Remaining Seats: {capacity - sold}")
