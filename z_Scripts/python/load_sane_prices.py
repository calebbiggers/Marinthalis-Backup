import csv
from pathlib import Path

def main():
    with open("./z_Scripts/sane-pricelist.csv") as csv_file:
            not_found = []
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                # Skip header row
                if row[1] == "Item":
                    continue

                price = row[2].replace("gp", "").strip()
                print(f"[LOG] - Found item in csv file: <{row[1]}>")
                file = Path(f"./Wondrous Items/{row[1]}.md")

                if file.is_file():
                    print(f"\t[LOG] - File found for item: <{row[1]}>")
                    addPrice(file, price)
                    continue
                else:
                    print(f"[WARNING] - File not found for item: {row[1]}. Attempting to find file...")
                    
                    no_parenthesis_attempt = row[1].split("(")[0].strip()
                    print(f"[LOG] - Attempting to find file: <{no_parenthesis_attempt}>")

                    replace_of_attempt = row[1].replace(" Of ", "of").strip()
                    print(f"[LOG] - Attempting to find file: <{replace_of_attempt}>")


    
    print(f"[WARNING] - Not Found Items:")
    for item in not_found:
        print(f"\t{item}")

def addPrice(in_file, price):
    with open(in_file, "r", encoding="utf-8") as fp:
        lines = fp.readlines()

    with open(in_file, "w", encoding="utf-8") as fp:
        for i in range(len(lines)):
            if "type: " in lines[i]:
                fp.write(lines[i])
                fp.write(f"price: {price}\n")
            else:
                fp.write(lines[i])

if __name__ == "__main__":
    main()