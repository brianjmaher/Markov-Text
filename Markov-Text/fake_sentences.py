import weighted_choice as wc
import seperate as sp

def bible_text():
    text = ""
    for line in open('kjvdat.txt'):
        text += line[line.find(" ") + 1:-2] + " "
    return text

def read_text(filename):
    text = ' '.join([line.strip() for line in open(filename)])
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.strip()

def get_weights(sentences):
    weights = {}
    for sentence in sentences:
        words = sentence.split(" ")
        last_word = "<begin>"
        for i in range(len(words)):
            if i > 0:
                word = words[i].lower().strip()
                if word != "":
                    if last_word not in weights:
                        weights[last_word] = {}
                    if word not in weights[last_word]:   
                        weights[last_word][word] = 0
                    weights[last_word][word] += 1
                    last_word = word
    return weights

def make_sentences(words_dict, n):
    sentences = []
    init_sentence = ["<begin>"]
    while len(sentences) < n:
        sentence_words = init_sentence[:]
        while True:
            prev_word = sentence_words[-1]
            words, weights = zip(*wc.get_weights_from_dict(words_dict[prev_word]))
            new_word = wc.weighted_choice(words, weights)
            sentence_words.append(new_word)
            if "<end>" in new_word:
                if len(sentence_words) > 2:
                    sentences.append(format_sentence(sentence_words))
                break
    return sentences

def format_sentence(sentence_words):
    sentence = ' '.join(sentence_words)
    sentence = sentence.replace("<begin> ", "").replace(" <end>", "")
    sentence = sentence.replace("<begin>", "").replace("<end>", "")
    sentence = sentence.replace(" <>", "").replace("<> ", "").replace("<>", "")
    return sentence.capitalize()

if __name__ == "__main__":
    pass