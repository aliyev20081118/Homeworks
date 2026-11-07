rivers = ['Nile', 'Amazon', 'Volga', 'Mississippi', 'Danube']
print("Original list of rivers:")
print(rivers)

print(f"\nThe first river in the list is: {rivers[0]}")

rivers[0] = 'White Nile'
print("\nAfter modifying the first element:")
print(rivers)

rivers.append('Kur')
print("\nAfter using append():")
print(rivers)

rivers.insert(2,'Araz')
print("\nAfter using insert():")
print(rivers)

del rivers[0]
print("\nAfter using del to remove the first item:")
print(rivers)

popped_river = rivers.pop()
print(f"\nPopped river (removed from the end): {popped_river}")
print("List after using pop():")
print(rivers)

rivers.remove('Danube')
print("\nAfter using remove('Danube'):")
print(rivers)

print(f"\nNumber of rivers currently in the list: {len(rivers)}")

print("\nTemporary alphabetical order using sorted():")
print(sorted(rivers))
print("Original list is still in its original order:")
print(rivers)

print("\nTemporary reverse alphabetical order using sorted(..., reverse=True):")
print(sorted(rivers, reverse=True))

rivers.reverse()
print("\nAfter using reverse():")
print(rivers)

rivers.sort()
print("\nAfter using sort() (alphabetical):")
print(rivers)

rivers.sort(reverse=True)
print("\nAfter using sort(reverse=True) (reverse alphabetical):")
print(rivers)