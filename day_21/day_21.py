#Day 21 of 30 days with python

class Statistics :
    def __init__(self, data):
        self.data = sorted(data)
        
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return self.data[0]
    
    def max(self):
        return self.data[-1]
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]
    
    def mode(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        return modes if len(modes) > 1 else modes[0]
    
    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()
    
    def std_deviation(self):
        return self.variance() ** 0.5
    
    def percentile(self, p):
        if not 0 <= p <= 100:
            raise ValueError("Percentile must be between 0 and 100")
        k = (len(self.data) - 1) * (p / 100)
        f = int(k)
        c = min(f + 1, len(self.data) - 1)
        return self.data[f] + (self.data[c] - self.data[f]) * (k - f)
    
    def frequency_distribution(self):
        freq = {}
        for num in self.data:
            freq[num] = freq.get(num, 0) + 1
        return dict(sorted(freq.items()))
    
    def describe(self):
        return {
            "Count": self.count(),
            "Sum": self.sum(),
            "Min": self.min(),
            "Max": self.max(),
            "Range": self.range(),
            "Mean": self.mean(),
            "Median": self.median(),
            "Mode": self.mode(),
            "Variance": self.variance(),
            "Standard Deviation": self.std_deviation(),
            "25th Percentile": self.percentile(25),
            "50th Percentile": self.percentile(50),
            "75th Percentile": self.percentile(75),
            "Frequency Distribution": self.frequency_distribution()
        }
        
        
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print(Statistics(ages).describe())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []   # List of tuples (amount, description)
        self.expenses = []  # List of tuples (amount, description)
    
    def add_income(self, amount, description):
        self.incomes.append((amount, description))
    
    def add_expense(self, amount, description):
        self.expenses.append((amount, description))
    
    def total_income(self):
        return sum(amount for amount, _ in self.incomes)
    
    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        info = f"Account Owner: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        
        info += "\n--- Incomes ---\n"
        for amount, desc in self.incomes:
            info += f"{desc}: {amount}\n"
        
        info += "\n--- Expenses ---\n"
        for amount, desc in self.expenses:
            info += f"{desc}: {amount}\n"
        
        return info


# Example usage
person = PersonAccount("James", "Amouzou")
person.add_income(2000, "Salary")
person.add_income(500, "Freelance")
person.add_expense(800, "Rent")
person.add_expense(200, "Groceries")



class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []   # List of tuples (amount, description)
        self.expenses = []  # List of tuples (amount, description)
    
    def add_income(self, amount, description):
        self.incomes.append((amount, description))
    
    def add_expense(self, amount, description):
        self.expenses.append((amount, description))
    
    def total_income(self):
        return sum(amount for amount, _ in self.incomes)
    
    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        info = f"Account Owner: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        
        info += "\n--- Incomes ---\n"
        for amount, desc in self.incomes:
            info += f"{desc}: {amount}\n"
        
        info += "\n--- Expenses ---\n"
        for amount, desc in self.expenses:
            info += f"{desc}: {amount}\n"
        
        return info


# Example usage
person = PersonAccount("James", "Amouzou")
person.add_income(2000, "Salary")
person.add_income(500, "Freelance")
person.add_expense(800, "Rent")
person.add_expense(200, "Groceries")
