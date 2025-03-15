"""
! category : easy
TODO : Create a program that generates a digital identity card using the concept of string concatenation. Your program will combine several pieces of personal information into one formatted text. Input : First name: "John", Last name: "Doe", Age: 25, Occupation: "Software Developer", City: "New York". Tasks : Combine the first name and last name to create a full name using the + operator with a space between them. Create a string that displays the age in the format "Age: X years" using concatenation with the + operator. Combine the occupation information with an introductory sentence using a concatenation method of your choice. Combine the location in the format "Location: [city]" using a concatenation method of your choice. Finally, combine all the above information into an "identity card" separated by new lines (\n).
"""

first_name = "John"
last_name = "Doe"
age = 25
occupation = "Software Developer"
city = "New York"

print(
    f"identity card\n===============================\nname : {first_name + ' ' + last_name}\nage : {'%s%s' % (age, ' years')}\noccupation : {occupation}\nlocation : {city}\n===============================\n"
)

"""
! category : medium
TODO : Create a program that generates marketing messages for various products using different string concatenation techniques. Input : customer_name = "Alex", product = "SmartWatch Pro", regular_price = 299.99, discount = 15  # in percentage, voucher_code = "TECH15", expiration_date = "April 25, 2025".Tasks : Create a personalized greeting line that includes the customer's name using f-string. Calculate the price after discount (regular price minus discount percentage) and store it in a variable. Create a string that displays the product information and regular price using the .format() method. Create a string that displays the discount amount and the price after discount using concatenation with the + operator. Create a string that displays the voucher code surrounded by * symbols using the string repetition operator (*). Create a deadline message that shows the expiration date using concatenation. Combine all the above strings to create a complete marketing message.
"""

customer_name = "Alex"
product = "SmartWatch Pro"
regular_price = 299.99
discount = 15
voucher_code = "TECH15"
expiration_date = "25 April 2025"

welcome = f"Halo {customer_name}! we have a special offer for you!"
total_discount = regular_price * discount / 100
price_after_discount = regular_price - total_discount
info_product = "product : {}\nnormal price : ${:.2f}".format(product, regular_price)

info_discount = (
    "you save : $"
    + str("{:.2f}".format(total_discount))
    + " ("
    + str(discount)
    + "%)"
    + "\nspecial price : $"
    + str("{:.2f}".format(price_after_discount))
)

info_voucher = "use the code : " + "*" * 3 + voucher_code + "*" * 3
deadline = "The offer ends on : " + expiration_date
close = "thank you for being our loyal customer!"
symbol = "-" * 39

message = (
    welcome
    + "\n\n"
    + "PENAWARAN SPESIAL"
    + "\n"
    + symbol
    + "\n"
    + info_product
    + "\n"
    + info_discount
    + "\n\n"
    + info_voucher
    + "\n\n"
    + deadline
    + "\n\n"
    + close
    + "\n"
    + symbol
)

print(message)
