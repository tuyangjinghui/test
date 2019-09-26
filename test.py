#!/usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.baidu.com')
html = r.content.decode('utf-8')
print(html)