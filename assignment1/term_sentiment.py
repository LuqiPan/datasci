import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    one_word_scores = {}
    two_word_scores = {}

    luqi_scores = {}

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
            span = 2
            sum, abs_sum = [0, 0]

            for i in range(0, len(terms), span):
                score = two_word_scores.get(" ".join(terms[i:i+span]), 0)
                sum += score
                abs_sum += abs(score)

            for term in terms:
                score = one_word_scores.get(term, 0)
                sum += score
                abs_sum += abs(score)

            if abs_sum == 0:
                luqi_score = 0
            else:
                luqi_score = float(sum) / abs_sum * 10

            for term in terms:
                if not one_word_scores.has_key(term):
                    if '@' in term:
                        continue
                    if luqi_scores.has_key(term):
                        luqi_scores[term] += luqi_score
                    else:
                        luqi_scores[term] = luqi_score

    for k, v in luqi_scores.iteritems():
        print k + " " + str(v)

if __name__ == '__main__':
    main()
