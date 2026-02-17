from datetime import datetime

class Expense:
    def __init__(self, name, category, amount, date=None):
        self.name = name
        self.category = category
        self.amount = amount
        
        # ✅ Auto-generate date if not provided
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"<Expense Name: {self.name}, "
            f"Category: {self.category}, "
            f"Amount: {self.amount}, "
            f"Date: {self.date}>"
        )
