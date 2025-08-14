#  Research Paper Analyzer and Plagiarism Checker

A **Command Line Interface (CLI)** application that analyzes research papers for originality, citation accuracy, readability, keyword extraction, and topic modeling. It also generates detailed plagiarism reports.  

---

##  Features

- **Sentence-Level Plagiarism Detection** – Detects plagiarism using string matching algorithms.
- **Citation Style Detection** – Identifies and validates in-text citations and references.
- **Readability Analysis** – Calculates readability scores and writing quality metrics.
- **Keyword Extraction & Topic Modeling** – Highlights key terms and subjects covered.
- **Detailed Report Generation** – Generates plagiarism reports with similarity percentages.
- **Citation Exclusion** – Excludes detected citations from plagiarism checks.

---

##  Directory Structure

```text
 Research-Paper-Analyzer
├──  main.py                          # Entry point of the application
├──  User_guide.py                    # CLI help and usage guide
├──  analyzer/                        # Core analysis modules
│   ├──  __init__.py                   # Marks package initialization
│   ├──  plagiarism_checker.py         # Sentence-level plagiarism detection
│   ├──  citation_checker.py           # Citation style detection and validation
│   ├──  readability_analyzer.py       # Readability score calculations
│   ├──  report_generator.py           # Generates detailed analysis reports
│   ├──  topic_modeler.py              # Keyword extraction & topic modeling
├──  utils/                            # Helper functions
│   ├──  __init__.py
│   ├──  file_utils.py                 # File loading and parsing (.docx)
├──  tests/                            # Unit and functional tests
│   ├──  __init__.py
│   ├──  test_checker.py               # Test cases for all modules
├──  data/                             # Input/output storage
│   ├──  reports/                      # Generated analysis & comparison reports
│   ├──  sample/                       # Sample research paper files
└──  README.md                         # Project documentation
```

---

##  Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/Research-Paper-Analyzer.git
   cd Research-Paper-Analyzer
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

---

##  Usage

To see the help guide:
```bash
python User_guide.py
```

To analyze a paper:
```bash
python main.py --file path/to/your/document.docx
```

---

##  Example Output

- **Plagiarism Report**  
  Similarity: `12%`  
  Matched Sources: `2`  
  Citations Detected: `15`  

- **Readability Metrics**  
  Flesch Reading Ease: `72.3`  
  Grade Level: `8`  

---

##  Testing

Run all unit tests:
```bash
python -m unittest discover tests
```

---

##  License
This project is for educational purposes and demonstrates Python fundamentals:

- Functions & Data Structures
- Object-Oriented Programming
- File Handling
- Loops & Control Flow
- Error Handling
- Unit Testing
