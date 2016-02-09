import string

seperators = '.!?'

def seperate(text):
    sentences = []
    sentence = "<begin> "
    for char in text:
        if char in seperators:
            sentence += " <end>%s " % char
            for wschar in set(string.whitespace) - set(' '):
                sentence = sentence.replace(wschar, ' ')
            while "  " in sentence:
                sentence = sentence.replace("  ", " ")  
            sentences.append(sentence.strip())
            sentence = "<begin> "
        else:
            if char in string.punctuation:
                sentence += " <>"
            sentence += char
            if char in "()\"'":
                sentence += "<> "
    return sentences

if __name__ == "__main__":
    print seperate(raw_input())
    print seperate("Hello, my name is 'Barack Hussein Obamacare'. I was born in the\n greatest nation (Kenya) in 1969.")