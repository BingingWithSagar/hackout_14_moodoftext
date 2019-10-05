#! /usr/bin/python3
# Downloads pictures from reddit.com/r/gentlemanboners after sorting by new

import os,requests,bs4

base='https:/old.reddit.com'
# url='https://old.reddit.com/r/depression'
url='https://old.reddit.com/r/depression/top/?sort=top&t=all'
if os.path.exists('/home/anon/Codes/Python/HACKATHON/neg/')==False:
    os.makedirs('/home/anon/Codes/Python/HACKATHON/neg/')
os.chdir('/home/anon/Codes/Python/GB')
# first_perma=''
# if os.path.exists('first'):
#     first=open('first')
#     first_perma=first.read()
#     first.close()
#if True:

for i in range(200):
    length=0
    while length==0:
        site=requests.get(url)
        soup_obj=bs4.BeautifulSoup(site.text)
        site_table=soup_obj.select('div[data-context="listing"]')
        length=len(site_table)
    #if True:
    for j in range(len(site_table)):
        res=requests.get(site_table[j].attrs['data-url'])
        #print(type(site_table[j].select('[data-event-action="title"]')[0]))
        if i==0 and j==0:
            if first_perma==site_table[0].get('data-permalink'):
                print('No new images')
                exit()
            first=open('first','w')
            first.write(site_table[0].get('data-permalink'))
            first.close()
        name=site_table[j].select('[data-event-action="title"]')[0].getText()
        print('Downloading '+name+'...')
        if os.path.exists(name)==True:
            num=1
            newname=name+'('+str(num)+')'
            while os.path.exists(newname)==True:
                num+=1
                newname=name+'('+str(num)+')'
            name=newname
        files=open(name,'wb')
        for chunk in res.iter_content(100000):
            files.write(chunk)
        files.close()
    url=soup_obj.select('.next-button a')[0].get('href')
