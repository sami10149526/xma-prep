import csv

TARGET_HOURS = 48

def is_overdue(hours_open, target):
    return hours_open > target

def find_overdue(rows,target):
    overdue = []
    for row in rows:
        try:
            hours = float(row["hours_open"])
            if is_overdue(hours,target):
                overdue.append(row["ticket_id"])
        except ValueError:
            pass
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

def find_missing(rows):
    missing_cat=[]
    for row in rows:
        if row["category"].strip() == "":
            missing_cat.append(row["ticket_id"])
    return missing_cat

def find_bad_hours(rows):
    bad_hours_ids = []
    for row in rows:
        try:
            float(row["hours_open"])
        except ValueError:
            bad_hours_ids.append(row["ticket_id"])
    return bad_hours_ids

def load_tickets(filename):
    rows = []
    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Could not find {filename}")
        exit()
    return rows

#------------ main ---------------
ticket_ids = []
report = ""

rows = load_tickets("tickets.csv")
for row in rows:
    ticket_ids.append(row["ticket_id"])

report =(f"Tickets Loaded: {len(rows)}\n"
        f"Duplicate IDs: {', '.join(duplicates_from_counts(count_ids(ticket_ids)))}\n"
        f"Missing Category: {', '.join(find_missing(rows))}\n"
        f"Overdue (Over 48h open): {', '.join(find_overdue(rows,TARGET_HOURS))}\n"
        f"Bad hours tickets: {', '.join(find_bad_hours(rows))}")

with open ("report.txt", "w") as file:
    file.write(report)


#update to see if it works