import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    hashtag_counts = {}
    total_counts = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if (tweet.has_key("entities") and tweet["entities"].has_key("hashtags")):
            hashtags = tweet["entities"]["hashtags"]
            total_counts += len(hashtags)
            for tag_dict in hashtags:
                tag = tag_dict["text"]
                if hashtag_counts.has_key(tag):
                    hashtag_counts[tag] += 1
                else:
                    hashtag_counts[tag] = 1

    top_ten = sorted(hashtag_counts.items(), key = lambda (k, v): v, reverse = True)[:10]
    for item in top_ten:
        print item[0], item[1]

if __name__ == '__main__':
    main()
