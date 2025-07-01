import requests
import calculate
import configparser
import logging
import textgenerator

logging.basicConfig(filename='tbotlog.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Read the config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get the Telegram Bot token from the config file
        tk = config.get('BotSettings', 'token')

        # Build the API URL with the token
        base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-1001744319698&'.format(tk)
        new_url = base_url + 'text={}'.format(textgenerator.f_text)

        # Send the message using the API URL
        requests.get(new_url)
        logging.info("Success message: " + new_url)
        print("Success message: " + new_url)
    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error: ", e)

if __name__ == '__main__':
    main()




'''import requests
import calculate


def main():
    base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-1001744319698&'.format(tk)
    new_url = base_url + 'text={}'.format(calculate.final_text)
    requests.get(new_url)
    print("Success message: " + new_url)

if __name__ == '__main__':
    with open('config.txt',encoding="utf8") as f:
        tk = f.read()
    main()
'''

'''
import requests

def main():
    base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-1001744319698&'.format(tk)
    new_url = base_url + 'text={}'.format(message)
    requests.get(new_url)
    print("Success message: " + new_url)

if __name__ == '__main__':
    with open('message.txt', encoding="utf8" ) as f:
        message = f.read()

    with open('config.txt',encoding="utf8") as f:
        tk = f.read()
    main()
'''

'''
import requests

def main():
    with open('message.txt', encoding="utf8") as f:
        message = f.read()
        
        with open('config.txt', encoding="utf8") as f:
            tk = f.read()

        usdt_mmk = float(input("Enter the exchange rate of 1 USDT to MMK: "))
        usdt_thb = float(input("Enter the exchange rate of 1 USDT to THB: "))

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
            print("1 THB = {} MMK".format(final_round))
            return final_round

        profit_pct = float(input("Enter the profit percentage: "))
        first = get_rate(profit_pct)
        second = round(first - 0.16, 2)
        third = round(second - 0.04, 2)

        ratefirst = first + 0.2
        ratesecond = round(ratefirst - 0.16, 2)
        ratethird = round(ratesecond - 0.04, 2)

        text = '- 85.83(Baht 1000 - Baht 50000 )\n- 85.67(Baht 50001 - Baht 500,000 ) \n- 85.63 (Baht 500,000 +)'
        text = text.replace('85.83', str(first)).replace('85.67', str(second)).replace('85.63', str(third))

        text1 = text.replace('85.83', str(ratefirst)).replace('85.67', str(ratesecond)).replace('85.63', str(ratethird))

        final_text = '( Cash သို့ Special Acc ) \n' + text + '\n ( Old Account သို့ Kpay )#02 \n' + text1
        
        base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-1001744319698&'.format(tk)
        new_url = base_url + 'text={}'.format(final_text)
        requests.get(new_url)
        print("Success message: " + new_url)

if __name__ == '__main__':
    main()
print('Final Text: ', final_text)
'''