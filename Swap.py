# Python program to swap two variables

# To take input from the user
# x = input('Enter value of x: ')
# y = input('Enter value of y: ')

x = 15
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
