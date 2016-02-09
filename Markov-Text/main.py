import fake_sentences as fs
import seperate as sp

def main():
    filename = raw_input("Please enter a file name to parse: ")
    num = int(raw_input("How many sentences do you want? "))
    out_filename = raw_input("What file name should output be written to? ")

    sep_text = sp.seperate(read_text(filename))
    sentences = make_sentences(fs.get_weights(sep_text), num)
    
    out_file = open(out_filename, 'w')
    out_file.write(' '.join(sentences))
    out_file.close()
   
if __name__ == "__main__":
	main()