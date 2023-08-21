class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = f"{'*' * 30}\n{self.category.center(30, '*')}\n"
        for item in self.ledger:
            output += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    spendings = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spendings)
    percentages = [(spending / total_spent) * 100 if total_spent > 0 else 0 for spending in spendings]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"
    
    max_category_name_length = max(len(category.category) for category in categories)
    category_names = [category.category.ljust(max_category_name_length) for category in categories]

    for i in range(max_category_name_length):
        chart += "     "
        for name in category_names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")


# Testing the Category class
if __name__ == "__main__":
    food_category = Category("Food")
    clothing_category = Category("Clothing")
    auto_category = Category("Auto")

    food_category.deposit(1000, "initial deposit")
    food_category.withdraw(10.15, "groceries")
    food_category.withdraw(15.89, "restaurant and more food")
    food_category.transfer(50, clothing_category)
    
    clothing_category.deposit(500, "initial deposit")
    clothing_category.transfer(50, food_category)
    
    print(food_category)
    print(clothing_category)
    print(auto_category)

    # Testing the create_spend_chart function
    categories = [food_category, clothing_category, auto_category]
    chart = create_spend_chart(categories)
    print(chart)
