## Stable Marriage Problem

The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

```python
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}
```

```python
gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
```

Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.

## Solution
Don't be upset if you found this problem challenging: the Gale-Shapley algorithm to solve this ended up earning one its creators a Nobel Prize!

The algorithm is as follows:
At each step, we consider one currently unmarried man. This man goes through his list of partners, proposing to each one. If the woman is unmarried, she agrees automatically. Otherwise, she will consider whether she prefers this new suitor to her current husband. If she does, she "trade up" to the new offer.

With the input above:
- Andrew proposes to Caroline. Since Caroline is currently available, she says yes, and they get paired up. 
- Next, Bill has Caroline as her first choice. Unfortunately for Andrew, Caroline prefers Bill, so she dumps Andrew and pairs up with Bill.
- Andrew goes to her second choice Abigail, and she agrees.
- Finally Chester asks Betty to marry. Sadly for Betty, even though Chester is her least favorite, she has no choice but to agree.

```
   men   |  women  | pairs
-----------------------------
A, B, C  | A, B, C |    -
B, C     | A, B    | (A, C)
A, C     | A, B    | (B, C)
C        | B       | (B, C), (A, A)
    -    |    -    | (B, C), (A, A), (C, B)

```

### How do we know this algorithm works?
Each man must get married, or exhaust his list. In this algorithm, once a woman is married, she can't be single again - but can only exchange partners. Since every gal getting married means every guy getting married, we have reached a contradiction. 

We must also show that this matching is good that no two people (guy **and** gal) should secretly desire each other more than their current partners. This is impossible. 

As each guy goes through his list there are two scenarios:
- The gal **first** accepted his offer and **later** took another guy, in which case she won't desire him now.
- The gal rejects him as she is already in a stable marriage, which again means she cannot desire him now. 

Therefore, this algorithm will provide stable pairing, BUT not everyone will be happy. :)


```python
def format_input(guys, gals):
    # reverse guys preferences, so popping the most desired gal takes O(1) time
    guys = {guy: list(reversed(prefs)) for guy, prefs in guys.items()}
    
    # gal preferences are stored in a dict, so that comparing guys is O(1)
    for gal, prefs in gals.items():
        gals.update({gal: {guy: i for i, guy in enumerate(prefs)}})
    
    return guys, gals
```


```python
def match(guys, gals):
    pairs = {}
    
    guys_prefs, gals_prefs = format_input(guys, gals)
    
    married_men = set()
    married_women = set()
    
    bachelors = list(guys_prefs.keys())
    
    while bachelors:
        man1 = bachelors.pop()
        
        while man1 not in married_men:
            # find the gal he prefers O(1)
            woman = guys_prefs[man1].pop()
            
            # if desired woman is not married, pair with the current man
            if woman not in married_women:
                married_men.add(man1)
                married_women.add(woman)
                pairs[woman] = man1
            else:
                # she's already married, now check if she desires this new man
                # compare current husband with the new man(man1)
                her_current_man = pairs[woman]

                if gals_prefs[woman][man1] < gals_prefs[woman][her_current_man]:  # O(1)
                    married_men.remove(her_current_man)
                    bachelors.append(her_current_man)
                    married_men.add(man1)
                    pairs[woman] = man1
    return pairs
```


```python
guys_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gals_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
match(guys_preferences, gals_preferences)
```




    {'betty': 'chester', 'caroline': 'bill', 'abigail': 'andrew'}



In the worst case, we go through entire preference list of each man. This will take **O(N^2)** space and time, since we formatted our input to allow for constant time retrievals.


```python

```
