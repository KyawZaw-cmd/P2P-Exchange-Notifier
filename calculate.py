'''
def get_median_price(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'Median price' in line:
                median_price = float(line.split(': ')[1].replace(',', '').strip())
                return median_price

# Get median prices for USDT @ MMK and USDT @ THB
usdt_mmk = get_median_price('buy_answers.txt')
usdt_thb = get_median_price('sell_answers.txt')

def get_rate(profit_pct):
    thb_to_mmk_rounded = round((1 / usdt_thb) * usdt_mmk, 4)
    final_round = round(thb_to_mmk_rounded * (1 + profit_pct / 100), 2)
    return final_round

# Calculate rates and store them in lists
profit_pct = 1
first, second, third = [get_rate(profit_pct) - x for x in [0, 0.16, 0.2]]
cas = [round(x * 0.99, 2) for x in [first, second, third]]
old = [round(x * 0.99, 2) for x in [first + 0.2, first + 0.04, first - 0.12]]


# Create table data and text for display
#table_data =[cas, old, [first, second, third], [first + 0.2, first + 0.04, first - 0.12]]

table_data = [cas, old, [first, second, third], [round(first + 0.2, 2), round(first + 0.04, 2), round(first - 0.12, 2)]]


text = '- {}(Baht 1000 - Baht 50000 )\n- {}(Baht 50001 - Baht 500,000 ) \n- {} (Baht 500,000 နှင့် အထက် ) \n'
text1 = text.format(*map(str, [first, second, third]))
text2 = text.format(*map(str, [first + 0.2, first + 0.04, first - 0.12]))
text3 = text.format(*map(str, cas))
text4 = text.format(*map(str, old))
final_text = 'Selling Rate\nCash သို့ Special Acc \n{}\nOld Account သို့ Kpay \n{}\nBuying Rate\nCash သို့ Special Acc \n{}\nOld Account သို့ Kpay \n{}'.format(text1, text2, text3, text4)

# Write table data to a file
with open('table_data.txt', 'w') as f:
    for row in table_data:
        f.write('\t'.join(map(str, row)) + '\n')
print(table_data)
'''

'''
def get_median_price(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'Median price' in line:
                median_price = float(line.split(': ')[1].replace(',', '').strip())
                return median_price

# Get median prices for USDT @ MMK and USDT @ THB
usdt_mmk = get_median_price('buy_answers.txt')
usdt_thb = get_median_price('sell_answers.txt')

def get_rate(profit_pct):
    thb_to_mmk = (1 / usdt_thb) * usdt_mmk
    final_round = round(thb_to_mmk * (1 + profit_pct / 100), 4)
    return final_round

# Calculate rates and store them in lists
profit_pct = 1
first, second, third = [round(get_rate(profit_pct) - x, 4) for x in [0, 0.16, 0.2]]
cas = [round(x * 0.99, 4) for x in [first, second, third]]
old = [round(x * 0.99, 4) for x in [first + 0.2, first + 0.04, first - 0.12]]

# Create table data and text for display
table_data = [cas, old, [first, second, third], [round(first + 0.2, 4), round(first + 0.04, 4), round(first - 0.12, 4)]]
text = '- {}(Baht 1000 - Baht 50000 )\n- {}(Baht 50001 - Baht 500,000 ) \n- {} (Baht 500,000 နှင့် အထက် ) \n'
text1 = text.format(*map("{:.4f}".format, [first, second, third]))
text2 = text.format(*map("{:.4f}".format, [first + 0.2, first + 0.04, first - 0.12]))
text3 = text.format(*map("{:.4f}".format, cas))
text4 = text.format(*map("{:.4f}".format, old))
final_text = 'Selling Rate\nCash သို့ Special Acc \n{}\nOld Account သို့ Kpay \n{}\nBuying Rate\nCash သို့ Special Acc \n{}\nOld Account သို့ Kpay \n{}'.format(text1, text2, text3, text4)

# Write table data to a file
with open('table_data.txt', 'w') as f:
    for row in table_data:
        f.write('\t'.join(map(str, row)) + '\n')
print(round(final_round, 2))
'''

#working code
def get_median_price(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'Median price' in line:
                median_price_str = line.split(': ')[1].strip()
                median_price_str = median_price_str.replace(',', '')
                median_price = float(median_price_str)
                return median_price

# get median price for USDT @ MMK
usdt_mmk = get_median_price('buy_answers.txt')
print("USDT @ MMK Median Price:", usdt_mmk)

# get median price for USDT @ THB
usdt_thb = get_median_price('sell_answers.txt')
print("USDT @ THB Median Price:", usdt_thb)

def get_rate(profit_pct):
    thb_to_usdt = 1 / usdt_thb  # calculate the value of 1 THB in USDT
    usdt_to_mmk = usdt_mmk  # the value of 1 USDT in MMK

    thb_to_mmk = thb_to_usdt * usdt_to_mmk  # calculate the value of 1 THB in MMK
    thb_to_mmk_rounded = round(thb_to_mmk, 4)  # round the result to 4 decimal places
    new_round = round(thb_to_mmk_rounded, 2)

    # calculate the profit and add it to the new_round value
    profit_amount = new_round * profit_pct / 100
    new_round_with_profit = new_round + profit_amount
    final_round = round(new_round_with_profit,2)
    return final_round
#profit_pct = float(input("Enter the profit percentage: "))
profit_pct = 1
get_rate(profit_pct)

first = get_rate(profit_pct)
second = round(first - 0.16, 2)
third = round(second - 0.04, 2 )


ratefirst = round(first + 0.2 , 2) 
ratesecond = round(ratefirst - 0.16, 2)
ratethird = round(ratesecond - 0.04, 2 )


cas = [first,second,third]
old =  [ratefirst , ratesecond, ratethird]

# Reduce each value in cas and old by 1%
cas = [x * 0.99 for x in cas]
old = [x * 0.99 for x in old]

# round values in cas and old lists up to 2 decimal places
for i in range(len(cas)):
    cas[i] = round(cas[i], 2)
for i in range(len(old)):
    old[i] = round(old[i], 2)

# Print the updated lists

table_data = [[cas[0], cas[1], cas[2]],
            [old[0],old[1], old[2]],
            [first,second,third],
            [ratefirst , ratesecond, ratethird],]  
print(table_data)
text = '- 85.83(Baht 1000 - Baht 50000 )\n- 85.67(Baht 50001 - Baht 500,000 ) \n- 85.63 (Baht 500,000 နှင့် အထက် ) \n'
text1 = text.replace('85.83', str(first)).replace('85.67', str(second)).replace('85.63', str(third))

text2 = text.replace('85.83', str(ratefirst)).replace('85.67', str(ratesecond)).replace('85.63', str(ratethird))
text3 = text.replace('85.83', str(cas[0])).replace('85.67', str(cas[1])).replace('85.63', str(cas[2]))
text4 = text.replace('85.83', str(old[0])).replace('85.67', str(old[1])).replace('85.63', str(old[2]))
#final_text = '( Cash သို့ Special Acc ) \n' + text + '\n ( Old Account သို့ Kpay )#02 \n' + text1
final_text = 'Selling Rate' + '\n' + 'Cash သို့ Special Acc \n'+ text1 + '\n' + 'Old Account သို့ Kpay \n'+ text2 + '\n' + 'Buying Rate' + '\n' +'Cash သို့ Special Acc \n' + text3 + '\n' + 'Old Account သို့ Kpay \n' + text4

with open('table_data.txt', 'w') as f:
    for row in table_data:
        f.write('\t'.join(map(str, row)) + '\n')

