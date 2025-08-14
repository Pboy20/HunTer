import re

class CitationChecker:
    def check(self, text):
        """
        Scan the text for citations and references.
        Returns basic stats and issues found.
        """
        results = {}

        # --- 1. Check for in-text citations ---

        # APA-style citations: (Kalilu, (2024)), (Zaccheus & Rotimi, (2023))
        apa_pattern = r'\([A-Z][a-zA-Z& ]*, ?\s?\d{4}\)'

        # IEEE-style citations: [1], [12], etc.
        ieee_pattern = r'\[\d+\]'

        apa_matches = re.findall(apa_pattern, text)
        ieee_matches = re.findall(ieee_pattern, text)

        total_citations = len(apa_matches) + len(ieee_matches)

        # --- 2. Check if References/Bibliography section exists ---
        has_references = "references" in text.lower() or "bibliography" in text.lower()

        # --- 3. Prepare results ---
        results["apa_count"] = len(apa_matches)
        results["ieee_count"] = len(ieee_matches)
        results["total_citations"] = total_citations
        results["has_references_section"] = has_references

        # Warnings
        results["warnings"] = []

        if total_citations == 0:
            results["warnings"].append("No in-text citations found.")

        if not has_references:
            results["warnings"].append("No References or Bibliography section found.")
            
        return results