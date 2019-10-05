#! /usr/bin/python3
import praw,time

reddit = praw.Reddit(client_id='T7sTBKCu6Tg3LA', client_secret='fUscf6kP7Wrhq0W7hzhNXTP1aWg', user_agent='ml')
# srList=['getmotivated','happy','casualconversation']
# fname='positive'
srList=['depression','suicidewatch','anxiety']
fname='negative'
i=0
for sr in srList:
    # sr='happy'
    depPost=reddit.subreddit(sr).top(limit=None)
    f=open(sr+'Posts.txt','a')
    for post in depPost:
        i+=1
        if (post.selftext==''):
            i-=1
        else:
            f.write(post.title+'\n'+post.selftext+'\n.\n')
        print(i)
        # if i%900==0:
        #     time.sleep(12)
    f.close()