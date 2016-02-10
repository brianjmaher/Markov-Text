import weighted_choice as wc
from separate import separate

# reads text from a txt file and returns it as a string
def read_text(filename):
    return ' '.join([line.strip() for line in open(filename)]).strip()

# from a list of separated sentences, get the dictionary of word weights
# has the form weights[first_word][next_word] = weight
def get_word_weights(sentences):
    weights = {}
    for sentence in sentences:
        words = sentence.split(" ")
        # if the sentence is longer than two words, i.e., is more than
        # just a begin and end tag
        if len(words) > 2:
            prev_word = "<begin>"
            for i in range(1, len(words)):
                # manipulate the word as lowercase and stripped
                word = words[i].lower().strip()
                # if the word isn't an empty string, increment the weights dict
                if word != "":
                    if prev_word not in weights:
                        weights[prev_word] = {}
                    if word not in weights[prev_word]:   
                        weights[prev_word][word] = 0
                    weights[prev_word][word] += 1
                    prev_word = word
    return weights

# sentence generator function, takes a filename and a number of sentences
# to generate
def generate_sentences(filename, n):
    # separate text and generate the word weights dictionary
    sep_text = separate(read_text(filename))
    words_dict = get_word_weights(sep_text)
    sentences = []
    # begin all sentences with a begin tage
    init_sentence = ["<begin>"]
    while len(sentences) < n:
        sentence_words = init_sentence[:]
        while True:
            # get the last word of the sentence
            prev_word = sentence_words[-1]
            # get the list of words and weights for that word
            words, weights = zip(*wc.get_weights_from_dict(words_dict[prev_word]))
            # make a weighted choice for the new word based on the previous
            new_word = wc.weighted_choice(words, weights)
            sentence_words.append(new_word)
            # if an end tag is found and the sentence list is more than two,
            # format the sentence into a string and append it to the list
            if "<end>" in new_word:
                if len(sentence_words) > 2:
                    sentences.append(format_sentence(sentence_words))
                break
    return sentences

# formats a list of sentence words into a sentence string
def format_sentence(sentence_words):
    sentence = ' '.join(sentence_words)
    # remove all begin and end tags
    sentence = sentence.replace("<begin> ", "").replace(" <end>", "")
    sentence = sentence.replace("<begin>", "").replace("<end>", "")
    # remove punctuation tags
    sentence = sentence.replace(" <>", "").replace("<> ", "").replace("<>", "")
    return sentence.capitalize()

if __name__ == "__main__":
    pass