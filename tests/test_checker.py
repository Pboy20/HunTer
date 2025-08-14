import unittest
from analyzer.plagiarism_checker import PlagiarismChecker
from analyzer.readability_analyzer import ReadabilityAnalyzer
from analyzer.citation_checker import CitationChecker
from analyzer.topic_modeler import TopicModeler

class TestPlagiarismChecker(unittest.TestCase):
    def test_detects_similarity(self):
        text = "Nelfund student loan is transforming the academic sector. Nelfund student loan is changing lives of less priviledged students"
        checker = PlagiarismChecker(threshold=0.5)
        results = checker.analyze(text)
        self.assertGreater(len(results), 0, "Should detect similar sentences")

class TestReadabilityAnalyzer(unittest.TestCase):
    def test_readability_score(self):
        text = "This is a short puzzle. This is another one."
        analyzer = ReadabilityAnalyzer()
        result = analyzer.analyze(text)
        self.assertIn("score", result)
        self.assertIn("level", result)
        self.assertIsInstance(result["score"], float)
        self.assertIsInstance(result["level"], str)

class TestCitationChecker(unittest.TestCase):
    def test_detects_apa_and_ieee_citations(self):
        text = "This course was explained by Zaccheus (2025). See [202] manual for more info. References"
        checker = CitationChecker()
        result = checker.check(text)
        self.assertGreater(result["total_citations"], 0)
        self.assertTrue(result["has_references_section"])

class TestTopicModeler(unittest.TestCase):
    def setUp(self):
        self.modeler = TopicModeler()

    def test_keywords_extraction(self):
        text = (
           """CSC 202, titled "Computer Programming Lab II," is a practical course offered to second-year Computer Science students. It builds upon the foundations laid in CSC 201, focusing more on problem-solving through structured programming techniques."
           Assignments include file handling, error checking, working with data structures such as lists, dictionaries, sets, etc. Students are assessed continuously through lab exercises, short quizzes, and a final mini-project. CSC 202 emphasizes "
           writing clean, efficient code and prepares students for more advanced programming tasks in future courses."""
        )
        result = self.modeler.extract_keywords(text, top_n=5)

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(isinstance(k[0], str) for k in result))

    def test_empty_text(self):
        result = self.modeler.extract_keywords("", top_n=5)
        self.assertEqual(result, [])

    def test_ignore_common_words(self):
        text = "the and a to in for of on with as is was are be this that"
        result = self.modeler.extract_keywords(text)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()

        