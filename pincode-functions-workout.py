Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests

url = "https://api.postalpincode.in/pincode/"
mypincode = 500001

call_url = url+str(mypincode)
call_url
'https://api.postalpincode.in/pincode/500001'

resp = requests.get(call_url)
resp
<Response [200]>
data = resp.json()
data
[{'Message': 'Number of pincode(s) found:5', 'Status': 'Success', 'PostOffice': [{'Name': 'Gandhi Bhawan (Hyderabad)', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Hyderabad ', 'Description': None, 'BranchType': 'Head Post Office', 'DeliveryStatus': 'Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad GPO', 'Region': 'Hyderabad City', 'Block': 'Hyderabad', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Moazzampura', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Seetharampet', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'State Bank Of Hyderabad', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}]}]

data.keys)_
SyntaxError: unmatched ')'
data.keys()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.keys()
AttributeError: 'list' object has no attribute 'keys'

data[0]
{'Message': 'Number of pincode(s) found:5', 'Status': 'Success', 'PostOffice': [{'Name': 'Gandhi Bhawan (Hyderabad)', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Hyderabad ', 'Description': None, 'BranchType': 'Head Post Office', 'DeliveryStatus': 'Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad GPO', 'Region': 'Hyderabad City', 'Block': 'Hyderabad', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Moazzampura', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Seetharampet', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'State Bank Of Hyderabad', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}]}


data[0].keys()
dict_keys(['Message', 'Status', 'PostOffice'])

data[0].get('message']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
data[0].get('message')

data[0].get('Message')
'Number of pincode(s) found:5'
data[0].get('PostOffice')
[{'Name': 'Gandhi Bhawan (Hyderabad)', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Hyderabad ', 'Description': None, 'BranchType': 'Head Post Office', 'DeliveryStatus': 'Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad GPO', 'Region': 'Hyderabad City', 'Block': 'Hyderabad', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Moazzampura', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'Seetharampet', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}, {'Name': 'State Bank Of Hyderabad', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}]
data[0].get('PostOffice')[]
SyntaxError: invalid syntax
data[0].get('PostOffice')[0]
{'Name': 'Gandhi Bhawan (Hyderabad)', 'Description': None, 'BranchType': 'Sub Post Office', 'DeliveryStatus': 'Non-Delivery', 'Circle': 'Andhra Pradesh', 'District': 'Hyderabad', 'Division': 'Hyderabad City', 'Region': 'Hyderabad City', 'Block': 'Nampally', 'State': 'Telangana', 'Country': 'India', 'Pincode': '500001'}

data[0].get('PostOffice')[0].get('Name')
'Gandhi Bhawan (Hyderabad)'



def pincode(your_pincode_number):
    url = "https://api.postalpincode.in/pincode/"
    apilink = url+your_pincode_number
    resp=requests.get(apilink)

def pincode(your_pincode_number):
    url = "https://api.postalpincode.in/pincode/"
    apilink = url+your_pincode_number
    resp=requests.get(apilink)
    data = resp.json()
    results = {}
    results['total responses']=data[0].get('Message')
    results['Area name'] = data[0].get('PostOffice')[0].get('Name')
    results['pincode'] = your_pincode_number
    return results



pincode(500005)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    pincode(500005)
  File "<pyshell#45>", line 3, in pincode
    apilink = url+your_pincode_number
TypeError: can only concatenate str (not "int") to str
>>> pincode('500005')
{'total responses': 'Number of pincode(s) found:5', 'Area name': 'Balapur', 'pincode': '500005'}
>>> 
>>> def pincode(your_pincode_number):
...     url = "https://api.postalpincode.in/pincode/"
...     apilink = url+str(your_pincode_number)
...     resp=requests.get(apilink)
...     data = resp.json()
...     results = {}
...     results['total responses']=data[0].get('Message')
...     results['Area name'] = data[0].get('PostOffice')[0].get('Name')
...     results['pincode'] = your_pincode_number
...     return results
... 
>>> pincode(500035)
{'total responses': 'Number of pincode(s) found:3', 'Area name': 'Huda Residential Complex', 'pincode': 500035}
