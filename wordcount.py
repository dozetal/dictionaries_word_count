
# put your code here.

# Create the dictionary WORDCOUNT
wordcount = {}

# Define the function TO_COUNT
def to_count(textfile):

    # This unpacks the data
    data = open(textfile)

    # This takes each word, iterates by word occurence 
    # And adds the word to the dictionary, 
    # increasing its word count by one
    # Each time it is seen

    # Splits the poem into a list of words
    for line in data:
        words = line.rstrip().split()

        # Iterate over the list of words
        for word in words:
            wordcount[word] = wordcount.get(word, 0) + 1
    
    # Print the key and value, i.e. word and its occurences in text 
    for key, value in wordcount.items():
        print key, value 

to_count('twain.txt')









