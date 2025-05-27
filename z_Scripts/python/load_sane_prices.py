import csv
from pathlib import Path
def main():
    with open("./z_Scripts/sane-pricelist.csv") as csv_file:
            not_found = []
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                price = row[2].replace("gp", "").strip()
                print(f"Found item: <{row[1]}>")
                file = Path(f"./DND SRD/Wondrous Items/{row[1]}.md")

                if file.is_file():
                    print("\tfile is a file")
                    addPrice(file, price)
                else:
                    name_attempt = row[1].split("(")[0].strip()
                    file = Path(f"./DND SRD/Wondrous Items/{name_attempt}.md")
                    if file.is_file():
                        print("Found file now")
                        addPrice(file, price)
                    else: 
                        not_found.append(row[1])
    
    print("Not Found Items:")
    for item in not_found:
        print(f"\t{item}")

def addPrice(in_file, price):
    with open(in_file, "r", encoding="utf-8") as fp:
        lines = fp.readlines()

    print(f"\tPrice: {price}")
    with open(in_file, "w", encoding="utf-8") as fp:
        for i in range(len(lines)):
            if "type: " in lines[i]:
                fp.write(lines[i])
                fp.write(f"price: {price}\n")
            else:
                fp.write(lines[i])

if __name__ == "__main__":
    main()