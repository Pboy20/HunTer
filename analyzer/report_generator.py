import os
from datetime import datetime

class ReportGenerator:
    def generate(self, filepath, plagiarism_results, readability_results, citation_results, keywords=None):
        """
        Generate a .txt report of all analysis results.
        Save it in the 'data/reports' directory.
        """
        # Create report folder if it dosent exist
        report_dir = "data/reports"
        os.makedirs(report_dir, exist_ok=True)

    
        # Create unique filename with timestamp
        base_name = os.path.basename(filepath).replace('.docx', '')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(report_dir, f"{base_name}_report_{timestamp}.txt")

        with open(report_path, "w", encoding="utf_8") as report:
            report.write("=== RESEARCH PAPER ANALYSIS REPORT ===\n\n")
            report.write(f"File: {filepath}\n")
            report.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Section 1: Plagiarism
            report.write("Plagiarism Check:\n")
            if plagiarism_results:
                report.write(f"Found {len(plagiarism_results)} similar sentence pairs:\n")
                for match in plagiarism_results:
                    report.write(f"- {match['similarity']}% similar\n")
                    report.write(f"  Sentence 1:  {match['sentences1']}\n")
                    report.write(f"  Sentence 2:  {match['sentences2']}\n")
            else:
                report.write("no significant similarities found. Looks original.\n\n")\
                
            # Section 2: Readability 
            report.write("Readability:\n")
            report.write(f"Score:  {readability_results['score']} ({readability_results['level']})\n\n")
                                                                                        
            # Section 3: Citations
            report.write("Citation Check:\n")
            report.write(f"APA-style:  {citation_results['apa_count']}\n")
            report.write(f"IEEE-style:  {citation_results['ieee_count']}\n")
            report.write(f"Total:  {citation_results['total_citations']}\n")
            report.write("References Section:  {}\n\n".format(
                "Present" if citation_results["has_references_section"] else "Missing"
            ))

            if citation_results["warnings"]:
                report.write("Warnings:\n")
                for warning in citation_results["warnings"]:
                    report.write(f"-  {warning}\n")

            # Section 4: Keywords from Topic Modeling
            report.write("4. Topic Modeling - Extracted Keywords:\n")
            if keywords:
                for word, score in keywords:
                    report.write(f"- {word}: {score:.2f}\n")
            else:
                report.write("No significant keywords extracted.\n")

        print(f"Report saved at: {report_path}")

    
                                                                                        
        