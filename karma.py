import praw
from praw.models import MoreComments
from praw.models import Message
from string import Template
import time



reddit = praw.Reddit(client_id = 'OiAW28ePr0xVUQ',
client_secret = 'fca3r_79Vt05iSvf20FnJXAxUfDbkg',
user_agent = 'console: message_bot 1.0',
username = 'Consistent-Ad7472',
password = 'Arcticfox11')

def check_author(author):
    
    file = open("comment_list.txt",'r')
    for line in file.readlines():
        if author in line:
            file.close()
            return 1


    file.close()        

    return 0


title = 'Sleepy Sloth Finance'
 
i = 50



countdown = 48
tries = 0

subreddits = ['FreeKarma4U']

reply = "Heyy, I am new to reddit, upvote for upvote ? XOXO"

while (i>0):

    for topic in subreddits:
        subreddit = reddit.subreddit(topic)
        for submission in subreddit.new(limit = 50):
            print("online")
            author = str(submission.author)
            check = check_author(author)
            if check == 0:
                
                submission.reply(reply)
                print("Commented on subreddit ",subreddit )
                                    
                message_list = open("comment_list.txt",'a+')
                message_list.write('\n' + author)
                message_list.close()
                time.sleep(200)
            submission.comments.replace_more(limit = 0)
            for comment in submission.comments :
                author = str(comment.author)
                                
                if check_author(author) == 0 :
                    comment.reply(reply)
                    
                    message_list = open("comment_list.txt",'a+')
                    message_list.write('\n' + author)
                    message_list.close()
                    time.sleep(200)

                

    



 
         
            

