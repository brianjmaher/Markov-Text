import string

separators = '.!?'

# processses a string file into a list of separated sentences
def separate(text):
    # remove all double (or greater) spaces
    while '  ' in text:
        text = text.replace('  ', ' ')
    sentences = []
    #<begin> tag marks the beginning of sentences
    sentence = "<begin> "
    for char in text:
        #if the char is a separator, and an end tag to the sentence and begin a new one
        if char in separators:
            sentence += " <end>%s " % char
            # replace all non-space whitespace with spaces
            for wschar in set(string.whitespace) - set(' '):
                sentence = sentence.replace(wschar, ' ')
            # replace consecutive spaces with a single space
            while "  " in sentence:
                sentence = sentence.replace("  ", " ")  
            sentences.append(sentence.strip())
            #begin a new sentence
            sentence = "<begin> "
        else:
            # if char is punctuation, tag it
            if char in string.punctuation:
                sentence += " <>"
            sentence += char
            # wrap with more tag if needed
            if char in "()\"'":
                sentence += "<> "
    return sentences

if __name__ == "__main__":
    print separate(raw_input("Text to separate: "))