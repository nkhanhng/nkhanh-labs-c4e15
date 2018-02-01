from gmail import GMail, Message
from random import choice


html_template = '''<p><span style="color: #00ff00;">Should the remedy delay the unable geography? </span></p>
<p><span style="color: #993300;">The ghastly brain perceives the pope below the betting friend.</span></p>
<p><br />An organized anatomy pants. The analogy disadvantages an aware protein.</p>
<p>The <strong>{{someone}}</strong> springs onto the skull.</p>
<p><br />The blame winner notices a manned ozone.</p>'''

template = [
    {
        'html':'''<p>The <strong>{{someone}}</strong> springs onto the skull.</p>''',
        'blah': ['']
    }
]

someone_list = ['monkey','elephant','dog']

html_con = html_template.replace('{{someone}}',choice(someone_list))

gmail = GMail('khanhmatden123@gmail.com','kingofwar123')
msg = Message('Test Message',to='c4e.201708@gmail.com',html = html_con)
gmail.send(msg)
