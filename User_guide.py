"""
USER GUIDE
Here's a step by step guide to using this tool:

Step 1: Installation and Setup
    - Ensure python 3.8+ is installed on your system.
    - Download the project folder.

Step 2: Prepare Your File
    - Make sure your research paper is saved as a .docx file.
    - Place it inside the project folder.

Step 3: Run the Application
    - Open your terminal or command prompt.
    - Navigate to the project folder using cd command:
        cd "C:\Users\YourName\GROUP 43"
    - Run (pip3 install python-docx) in terminal to be able to read .docx file
    - Run the program using (python main.py)

Step 4: Follow the Prompts and select Option
    - Option 1: Analyze a Single Research Paper
        - Prompts for one .docx file.
        - Enter research paper file path
	  - Outputs:
            - Similar sentence checks
            - Readability metrics
            - In-text citation and reference analysis
            - Top keywords
            - Report is saved automatically

    - Option 2: Compare Two Papers
        - Prompts for two .docx files.
        - Enter research paper 1 & 2 file path
        - Outputs:
            - Sentence similarity matches
            - Keyword overlap
            - Structure (section) comparison
            - Citation stats for both
            - Saves report as comparison_report.txt
You'll see progress updates like:
step 1: Checking for sentence-level plagiarism...
step 2: Evaluating readability...
step 3: Detecting citation styles......

Step 5: View Report
    - Once complete, your report will be saved in the data/reports/ folder.
    - The file will be named using the original filename and timestamp, for example:
        sample1_report_20250730_104215.txt
    - The report includes:
        - Detected plagiarism matches (with similarity percentages)
        - Readability score and level
        - Citation counts and reference section status
        - List of extracted keywords
        - Any citation warnings


"""