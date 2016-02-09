import random, string

# make a weighted choice from a list of options using the corresponding 
# list of weights, which can be any floats or ints
def weighted_choice(options, weights):
    total_weight = sum(weights)
    #select a random number between 0 and total_weight
    choice_number = random.uniform(0, total_weight)
    total = 0
    #use this reandom number to make a random choice
    for i in range(len(weights)):
        total += weights[i]
        if total >= choice_number:
            return options[i]

# given a dictionary of words mapping to their weights, convert it into a 
# list of tuples of from (word, weight)
def get_weights_from_dict(word_dict):
    output_lst = []
    for word in word_dict.keys():
        output_lst.append((word, word_dict[word]))
    return output_lst

if __name__ == "__main__":   
    pass