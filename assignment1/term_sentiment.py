import sys

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    one_word_scores = {}
    two_word_scores = {}

    for line in sent_file:
        term, score = line.split("\t")
        one_word_scores[term] = int(score)

    for line in sent_file:
        term, score = line.split("\t")
        if ' ' in term:
            one_word_scores.pop(term, None)
            two_word_scores[term] = int(score)

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
