import json
import tkinter as tk
from tkinter import filedialog

def analyze_scores(students):
    if not students:
        return {"Error": "No student data found."}

    average_score = sum(student['Score'] for student in students) / len(students)
    top_scorer = max(students, key=lambda x: x['Score'])
    lowest_scorer = min(students, key=lambda x: x['Score'])

    feedback = []
    for student in students:
        name = student['StudentName']
        score = student['Score']
        if score >= 90:
            feedback.append(f"🌟 {name} is doing excellent! Keep up the great work!")
        elif score >= 80:
            feedback.append(f"👍 {name} is doing well but can aim for a higher score next time.")
        elif score >= 70:
            feedback.append(f"💡 {name} is passing but needs to focus more on studies.")
        elif score >= 60:
            feedback.append(f"⚠️ {name} is barely passing and needs significant improvement.")
        else:
            feedback.append(f"❌ {name} is failing and needs urgent attention.")

    class_summary = f"""
📊 Class Performance Summary:
----------------------------------
✅ Average Score: {average_score:.2f}
🏆 Top Scorer: {top_scorer['StudentName']} ({top_scorer['Score']})
📉 Lowest Scorer: {lowest_scorer['StudentName']} ({lowest_scorer['Score']})
"""

    return {
        "ClassSummary": class_summary,
        "Feedback": feedback
    }

def upload_file():
    root = tk.Tk()
    root.update()  # Ensures the dialog shows up properly
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select a JSON file",
        filetypes=[("JSON Files", "*.json")]
    )
    print("DEBUG: File selected:", file_path)
    return file_path

def main():
    print("\n📢 Welcome to the Student Quiz Analysis Chatbot!\n")
    input("Press ENTER to upload a JSON file containing student scores...")

    file_path = upload_file()

    if not file_path:
        print("❌ No file selected. Please restart the program and upload a valid JSON file.")
        return

    try:
        with open(file_path, 'r') as file:
            students = json.load(file)
            print("\n📂 Student Data Loaded Successfully!")

            print("\n🔍 Analyzing Performance... Please wait...\n")
            analysis_result = analyze_scores(students)

            if "Error" in analysis_result:
                print("❌", analysis_result["Error"])
                return

            print(analysis_result['ClassSummary'])
            print("\n📢 Personalized Feedback:")
            for comment in analysis_result['Feedback']:
                print(comment)
            print("\n✅ Analysis Complete! Thanks for using the Student Quiz Analysis Chatbot.\n")
    except FileNotFoundError:
        print("❌ Error: The selected file was not found. Please try again.")
    except json.JSONDecodeError:
        print("❌ Error: The file format is invalid. Please upload a proper JSON file.")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")

if __name__ == "__main__":
    main()
