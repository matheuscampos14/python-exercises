class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description})
    def withdraw (self, amount, description = ''):
        if self.get_balance() < amount:
            return False
        self.ledger.append({
            'amount': - amount,
            'description': description})
        return True
    def get_balance(self):
        total = 0
        for ledge in self.ledger:
            total += ledge['amount']
        return total
    def transfer(self, amount, category):
        if not self.withdraw(amount, f'Transfer to {category.name}'):
            return False
        category.deposit(amount,f'Transfer from {self.name}')
        return True
    def check_funds(self, amount):
        total = 0
        for ledge in self.ledger:
            total += ledge['amount']
        if amount > total:
            return False
        return True
    def __str__(self):
        string1 =  f'{self.name:*^30}'
        if not self.ledger:
            string_ledger = "".join("\nEmpty Ledger")
        else:
            lines = []
            for ledge in self.ledger:
                lines.append(f"{ledge['description'][:23]:<23}{ledge['amount']:>7.2f}")
            string_ledger = '\n' + '\n'.join(lines)
        string2 = f'\nTotal: {self.get_balance()}'
        return string1 + string_ledger + string2

def create_spend_chart(categories):
    withdrawals = []
    # calcula quanto cada categoria gastou
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        withdrawals.append(spent)
    # total gasto entre todas categorias
    total_spent = sum(withdrawals)
    percentages = []
    for spent in withdrawals:
        percent = (spent / total_spent * 100)//10*10
        percentages.append(percent)
    chart = 'Percentage spent by category\n'
    # eixo vertical
    for label in range(100, -1, -10):
        line = f"{label:>3}|"
        for percent in percentages:
            if percent >= label:
                line += ' o '
            else:
                line += '   '
        line += ' \n'
        chart += line
    # linha horizontal
    chart += '    '
    chart += '-' * (len(categories) * 3 + 1)
    chart += '\n'
    # tamanho do maior nome
    max_length = max(len(category.name) for category in categories)
    # nomes na vertical
    for i in range(max_length):
        line = '     '
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + '  '
            else:
                line += '   '
        # evita quebra de linha extra no final
        if i != max_length - 1:
            line += '\n'
        chart += line
    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))

