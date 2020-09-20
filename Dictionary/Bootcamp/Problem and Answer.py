# To get value from dictionary for the given key
d = {10: 'dutta', 20: 'rani', 50: 'dey', 40: 'krish'}

key = int(input('Enter the key to get the value:'))
if key in d:
    print('The corresponding value to the key is ::', d.get(key))
else:
    print('The specified key is not available in the dictionary')

# to get key from the dictionary for the given value
value = input('Enter the value to find the key::')
available = False
for k, v in d.items():
    if v == value:
        print('The corresponding key is ::',k)
        available = True
if available == False:
    print('The specified value is not found in the dictionary')
