from random import choices

ticket = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')
winning_ticket = choices(ticket, k=4)
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")