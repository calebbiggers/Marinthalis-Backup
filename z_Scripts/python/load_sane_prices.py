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

                item_name = row[1].strip().replace(" Of ", " of ")
                price = row[2].replace("gp", "").strip()

                if not price.isdigit():
                    print(f"[WARNING] - Invalid price for item: {row[1]}. Skipping...")
                    not_found.append([item_name, price])
                    continue

                print(f"[LOG] - Found item in csv file: <{item_name}> with price: {price}")
                file = Path(f"./Wondrous Items/{item_name}.md")

                if file.is_file():
                    print(f"[LOG] - File found for item: <{item_name}>")
                    #addPrice(file, price)
                    continue
                else:
                    print(f"[WARNING] - File not found for item: {item_name}. Attempting to find file...")
                    
                    # Try removing parenthesis
                    no_parenthesis_attempt = item_name.split("(")[0].strip()
                    file = Path(f"./Wondrous Items/{no_parenthesis_attempt}.md")
                    print(f"[LOG] - Attempting to find file: <{no_parenthesis_attempt}>")
                    if file.is_file():
                        print(f"[LOG] - File found for item: <{no_parenthesis_attempt}>")
                        #addPrice(file, price)
                        continue
                    
                    # Add to list of not found items
                    not_found.append([item_name, price])


    
    print(f"[WARNING] - Not Found Items:")
    for item in not_found:
        print(f"\t{item}")

def addPrice(in_file, price):
    with open(in_file, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    
    # Check if the file already has a price
    if any("price:" in line for line in lines):
        print(f"[WARNING] - File already has a price: {in_file}. Replacing it...")
        has_price = True
    else:   
        print(f"[LOG] - Adding price to file: {in_file}")
        has_price = False

    with open(in_file, "w", encoding="utf-8") as fp:
        # Iterate through the lines and add price where appropriate
        for i in range(len(lines)):
            if has_price:
                # File already has a price, so replace it
                if "price: " in lines[i]:
                    fp.write(f"price: {price}\n")
                else:
                    fp.write(lines[i])
            else:
                # File does not have a price, insert it
                if "type: " in lines[i]:
                    fp.write(lines[i])
                    fp.write(f"price: {price}\n")
                else:
                    fp.write(lines[i])




            

if __name__ == "__main__":
    main()