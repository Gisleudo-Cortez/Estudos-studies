from collections import Counter
import tokenize
from io import BytesIO
import matplotlib.pyplot as plt 

def filter_word_counts(word_counts, first_char):
    """Filter Document.word_counts by the first character of the word
    
    :param word_counts: the word_counts attribute of a Document class instance
    :param first_char: only keep word counts that start with this character
    
    >>> # How to filter to only words that start with 'A'
    >>> filter_word_counts(document.word_counts, 'A')
    """
    return Counter({k: v for k, v in word_counts.items() if k[0] == first_char})

def plot_counter(data):
    """
    Plot a bar chart for the first three values in a dictionary.

    :param data: Dictionary with the structure {'name': value}
    """
    # Extract names and values for the first three items
    names = list(data.keys())[:3]
    values = list(data.values())[:3]

    # Plotting
    plt.bar(names, values)
    plt.xlabel('Names')
    plt.ylabel('Values')
    plt.title('First Three Values from the Dictionary')
    plt.show()

class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    def __init__(self, text):
        self.text = text
        # Tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Perform word count with non-public count_words method
        self.word_counts = self._count_words()

    def _tokenize(self):
        # Use tokenize module for tokenization
        tokens = []
        for token in tokenize.tokenize(BytesIO(self.text.encode('utf-8')).readline):
            if token.type == tokenize.NAME:
                tokens.append(token.string)
        return tokens
	
    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
