import re
def count_words(text):
    counts = dict()

    text = text.lower()
    words = re.split('[^a-zA-Z0-9]', text)
    while "" in words:
      words.remove("")   
    
    for element in words:
      if element in counts.keys():
        counts[element]+=1
      else:
        counts[element] = 1

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read() 

        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))

if __name__ == "__main__":
    test_run()