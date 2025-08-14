import re

class ReadabilityAnalyzer:
    def count_syllables(self, word):
        """
        Estimate number of syllables in a word using a simple rule.
        not 100% accurate, but okay for academic analysis.
        """
        word = word.lower()
        word = re.sub(r'[^a-z]', '', word)  # remove non-alphabet characters
        vowels = "aeiouy"
        count = 0
        prev_char_was_vowel = False

        for char in word:
            if char in vowels:
                if not prev_char_was_vowel:
                    count += 1
                prev_char_was_vowel= True
            else:
                prev_char_was_vowel= False

        if word.endswith("e"):
            count-= 1
        if count <= 0:
            count = 1
            
        return count
    
    def analyze(self, text):
        """
        Calculate Flesch Reading Ease score and return readability status.
        """
        # Split text into sentences
        sentences = re.split(r'[.!?]', text)
        sentences= [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)

        # Split text into words
        words = re.findall(r'\b\w+\b', text)
        num_words = len(words)

        # Count syllables in all words
        syllables = sum(self.count_syllables(word) for word in words)

        # Prevent division by zero
        if num_sentences== 0 or num_words == 0:
            return {"score": 0, "level": "Unreadable"}
        
        # Flesh Reading Ease Formula
        score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (syllables / num_words)
        level = self.get_readability_level(score)

        return {"score": round(score, 2), "level": level}
    
    def get_readability_level(self, score):
        """
        Return readability level based on flesch score. 
        """
        if score >= 90:
            return "Very Easy"
        elif score >= 70:
            return "Easy"
        elif score >= 50:
            return "Fairly Difficult"
        elif score >= 30:
            return "Difficult"
        else:
            return "Very Difficult"
        