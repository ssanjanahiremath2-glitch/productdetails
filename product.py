
import sys

def product_details(pid, name, quantity, price):
    return (
        f"Product ID: {pid}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

if __name__ == "__main__":
    pid = sys.argv[1]
    name = sys.argv[2]
    quantity = sys.argv[3]
    price = sys.argv[4]

    print("\nProduct Details")
    print("---------------------")
    print(product_details(pid, name, quantity, price))
