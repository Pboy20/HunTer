import difflib  # For calculating string similarity

class PlagiarismChecker:
    def __init__(self, threshold=0.8):
        # Threshold value (e.g., 0.8 = 80%) to mark sentences as similar
        self.threshold = threshold

    def split_into_sentences(self, text):
        """
        Split the full text into individual sentences.
        Currently uses periods to split _ simple but works for most cases.
        """
        return [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    
    def similarity_score(self, a, b):
        """
        Calculate similarity ratio between two strings using difflib.
        Returns a value between 0 and 1
        """
        return difflib.SequenceMatcher(None, a, b).ratio()
    
    def analyze(self, text):
        """
        Main function to compare each sentence with others.
        Returns a list of dictionaries with matched sentences and similarity scores.
        """
        sentences = self.split_into_sentences(text)
        results = []

        # Compare every sentence with every other sentence (only once)
        for i in range(len(sentences)):
            for j in range(i + 1, len(sentences)):
                score = self.similarity_score(sentences[i], sentences[j])

                # If similarity is higher than threshold, store the match
                if score>= self.threshold:
                    results.append({
                        "sentences1": sentences[i],
                        "sentences2": sentences[j],
                        "similarity": round(score * 100, 2) # convert to percentage
                    })

        return results