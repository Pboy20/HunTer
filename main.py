# Import function to read .docx files
from utils.file_utils import load_docx_text 

# Import the modules for analysis
from analyzer.plagiarism_checker import PlagiarismChecker   # Our new plagiarism checker
from analyzer.readability_analyzer import ReadabilityAnalyzer
from analyzer.citation_checker import CitationChecker
from analyzer.topic_modeler import TopicModeler
from analyzer.report_generator import ReportGenerator

def main():
    print("Welcome to Research Paper Analyzer")

def extract_sections(text):
    sections = ["abstract", "introduction", "methodology", "results", "discussion", "conclusion", "references", "bibliography"]
    found = []
    for line in text.split("\n"):
        for sec in sections:
            if sec in line.lower():
                found.append(sec.capitalize())
    return set(found)

def analyze_single_file():
    filepath = input("Enter the path to your .docx file: ")

    try:
        # Step 0: Load text from the .docx file
        text = load_docx_text(filepath)

        # Step 1: Plagiarism Check
        print("\n Step 1: Checking for sentence-level plagiarism...")
        checker = PlagiarismChecker()   # Create checker object
        similarities = checker.analyze(text)    # Analyze the text

        # Display results to the user
        if similarities:
            print(f"\n Found {len(similarities)} potentially plagiarized sentence pairs:\n")
            for match in similarities:
                print(f"- Match: {match['similarity']}% similar")
                print(f"  Sentence 1: {match['sentences1']}")
                print(f"  Sentence 2: {match['sentences2']}\n")
        else:
            print("No similar sentences pairs found. The paper looks original!")

        # Step 2: Run Readability Analyzer
        print("\n Step 2: Checking readability score...")
        # Create readability analyzer instance
        readability = ReadabilityAnalyzer().analyze(text)

        # Show readability result
        print(f"Readability Score: {readability['score']} ({readability['level']})\n")

        # Step 3: Run Citation Checker
        print("Step 3: Checking citations and references...")
        citations = CitationChecker().check(text)

        # Show citation stats
        print(f"Total In-Text Citations Found: {citations['total_citations']}")
        print(f"  APA-style citations: {citations['apa_count']}")
        print(f"  IEEE-style citations: {citations['ieee_count']}")

        # Check if References section is present
        if citations['has_references_section']:
            print("'References' or 'Bibliography' section found. ")
        else:
            print("No references section found.")

        # Show any warnings
        if citations["warnings"]:
            print("\nWarnings:")
            for w in citations["warnings"]:
                print(f"{w}")

        # Step 4: Topic Modeling
        print("\n Step 4: Extracting top keywords...")
        topic_modeler = TopicModeler()
        keywords = topic_modeler.extract_keywords(text, top_n=10)
        if keywords:
            print("Top Keywords:")
            for word, score in keywords:
                print(f"- {word} (score: {score:.2f})")
        else:
            print("No Keywords extracted (possibly due to short or generic content).")


        # Step 5: Report Generation
        print("Step 5: Generating report...")
        ReportGenerator().generate(filepath, similarities, readability, citations, keywords=keywords)


    except Exception as e:
        print(f"[ERROR]: {e}")     # Catch any unexpected errors

def compare_two_files():
    file1 = input("Enter path to first .docx file: ")
    file2 = input("Enter path to second .docx file: ")

    text1 = load_docx_text(file1)
    text2 = load_docx_text(file2)

    checker = PlagiarismChecker()
    sentences1 = checker.split_into_sentences(text1)
    sentences2 = checker.split_into_sentences(text2)

    results = []
    for s1 in sentences1:
        for s2 in sentences2:
            score = checker.similarity_score(s1, s2)
            if score >= checker.threshold:
                results.append({
                    "sentence1": s1,
                    "sentence2": s2,
                    "similarity": round(score * 100, 2)
                })

    print(f"\nFound {len(results)} similar sentence pairs between the two documents:\n")
    for match in results:
        print(f"- {match['similarity']}% similar")
        print(f" Sentence 1:: {match['sentence1']}")
        print(f" Sentence 1: {match['sentence2']}\n")

        # Optional enhancements:
    # Calculate average similarity and overlap of keywords
    topic_modeler = TopicModeler()
    keywords1 = set(topic_modeler.extract_keywords(text1))
    keywords2 = set(topic_modeler.extract_keywords(text2))
    common_keywords = keywords1.intersection(keywords2)

    print("Keyword Overlap:")
    if common_keywords:
        print(f"Common Keywords: {', '.join([word for word, _ in common_keywords])}")
    else:
        print("No common keywords found.")

# Citation Comparison
    print("\nCitation Comparison:")
    citation_checker = CitationChecker()
    citation1 = citation_checker.check(text1)
    citation2 = citation_checker.check(text2)

    print(f"File 1 - APA: {citation1['apa_count']}, IEEE: {citation1['ieee_count']}, Total: {citation1['total_citations']}")
    print(f"File 2 - APA: {citation2['apa_count']}, IEEE: {citation2['ieee_count']}, Total: {citation2['total_citations']}")

    # Structure Comparison
    print("\nStructure Comparison:")
    sections1 = extract_sections(text1)
    sections2 = extract_sections(text2)
    output_lines = []
    s1 = f"Sections in File 1: {', '.join(sections1)}"
    s2 = f"Sections in File 2: {', '.join(sections2)}"
    common = f"Common Sections: {', '.join(sections1.intersection(sections2))}"
    print(s1)
    print(s2)
    print(common)
    output_lines.extend([s1 + "\n", s2 + "\n", common + "\n"])
    export = input("Do you want to save the comparison report? (yes/no)").strip().lower() =="yes"
    if export:
        with open("comparison_report.txt", "w", encoding="utf-8") as f:
            f.writelines(output_lines)
        print("\nComparison report saved as 'comparison_report.txt' in current directory.")


    # Only run the main function if this file is executed directly
if __name__ == "__main__":
        print("\n==== RESEARCH PAPER ANALYZER ====")
        print("1. Analyze a single research paper")
        print("2. Compare two research papers")
        choice = input("\nEnter choice (1 or 2):").strip()

        if choice == "1":
            analyze_single_file()
        elif choice == "2":
            compare_two_files()
        else:
            print("Invalid choice. Exiting") 
        