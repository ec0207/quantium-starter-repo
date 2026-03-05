import csv

def main():
    with open('output_sales_data.csv', 'w', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=['sales', 'date', 'region'])
        writer.writeheader()
        for i in range(3):
            # Load datasets
            with open(f"./data/daily_sales_data_{i}.csv", newline='') as f:
                reader = csv.DictReader(f)
                for row in reader: 
                    if row['product'] == 'pink morsel':
                        writer.writerow({'sales': int(row['quantity']) * float(row['price'][1:]), 'date': row['date'], 'region': row['region'].strip()})               

main()