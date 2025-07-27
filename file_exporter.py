def export_to_csv(income_records, filename="income_sheet.csv"):
    with open(filename, "w") as f:
        for record in income_records:
            line = record.to_csv_line()
            checksum = record.compute_checksum()
            f.write(f"{line},{checksum}\n")
    print(f"Exported to {filename}")
