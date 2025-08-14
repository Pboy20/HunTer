import re
from collections import Counter

class TopicModeler:
    def extract_keywords(self, text, top_n=10):
        """
        Extract top keywords from the document using frequency analysis
        Returns a list of (word, count) tuples:
        """
        # Basic stopwords list
        stopwords = set([
            'the', 'and', 'is', 'in', 'to', 'of', 'a', 'for', 'on', 'with', 'as', 
            'by', 'an', 'be', 'at', 'this', 'that', 'from', 'are', 'or', 'it',
            'was', 'which', 'we', 'can', 'has', 'have', 'its', 'also', 'may', 'used'
        ])

        # Normalize text
        text = text.lower()

        # Tokenize into words (alphanumeric only)
        words = re.findall(r'\b[a-z]{3,}\b', text)  # 3+ letter words only

        # Remove stopwords
        filtered_words = [word for word in words if word not in stopwords]

        # Count frequency
        word_counts = Counter(filtered_words)

        # Get top N keywords
        top_keywords = word_counts.most_common(top_n)

        return top_keywords
    
