class Category(object):

    def __init__(self, name=None):
        self.name = name
        self.ledger = []

    def __str__(self):
        self.title = 30 * "*"
        self.title = (self.title[0:(15-(int(len(self.name)/2)))] +
                      self.name[0].upper() +
                      self.name[1:].lower() +
                      self.title[15+(int(len(self.name)/2)):])[:30]
        self.body = self.title + f"\n"
        for entries in self.ledger:
            self.body += (f"{entries['description'][:23]:<23}" +
                          f"{('{:.2f}'.format(entries['amount']))[:7]:>7}\n")
        self.body += f"Total: {'{:.2f}'.format(self.get_balance())}"
        return self.body

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    def get_name(self):
        return self.name

    def get_ledger(self):
        return self.ledger

    def get_balance(self):
        balance = float(0)
        for element in self.ledger:
            balance += element["amount"]
        return balance

    def check_funds(self, amount):
        check_funds_status = True
        if self.get_balance() < amount:
            check_funds_status = False
        return check_funds_status

    def withdraw(self, amount, description=""):
        balance = 0
        withdraw_status = True
        for element in self.ledger:
            balance += element["amount"]
        if balance - amount >= 0:
            self.ledger.append({"amount": float("-" + str(amount)), "description": description})
        else:
            withdraw_status = False
        return withdraw_status

    def transfer(self, amount, category):
        transfer_status = True
        if self.get_balance() - amount >= 0:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
        else:
            transfer_status = False
        return transfer_status


food = Category("food")
entertainment = Category("entertainment")
business = Category("business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


def round_down(num, divisor):
    return num - (num % divisor)


def create_spend_chart(categories):
    perc = 100
    categ_perc = {}
    lines = "Percentage spent by category" + f"\n"
    total_spent = 0
    total_spent_by_category = 0
    for category in categories[:]:
        for amount in category.get_ledger():
            if amount['amount'] < 0:
                total_spent_by_category += abs(amount['amount'])
            else:
                continue
        total_spent += total_spent_by_category
        categ_perc[category.get_name()] = total_spent_by_category
        total_spent_by_category = 0
    if len(categ_perc) == len(categories):
        for category in categ_perc:
            categ_perc[category] = round_down((categ_perc[category] * 100 / total_spent), 10)

    while perc != -10:
        o_checker = ""
        for category in categories:
            o_checker += (" " + (" " if categ_perc[category.get_name()] < perc else "o") +
                          (" " if category != categories[len(categories)-1] else "  "))
        lines += f"{perc:>3}|" + o_checker + f"\n"
        perc -= 10
        if perc == -10:
            lines += f"{'-' * (3 * len(categ_perc)+1):>{3 * len(categ_perc) + 5}}\n"
            for i in range(len(max(list(categ_perc.keys()), key=len))):
                lines += "".join([f"{'    ' if category == list(categ_perc.keys())[0] else ''}"
                                  for category in list(categ_perc.keys())])
                if i == 0:
                    lines += "".join([f" {category[i].upper() if i < len(category) else ' '} "
                                      for category in list(categ_perc.keys())])
                else:
                    lines += "".join([f" {category[i] if i < len(category) else ' '} " for category in
                                      list(categ_perc.keys())])
                lines += ' ' if i+1 == len(max(list(categ_perc.keys()), key=len)) else ' \n'
                if i == len(max(list(categ_perc.keys()), key=len)) - 1:
                    break
                else:
                    continue
    return lines


print(create_spend_chart([business, food, entertainment]))
