
import os
import praw


def main():

    pass


class Message:

    def format(self, matches):

        return ' '.join(['__[${}]__ - [{}]({})\n\n'.format(
               match[2], match[0], match[3]) for match in matches])

    def send(self, f_matches):

        reddit_id = os.environ['REDDIT_ID']
        reddit_secret = os.environ['REDDIT_SECRET']
        reddit_password = os.environ['REDDIT_KEY']
        user = 'nbonneBOT'
        user_agent = 'by u/prgrmr_noob'

        reddit = praw.Reddit(client_id=reddit_id,
                             client_secret=reddit_secret,
                             password=reddit_password,
                             user_agent=user_agent,
                             username=user)

        reddit.redditor('B_ongfunk').message('Canyon Oulet', f_matches)

if __name__ == '__main__':

    main()
