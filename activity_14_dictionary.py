currency = {
  'USD': {'NGN':740, 'CAD':600, 'YEN':400, 'CEDI': 100}
  'CFA': {'USD':740, 'CAD':600, 'YEN':400, 'CEDI': 100}
  }


#for item in currency.items():
 # currency, exc = item
#print(exc['YEN'])


  pass # To save code for future use


#create a function that will take amount and return the converter rate using python


def exchangeConverter(amount, symbol):
  base, value = symbol.split('/')
  base_value = currency[base]
  rate = base_value[value]
  converted_amount = rate * amount
  return converted_amount
converted_rate = exchangeConverter(200, 'USD/CEDI')
print(converted_rate)
   