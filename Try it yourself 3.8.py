places_to_visit = ['Khankendi', 'Khojaly', 'Aghdam', 'Barda', 'Beylagan']

print("Original list:")
print(places_to_visit)

print("\nAlphabetical order (using sorted()):")
print(sorted(places_to_visit))

print("\nOriginal list (unchanged):")
print(places_to_visit)

print("\nReverse alphabetical order (using sorted(..., reverse=True)):")
print(sorted(places_to_visit, reverse=True))

print("\nOriginal list (still unchanged):")
print(places_to_visit)

places_to_visit.reverse()
print("\nOrder changed using reverse():")
print(places_to_visit)

places_to_visit.reverse()
print("\nBack to original order using reverse() again:")
print(places_to_visit)

places_to_visit.sort()
print("\nPermanently sorted in alphabetical order using sort():")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nPermanently sorted in reverse alphabetical order using sort(reverse=True):")
print(places_to_visit)