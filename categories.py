CATEGORY = "Password"

tickets = {"T101": "Password",
           "T101": "Hardware",
           "T102": "Hardware",
           "T103": "Password",
           "T104": "Software",
           "T105": "Password"}

password_tickets = []

for ticket_id, ticket_category in tickets.items():
    if ticket_category == CATEGORY:
        password_tickets.append(ticket_id)


print(f"There are {len(password_tickets)} tickets for password issues and they are: {" | ".join(password_tickets)}")
