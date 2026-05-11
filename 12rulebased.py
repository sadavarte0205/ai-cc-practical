responses = {
    "price": "The product price is 500 Rs",
    "delivery": "Delivery takes 3 days",
    "hello": "Hi, Welcome"
}

while True:

    user = input("Enter query: ")

    if user in responses:
        print(responses[user])

    elif user == "exit":
        break

    else:
        print("Sorry, no response found")