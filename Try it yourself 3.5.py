dinner_guests = ['Nijat','Casarat','Asif','Aykhan','Farac','Emin','Ziya']
for guest in dinner_guests:
    print("Dear "+guest+", I would be deeply honored if you would join me for dinner to discuss your incredible life and work.")
absent_guest = "Nijat"
print(f"\nUnfortunately, {absent_guest} can't make it to the dinner.\n")
new_guest = "Ruslan"
dinner_guests[dinner_guests.index(absent_guest)] = new_guest
for guest in dinner_guests:
    print(f"Dear {guest}, I would be deeply honored if you would join me for dinner.")