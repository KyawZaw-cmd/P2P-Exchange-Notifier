
import calculate
from datetime import datetime
from pytz import timezone

with open('custom_text.txt', 'r', encoding='utf-8') as f:
    c_text = f.read()
with open('custom_text1.txt', 'r', encoding='utf-8') as f:
    c_text1 = f.read()

text = '- 85.83(Baht 1000 - Baht 50000 )\n- 85.67(Baht 50001 - Baht 500,000 ) \n- 85.63 (Baht 500,000 နှင့် အထက် ) \n'
text1 = text.replace('85.83', str(calculate.first)).replace('85.67', str(calculate.second)).replace('85.63', str(calculate.third))

text2 = text.replace('85.83', str(calculate.ratefirst)).replace('85.67', str(calculate.ratesecond)).replace('85.63', str(calculate.ratethird))
text3 = text.replace('85.83', str(calculate.cas[0])).replace('85.67', str(calculate.cas[1])).replace('85.63', str(calculate.cas[2]))
text4 = text.replace('85.83', str(calculate.old[0])).replace('85.67', str(calculate.old[1])).replace('85.63', str(calculate.old[2]))

final_text = 'Selling Rate' + '\n' + 'Cash သို့ Special Acc \n'+ text1 + '\n' + 'Old Account သို့ Kpay \n'+ text2 + '\n' + 'Buying Rate' + '\n' +'Cash သို့ Special Acc \n' + text3 + '\n' + 'Old Account သို့ Kpay \n' + text4

# Decode the encoded emoji in the final text
#final_text = bytes(final_text, 'utf-8').decode('unicode_escape')

tz = timezone('Asia/Yangon')
now = datetime.now(tz)
date_time_string = now.strftime("%m/%d/%Y %H:%M")

# Specify position and format of the date and time text
date_time_position = (770, 760)
date_time_format = "{}"


f_text = c_text + '\n'  + 'ယနေ့' + date_time_string + 'ငွေလဲစျေးနှန်းလေးတွေပါ ' + '\n' + final_text + '\n' + c_text1
# Draw the date and time on the image
f_text1 =  c_text + '\n'  + 'ယနေ့' + date_time_string + 'ငွေလဲစျေးနှုန်းတွေကိုအောက်ကပုံလေးမှာကြည့်လို့ရပါတယ်နော် ' + '\n' + c_text1

print(f_text)





