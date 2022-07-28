from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio import start_server


import pywebio 

country2city = {
    'China': ['Beijing', 'Shanghai', 'Hong Kong'],
    'USA': ['New York', 'Los Angeles', 'San Francisco'],
    }

countries = list(country2city.keys())


info = input_group('user info', [
    input("Input password", type=PASSWORD, name='password'),

    # Drop-down selection
    select('Which gift you want?', ['keyboard', 'ipad'], name='gift'),

    # Checkbox
    checkbox("User Term", options=['I agree to terms and conditions'], name='agree'),

    # Single choice
    radio("Choose one", options=['A', 'B', 'C', 'D'], name='answer'),
    
    # sideer raio 
    slider('slider: ', name='slider'),

    # Multi-line text input
    textarea('Text Area', rows=3, placeholder='Some text', name='text'),

    # File Upload
    file_upload("Select a image:", accept="image/*", name='file'),
    
    
 
    select('Country', options=countries, name='country',
        onchange=lambda c: input_update('city', options=country2city[c])),

    select('City', options=country2city[countries[0]], name='city')
    
])

pywebio.start_server(port=80)



