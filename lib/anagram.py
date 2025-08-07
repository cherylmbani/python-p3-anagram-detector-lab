# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word.lower()
    
    def match(self, word_list):
        matches=[]

        for candidate in word_list:
            if candidate.lower()==self.word:
                continue
            if sorted(candidate.lower())==sorted(self.word):
                matches.append(candidate)
        return matches

