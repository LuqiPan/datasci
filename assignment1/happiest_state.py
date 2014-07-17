import sys
import json

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

def main():
    def get_tweet_score(tweet):
        if (tweet.has_key("text")):
            text = tweet["text"]
            terms = text.split(" ")
            sum = 0
            for term in terms:
                sum += scores.get(term, 0)
            return sum
        else:
            return 0

    def get_location_words(tweet):
        if (tweet.has_key("place")):
            if tweet["place"]:
                if "," in tweet["place"]["full_name"]:
                    words = tweet["place"]["full_name"].split(",")
                    word1, word2 = [words[0], words[1]]
                    word2 = word2[1:]
                    return [word1, word2]
        return [None, None]

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    state_scores = {}
    states_reverse = {}
    for state in states.keys():
        state_scores[state] = 0
        states_reverse[states[state]] = state

    for line in tweet_file:
        tweet = json.loads(line)
        word1, word2 = get_location_words(tweet)
        score = get_tweet_score(tweet)
        if word1:
            #print word1, word2
            if states.has_key(word1):
                state_scores[word1] += score
                continue
            if states.has_key(word2):
                state_scores[word2] += score
                continue
            if states_reverse.has_key(word1):
                state_scores[states_reverse[word1]] += score
                continue

    max = 0
    state_max = ""
    for state in state_scores:
        if state_scores[state] > max:
            max = state_scores[state]
            state_max = state

    print state_max

if __name__ == '__main__':
    main()
