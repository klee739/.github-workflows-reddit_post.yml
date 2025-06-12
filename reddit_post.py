import os
import praw

# Reddit credentials from GitHub Secrets
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="AutoPoster",
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"],
)

# Post details
title = "Use my link for free FSD!"
body = "Use my link to get 3 months of Full Self-Driving (Supervised) or $400 off Solar Panel installation! https://www.tesla.com/referral/kyeu702786"
subreddits = ["teslareferralcode", "TeslaReferralsCode"]

# Submit post to each subreddit
for sub in subreddits:
    try:
        subreddit = reddit.subreddit(sub)
        subreddit.submit(title, selftext=body)
        print(f"Posted to r/{sub}")
    except Exception as e:
        print(f"Failed to post to r/{sub}: {e}")
