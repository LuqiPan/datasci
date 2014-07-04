import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        if (tweet.has_key("text")):
            text = tweet["text"]
            terms = text.split(" ")
            sum = 0
            for term in terms:
                sum += scores.get(term, 0)
            print sum


if __name__ == '__main__':
    main()
