num_of_invited_guests = int(input())
coming_guests = set()

for _ in range(num_of_invited_guests):
    guest = input()
    coming_guests.add(guest)

while True:
    reservation = input()
    if reservation == "END":
        break
    coming_guests.remove(reservation)

print(len(coming_guests))

sorted_guests = sorted(coming_guests)

for guest in sorted_guests:
    print(guest)
