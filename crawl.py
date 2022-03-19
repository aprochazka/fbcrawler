from facebook_scraper import get_posts
import sys

postUrl = ["10160740404099009"]

if(len(sys.argv) != 2):
    print("not enough arguments")
    sys.exit(0)

postUrl = [sys.argv[1]]

commentsArr = []
count = 0
commentsPrint = []
fullPostData = {}

def getReplies(comm):
    global commentsArr

    try:
        replies = comm["replies"]
        for reply in replies:
            getReplies(reply)
    except:
        pass
    commentsArr.append(comm)

def getComments(postId):
    global commentsArr
    global commentsPrint
    global count
    
    fullPostData = next(get_posts(post_urls=postUrl, options={"comments": True}))

    comments = fullPostData["comments_full"]

    for comment in comments:
        getReplies(comment)
        commentsArr.insert(0, commentsArr.pop())
        for eachComment in commentsArr:
            #print(eachComment)
            commentsPrint.append(eachComment)
            count = 1 + count
        commentsArr = []

getComments(postUrl)

f= open(postUrl[0]+".txt","w+")

for com in commentsPrint:
    f.write(com["commenter_name"]+" | "+com["comment_text"]+"\n")

f.close()

print(count)
    
