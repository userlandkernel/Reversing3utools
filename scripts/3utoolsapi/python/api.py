#!/usr/bin/env python3

# Yes, 3utools does not need any API key how excellent and polite!
# Let's build something beautiful out of the API, definitly not this crappy script I wrote in a minute.

import os
import sys
import requests

class TreeUAPI:
  def __init__(self):
    self.apibase = 'http://app.pcres.3u.com/'
    self.actions = ['firmware_list', 'firmware_iosVersion']
  
  def firmware_list(self, model='', fs='', seltype='', ios=''):
    url = self.apibase + 'firmware_list.action?'
    if model != '':
      url += '&model=' + str(model)
    
    if fs != '':
      url += '&fs=' + str(fs)
    
    if seltype != '':
      url += '&seltype=' + str(seltype)
      
    if ios != '':
      url += '&ios=' + str(ios)
    
    response = requests.get(url)
    print(response.text)
    
