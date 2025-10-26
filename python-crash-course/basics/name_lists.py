names = ['bao', 'long', 'james']
for name in names:
    print(f"Hello {name.title()}")


guests = ['teddy','einstein','marie']

for guest in guests:
    print(f"please come for dinner {guest.title()}")

not_come='teddy'
print(f"{not_come.title()} cannot come")

guests.remove(not_come)
print(guests)

guests.append('merkel')
guests.append('magaret')
print(guests)

while(len(guests)>2):
    guests.pop()

print(guests)