#rental car price

driven_km = float(input('How much km driven: '))
days_used = int(input('How many days: '))

print('Knowing that it costs R$60,00 per day and R$0,15 per km driven...')

#price to pay summing km driven and days used
price_to_pay = 0.15*driven_km + days_used*60

print('You owe {:.2f}R$ to Parish Rental Car Business'.format(price_to_pay))
