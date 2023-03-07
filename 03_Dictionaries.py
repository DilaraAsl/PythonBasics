employees = {"chef": "Annie", "ceo": "George"}
print(employees["ceo"])
#  add a new key value pair
employees["waiter"] = 'Mike'

print(employees["waiter"])

# update an existing key value
employees["chef"] = "Jose"
print(employees)

print(employees["waiter"].upper())

stock_prices = {"GOOGL": [200, 210, 220], "GME": [20, 100, 300]}
history = stock_prices["GOOGL"]

print(f"First day price is : {history[0]}")

mydict = {"OUTER": {"INNER": 100}}
print(mydict["OUTER"]["INNER"])

mydict = {'key1': 100, 'key2': 200, 'key3': 400}
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict['key4'] = 400
print(mydict.items())
