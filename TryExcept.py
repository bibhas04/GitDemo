try:
    with open('test.txt', 'r') as reader:
        reader.read()

except:
    print('There is an error in Try block')

# This will show the exact message which Python actually got:

try:
    with open('abc.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('This block will be executed if there is an error or no error')
