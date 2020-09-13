# Think of at least five places in the world you’d like to
# visit.

places_to_visit = ["japan", 'london', 'hong kong', 'hawaii', 'oregon']

# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print("Here's the original list:")
print(places_to_visit)

# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print("\nHere's the sorted() list:")
print(sorted(places_to_visit))  # sorted() is NOT .sorted its standalone!

# • Show that your list is still in its original order by printing it.
print("\nHere's the original list:")
print(places_to_visit)

# • Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list.
print("\nHere's the sorted(reverse=True) list:")
print(sorted(places_to_visit, reverse=True))

# • Show that your list is still in its original order by printing it again.
print("\nHere's the original list:")
print(places_to_visit)

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
places_to_visit.reverse()
print("\nHere's the reverse() list:")
print(places_to_visit)

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
places_to_visit.reverse()
print("\nHere's the reverse() list:")
print(places_to_visit)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
places_to_visit.sort()
print("\nHere's the sort() list:")
print(places_to_visit)

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
places_to_visit.sort(reverse=True)
print("\nHere's the sort(reverse=True) list:")
print(places_to_visit)


# .sorted() and .reversed() don't return a new object, therefore need to use the function then
# print out original list again
