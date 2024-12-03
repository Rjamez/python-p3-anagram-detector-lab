class Anagram:  
    def __init__(self, word):  
        self.word = word  

    def match(self, candidates):  
        # Logic to find anagrams:  
        matches = []  
        sorted_word = sorted(self.word)  # Sort the letters of the original word  
        for candidate in candidates:  
            if sorted(candidate) == sorted_word:  # Sort and compare  
                matches.append(candidate)  # Add to matches if they are equal  
        return matches  # Return the list of matches