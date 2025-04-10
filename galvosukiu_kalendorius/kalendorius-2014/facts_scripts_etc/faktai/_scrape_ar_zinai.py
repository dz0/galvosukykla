# coding=utf-8
# http://www.blog.pythonlibrary.org/2012/06/07/python-101-how-to-download-a-file/
index_url = "http://www.arzinai.lt/index.php?option=com_content&view=section&id=10&Itemid=550"

root="http://www.arzinai.lt"

#~ category=u"visata"
#~ url="http://www.arzinai.lt/index.php?option=com_content&view=category&id=54:visata&Itemid=550&layout=default"
#~ 
#~ category=u"buitis"
#~ url="http://www.arzinai.lt/index.php?option=com_content&view=category&id=49:buitis&Itemid=550&layout=default"

import urllib
#~ response = urllib.urlopen(url)
response = urllib.urlopen(index_url)
html = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)

import re
import os

links = soup.find('div', id="middlecontainer").find('ul').find_all('a')
for category_link in links:
    category_url = category_link.get('href')
    print category_url
    try:
        m = re.search(':(\w+)&', category_url)
        category = m.group(1)
    except:
        print 'no category name', 
        continue
    print category
    if category+'.arzinai.txt' in os.listdir('.'):
        print 'Already exists'
        continue

    response = urllib.urlopen(root+category_url+'&limit=0');
    soup = BeautifulSoup(  response.read() )

    contents=soup.find(id="middlecontainer")
    facts =[]
    for link in contents.find_all('a'):
        
        fact_url=root+link.get('href')
        if 'javascript' in fact_url: continue
        print
        print(fact_url)

        # get fact
        try:
            fact_html = urllib.urlopen(fact_url).read()
        except UnicodeError:
            print 'UnicodeError', fact_url
            continue
        fact_soup = BeautifulSoup(fact_html)
        try:
            fact = fact_soup.find(id="middlecontainer").find_all('table', class_="contentpaneopen")[1].get_text()
            fact = fact.replace(u'Parašė', '').strip(' \n\t\r')
            fact = re.sub('\s{2,10}', ' ', fact)
            facts.append( fact )
            print fact
        except:
            pass
        


    with open(category+".arzinai.txt", 'wb') as fout:
        fout.write( '\n'.join(facts) .encode("UTF-8") )

    #~ soup.find("div#middlecontainer")

    """
    form name=adminForm


    td.middlecolumn
    .contentpaneopen
    td
    """
