from gmail import GMail, Message
from random import choice
import datetime
import re


html_template = '''<p style="text-align: center;"><strong>Xin nghi om</strong></p>
<p style="text-align: left;">&nbsp;</p>
<p>Em chao anh,</p>
<p>Hom nay em thuc day thay rat dau dau, chong mat va buon non.</p>
<p>Em đi kham, bac si chẩn đoan bi <em><strong>{{sickness}}</strong></em>.</p>
<p>Cho em nghi anh nhe.</p>
<p>Em cam on</p>
'''
sick_list = ['Cam cum','Sot ret','Ebola']

ran = choice(sick_list)

html_con = html_template.replace('{{sickness}}',ran)

gmail = GMail('khanhmatden123@gmail.com','kingofwar123')
msg = Message('Test Message',to='Taken.jb@gmail.com',html = html_con)


time = datetime.datetime.now()
check = datetime.time(time.hour,time.minute)
time_to_send = datetime.time(7,0)


while True:
    if check == time_to_send:
        gmail.send(msg)
        break
