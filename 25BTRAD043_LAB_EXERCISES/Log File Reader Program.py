filename = "app.log"

try:
    with open(filename, "r") as file:
        content = file.read()

    print("Log Summary:")
    print("INFO    :", content.count("INFO"))
    print("WARNING :", content.count("WARNING"))
    print("ERROR   :", content.count("ERROR"))

except FileNotFoundError:
    print(f"Error: {filename} not found.")