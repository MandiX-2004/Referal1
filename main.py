from income import IncomeRecord
from file_exporter import export_to_csv
from utils import validate_code

income_records = []

def find_by_code(code):
    for record in income_records:
        if record.code == code:
            return record
    return None

def add_income():
    code = input("Enter Income Code (e.g., IN001): ").upper()
    if not validate_code(code, [r.code for r in income_records]):
        print("Invalid or duplicate code.")
        return
    desc = input("Enter Description (max 20 chars): ")[:20]
    date = input("Enter Date (dd/mm/yyyy): ")
    try:
        amount = float(input("Enter Income Amount: "))
        wht = float(input("Enter WHT Amount: "))
    except ValueError:
        print("Invalid numbers.")
        return
    income_records.append(IncomeRecord(code, desc, date, amount, wht))
    print("Income added.")

def delete_income():
    code = input("Enter Code to Delete: ").upper()
    record = find_by_code(code)
    if record:
        income_records.remove(record)
        print("Deleted.")
    else:
        print("Not found.")

def update_income():
    code = input("Enter Code to Update: ").upper()
    record = find_by_code(code)
    if not record:
        print("Not found.")
        return
    record.description = input("Enter New Description (max 20 chars): ")[:20]
    record.date = input("Enter New Date (dd/mm/yyyy): ")
    record.income_amount = float(input("Enter New Income Amount: "))
    record.wht_amount = float(input("Enter New WHT Amount: "))
    print("Updated.")

def search_income():
    code = input("Enter Code to Search: ").upper()
    record = find_by_code(code)
    if record:
        print(f"Code: {record.code}\nDescription: {record.description}\nDate: {record.date}")
        print(f"Income: {record.income_amount:.2f}, WHT: {record.wht_amount:.2f}, Checksum: {record.compute_checksum()}")
    else:
        print("Not found.")

def main_menu():
    while True:
        print("\n=== Income Recording Client System (IRCS) ===")
        print("1. Add Income")
        print("2. Delete Income")
        print("3. Update Income")
        print("4. Search Income")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Choose option: ")
        if choice == '1':
            add_income()
        elif choice == '2':
            delete_income()
        elif choice == '3':
            update_income()
        elif choice == '4':
            search_income()
        elif choice == '5':
            export_to_csv(income_records)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
