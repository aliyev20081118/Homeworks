dinner_guests = ['Nijat','Casarat','Asif','Aykhan','Farac','Emin','Ziya']
for guest in dinner_guests:
    print("Dear "+guest+", I would be deeply honored if you would join me for dinner to discuss your incredible life and work.")
print("Good news! We found a bigger dinner table, so we are inviting three more guests.\n")
dinner_guests.insert(0, "Alida")
dinner_guests.insert(2, "R.Gulay")
dinner_guests.append("H.Gulay")
for guest in dinner_guests:
    print(f"Dear {guest}, I would be deeply honored if you would join me for dinner.")
print("Unfortunately, our new dinner table won't arrive in time, and we now have space for only two guests.\n")

while len(dinner_guests) > 2:
    popped_guest = dinner_guests.pop()
    print(f"I'm sorry, {popped_guest}, I can't invite you to dinner.")
print("\n----------------------------------------\n")
for guest in dinner_guests:
    print(f"Dear {guest}, you are still invited to dinner!")
print("\n----------------------------------------\n")
del dinner_guests[0]
del dinner_guests[0]
print("Current guest list:", dinner_guests)