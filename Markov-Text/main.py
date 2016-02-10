from sentence_generator import generate_sentences
import sys # for command line arguments

def main(in_filename, out_filename, num):
    sentences = generate_sentences(in_filename, num)
    text = ' '.join(sentences)

    print text
    
    # write sentences to file
    out_file = open(out_filename, 'w')
    out_file.write(text)
    out_file.close()
   
if __name__ == "__main__":
    # argv[1] is the input file location
    # argv[2] is the output file location
    # argv[3] is the number of sentences to generate
    if len(sys.argv) == 4:
        try:
        	main(sys.argv[1], sys.argv[2], sys.argv[3])
            print "Success."
        except:
            print "Failed."
    else:
        print "ERROR: incorrect number of argumnets: %d given, 3 expected." % len(sys.argv)
        sys.exit(1)