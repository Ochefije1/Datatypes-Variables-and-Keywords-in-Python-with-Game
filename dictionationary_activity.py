# you can also use the {} to define a dictionary
# currency = {
#         'USD': {'NGN':740, 'CAD':600, 'YEN':400, 'CEDI':100},
#         'CFA': {'USD':740, 'CAD':600, 'YEN':400, 'CEDI':100}
#         }


# print(currency.keys())
# print(currency.values())
# print(currency.items())

# for currency:

# def exchangeConverter(amount, symbol):
#     pass



currency = {
    'USD': {'NGN':740, 'CAD':600, 'YEN':400, 'CEDI':100},
    'CFA': {'USD':740, 'CAD':600, 'YEN':400, 'CEDI':100}
}

def exchangeConverter(amount, symbol):
    base, value = symbol.split('/')
    return currency[base][value] * amount

print(exchangeConverter(200, 'USD/CEDI'))



def exchangeConverter(amount, symbol):
    base, value = symbol.split('/')
    base_value = currency[base]
    rate = base_value[value]
    converted_amount = rate * amount
    return converted_amount

converted_rate = exchangeConverter(200, 'USD/CEDI')
print(converted_rate)
