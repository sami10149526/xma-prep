TARGET_HOURS = 48

open_tickets = {"T101": 45,
           "T102": 93,
           "T103": 32,
           "T104": 102,
           "T105": 13,
           "T106": 78,}

ticket_ids = ["T101", "T102", "T103", "T101", "T104", "T102",]

def is_overdue(hours_open, target):
    return hours_open > target

def find_overdue(tickets,target):
    overdue = []
    for ticket_id, hours in tickets.items():
        if is_overdue(hours,target):
            overdue.append(ticket_id)
    return overdue

def count_ids(tickets_ids):
    counts = {}

    for ticket_id in tickets_ids:
        if ticket_id in counts:
            counts[ticket_id] +=1
        else:
            counts[ticket_id] =1
    return counts

def duplicates_from_counts(counts):
    duplicate_ids = []
    for ticket_id, count in counts.items():
        if count > 1:
            duplicate_ids.append(ticket_id)
    return duplicate_ids

print(f"Overdue Tickets: {','.join(find_overdue(open_tickets, TARGET_HOURS))}\n"
      f"Duplicate IDs: {','.join(duplicates_from_counts(count_ids(ticket_ids)))}\n"
      f"Total tickets checked: {len(open_tickets)}")



