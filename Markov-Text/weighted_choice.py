import random, string

def weighted_choice(options, weights):
    total_weight = sum(weights)
    choice_number = random.uniform(0, total_weight)
    total = 0
    for i in range(len(weights)):
        total += weights[i]
        if total >= choice_number:
            return options[i]

def get_weights_from_dict(word_dict):
    output_lst = []
    for word in word_dict.keys():
        output_lst.append((word, word_dict[word]))
    return output_lst

def get_word_weights(text):
    text = text.lower()
    letters_set = set(string.ascii_letters + "' ")
    chars_set = set(text)
    for char in chars_set - letters_set:
        text = text.replace(char, '')
    words = text.split()
    output_dict = {}
    for word in words:
        if "http" not in word:
            if word in output_dict:
                output_dict[word] += 1
            else:
                output_dict[word] = 1
    words_output = output_dict.keys()
    weights_output = [output_dict[word] for word in words_output]
    return words_output, weights_output

if __name__ == "__main__":   
    example = "Yo hey"
    words, weights = get_word_weights(example)
    for i in range(10):
        print weighted_choice(words, weights)