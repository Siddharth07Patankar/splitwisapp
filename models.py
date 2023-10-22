class User:
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

class UserGroup:
    def __init__(self, group_name, members):
        self.group_name = group_name
        self.members = members

class Expense:
    def __init__(self, description, amount, payer, participants, expense_type, shares=None):
        self.description = description
        self.amount = amount
        self.payer = payer
        self.participants = participants
        self.expense_type = expense_type
        self.shares = shares if shares else []