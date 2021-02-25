## Problem: Word Sense Disambiguation

Word sense disambiguation is the problem of determining which sense a word takes on in a particular setting, if that word has multiple meanings. 

For example, in the sentence "I went to get money from the bank", bank probably means the place where people deposit money, not the land beside a river or lake.

Suppose you are given a list of meanings for several words, formatted like so:
```json
{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}
```

Given a sentence, most of whose words are contained in the meaning list above, create an algorithm that determines the likely sense of each possibly ambiguous word.

## Solution
The idea here is that for each ambiguous word, we can compare the set of words in each sense's dictionary definition to the words in the immediate context of the sentence. 

If there is a lot of overlap, it is likely that that sense is correct.


Now let's say our sentence is `'I drove my car past the fork in the road to put some money in the bank.'`

When we compare each word's sense, we find the following overlaps:

```
word  | sense | overlap
-----------------------
bank  |   1   |   - (empty)
bank  |   2   | money
fork  |   1   |   - (empty)
fork  |   2   | road


```
Here we remove overlapping stopwords, such as `'in'` and `'to'`. 

We can see that since only the second senses of bank and fork have similarities to our sentence, those are the meaning we should choose.

Our algorithm, then, will find the sense with the most overlap for each ambiguous word, and store a mapping from word to best sense in a result dictionary.


```python
import re

STOPWORDS = set(['a', 'in', 'or', 'the', 'to'])

def normalize(sentense):
    """Sift out stop words and characters that aren't alphabets"""
    sentense = re.sub('[^A-Za-z]', ' ', sentense)
    words = sentense.lower().split()
    sentense = [word for word in words if word not in STOPWORDS]
    return sentense
```


```python
normalize("I have a dream last night that the year 2021 will be good 1 for us!")
```




    ['i',
     'have',
     'dream',
     'last',
     'night',
     'that',
     'year',
     'will',
     'be',
     'good',
     'for',
     'us']




```python
def disambiguate(sentense, words, meanings):
    """O(W * S * L) time, where W=words to disambiguate, S=number of senses for each word, L=length of definitions for each sense
    O()
    """
    
    sentense = set(normalize(sentense))
    true_senses = {}
    for word in words:
        true_senses[word] = None
        max_overlaps = 0
        for meaning in meanings[word]:
            definition = set(normalize(meaning))
            overlaps = definition.intersection(sentense)
            if len(overlaps) > max_overlaps:
                max_overlaps = len(overlaps)
                true_senses[word] = meaning
    return true_senses
```

### Testing it out


```python
meanings = {
    'bank': ['land beside a river or lake', 'place to deposit money'],
    'fork': ['eating utensil', 'bend in the road']
}
disambiguate(
    sentense="I drove my car past the fork in the road to put my money to the bank", 
    words=['fork', 'bank'],
    meanings=meanings
)
```




    {'fork': 'bend in the road', 'bank': 'place to deposit money'}


