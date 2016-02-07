# -*- coding: utf-8 -*-

import yaml as ya


URL_LIST_SAMPLE = """
name: СНС Росстата
url: http://www.gks.ru/free_doc/new_site/vvp/
files:
 - tab1.xls
 - tab2.xls
 - tab2a.xls
 - tab3.xls
 - tab4.xls
 ---
# СНС Росстата
- http://www.gks.ru/free_doc/new_site/vvp/
-
 - tab1.xls
 - tab2.xls
 - tab2a.xls
 - tab3.xls
 - tab4.xls
---
- http://www.cbr.ru/statistics/credit_statistics/M2-M2_SA.xlsx
---
http://www.cbr.ru/statistics/credit_statistics/M2-M2_SA.xlsx
"""

URL_LIST_DOC = """
name: СНС (Росстат)
url: http://www.gks.ru/free_doc/new_site/vvp/
files:
 - tab1.xls
 - tab2.xls
 - tab2a.xls
 - tab3.xls
 - tab4.xls
---
name: Сглаженный ряд М2
url: http://www.cbr.ru/statistics/credit_statistics/M2-M2_SA.xlsx
"""

def concat(url, fn):
    return url + fn

def split_yaml_dict(yaml_dict):
    if 'files' in yaml_dict.keys():
        for fn in yaml_dict['files']:
            yield concat(yaml_dict['url'], fn)
    else:
        yield yaml_dict['url']
 
def split_yaml_list(yaml_list):
    if len(yaml_list) == 1:
        yield yaml_list[0]
    else:
        for fn in yaml_list[1]:
            yield concat(yaml_list[0], fn)

def get_urls(yaml_doc):    
    if isinstance(yaml_doc, str):
        return yaml_doc 
    elif isinstance(yaml_doc, list):
        return split_yaml_list(yaml_doc)
    elif isinstance(yaml_doc, dict):
        return split_yaml_dict(yaml_doc)
   
def yield_urls_based_on_yaml():
   for job in ya.load_all(URL_LIST_DOC):       
       for url in get_urls(job):
           yield(url)