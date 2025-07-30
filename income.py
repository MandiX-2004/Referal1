class IncomeRecord:
    def __init__(self, code, description, date, income_amount, wht_amount):
        self.code = code
        self.description = description
        self.date = date
        self.income_amount = float(income_amount)
        self.wht_amount = float(wht_amount)

    def to_csv_line(self):
        return f"{self.code},{self.description},{self.date},{self.income_amount:.2f},{self.wht_amount:.2f}"

    def compute_checksum(self):
        line = self.to_csv_line()
        capital_count = sum(1 for c in line if c.isupper())
        numeric_count = sum(1 for c in line if c.isdigit() or c == '.')
        return capital_count + numeric_count


