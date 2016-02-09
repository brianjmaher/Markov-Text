from sentence_generator import generate_sentences

def main():
	# read filenames and number of sentences
    in_filename = raw_input("Please enter a file name to parse: ")
    out_filename = raw_input("Please enter a file name to write ouput to: ")
    num = int(raw_input("How many sentences do you want? "))

    # generate sentences
    sentences = generate_sentences(in_filename, num)
    text = ' '.join(sentences)

    print text
    
    # write sentences to file
    out_file = open(out_filename, 'w')
    out_file.write(text)
    out_file.close()
   
if __name__ == "__main__":
	main()