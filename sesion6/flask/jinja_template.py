from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime

def render_email(**data):
	with open('email_template.eml') as f:
		template = Template(f.read())
		return template.render(**data)

data = {'date': format_datetime(datetime.now()),'to': 'user1@domain.com',
'from': 'user1@domain.com','subject': "Testing email",'name': 'User',
'items': [{'name': 'product1', 'price': 10},{'name': 'product2', 'price': 20},{'name': 'Product3', 'price': 30}]}

print(render_email(**data))

