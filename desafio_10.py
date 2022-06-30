#show how much dollars could someone buy with declared balance

balance = float(input('How much dollars do you have? '))

print('1 dolar equals to R$5,25')

#swap balance
swap_result = balance/5.25

print('You can buy this amount>> Swap result: {:.2f}U$'.format(swap_result))