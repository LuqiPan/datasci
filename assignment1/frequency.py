import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    counts = {}
    count = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if (tweet.has_key("text")):
            text = tweet["text"]
            terms = text.split(" ")
            for term in terms:
                count += 1
                if counts.has_key(term):
                    counts[term] += 1
                else:
                    counts[term] = 1

    for k, v in counts.iteritems():
        if "@" in k:
            continue
        if "\n" in k:
            continue
        freq = float(v) / count
        print k + " " + str(freq)

if __name__ == '__main__':
    main()
