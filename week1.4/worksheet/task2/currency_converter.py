
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

proceed=True

while proceed:
    amount=float(input("enter amount you want to convert"))
    from_currency=str(input("enter currency you are converting from"))
    to_currency=str(input("enter currency you are converting to"))

    def currency_converter(amount, from_currency, to_currency):
        if amount <0:
            return float(0)

        conversion_rate = {
            'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
            'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
            'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
            'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
        }

        conversion_rate = conversion_rate[from_currency]
        conversion_rate=conversion_rate[to_currency]
        converted_amount=conversion_rate*amount
    #    print(conversion_rate['GBP'])
        # your code here

        return converted_amount

    x = round(currency_converter(amount,from_currency,to_currency),2)

    print(f"{amount:.2f} {from_currency} is {x:.2f} {to_currency}")
# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
