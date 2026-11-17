ticket_ids = ["T101", "T102", "T103", "T101", "T104", "T102", "T101"]


"""def find_duplicates(ticket_ids):
    seen = []
    duplicates = []
    for ticket in ticket_ids:
        if ticket in seen and ticket not in duplicates: # if ticket id is in seen already add to dupe
            duplicates.append(ticket)
        else:
            if ticket not in seen:
                seen.append(ticket) # if its not in seen already add to seen
    return duplicates
"""



def count_ids(ticket_ids):
    ticket_dictionary = {}
    for ticket in ticket_ids:
        if ticket in ticket_dictionary:
            ticket_dictionary[ticket] = ticket_dictionary[ticket] + 1
        else:
            ticket_dictionary[ticket] = 1
    return ticket_dictionary

print(count_ids(ticket_ids))



def duplicates_from_counts(tickets):
    duplicates = []
    for ticket, amount in tickets.items():
        if amount > 1:
            duplicates.append(ticket)
    return duplicates


print(duplicates_from_counts(count_ids(ticket_ids)))
