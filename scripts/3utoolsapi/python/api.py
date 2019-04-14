#!/usr/bin/env python3
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
    
