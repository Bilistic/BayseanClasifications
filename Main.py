import Probability
import Parse

def main():
    print("Parsing Training Data...")
    parser = Parse.Parser("C:\\Users\\Asus\\Downloads\\IMDB")
    maths = Probability.Probability(parser.p_d, parser.n_d, parser.c_p, parser.c_n, parser.v_c)
    pos = test("C:\\Users\\Asus\\Downloads\\smallTest\\pos", parser, maths)
    neg = test("C:\\Users\\Asus\\Downloads\\smallTest\\neg", parser, maths)
    print("\nPOS test set: ", pos, "\n\nNeg test set: ", neg)

def test(path, parser, maths):
    p_counter = 0
    n_counter = 0
    test_path = path
    for file in parser.folder_files(test_path):
            dic = {}
            if maths.naive_bayes(parser.read_txt(test_path + "\\" +file, dic, vocab=False)) is True:
                p_counter +=1
            else:
                n_counter +=1
    return "\nPositive: " + str(p_counter) + "\nNegative: " + str(n_counter)

if __name__ == "__main__":
    main()
