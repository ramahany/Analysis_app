# 🧠 Code Complexity Analyzer – LeetCode-Style AI Feedback for Your Code

Tired of hitting a paywall just to analyze your code's time complexity on LeetCode?  
**So was I.**  
That's why I built this app.

Whether you're solving problems on LeetCode, prepping for interviews, or just curious about your code’s performance, this tool gives you **AI-powered analysis**—free, fast, and in a familiar format.

---

## 🚀 What It Does

- 📥 Accepts code via:
  - A file (auto-detects the language based on extension)
  - Or a manual paste (with language selection)
- 🧠 Sends the code to an LLM (via [Groq API](https://groq.com/))
- 💬 Returns:
  - A full explanation of your code with in-line comments
  - The **Big O time complexity**
- 📊 Extracts the complexity and plots it visually using `matplotlib`
- 🎨 Includes a custom dark theme to match LeetCode’s aesthetic

---

## ✨ Why I Built It

> I was solving LeetCode problems and loved their AI Analysis feature—  
> until I realized it needed a subscription.  
> So I built my own version. 😊

---

## 🛠 Tech Stack

- Python 🐍
- [Groq LLM API](https://groq.com/)
- `matplotlib` for styled plotting
- `streamlit` for UI (optional, if you add UI later)
- Custom `.mplstyle` for LeetCode-themed plots
- File extension detection from scratch (`detect_lang.py`)

---

## 📦 How to Use

1. Clone this repo:

   ```bash
   git clone https://github.com/ramahany/Analysis_app.git
   cd CodeComplexityAnalyzer

2. Install requirements:

   ```bash
    pip install -r requirements.txt

3. Add your Groq API key to a secrets config or environment variable.
4. Run the script:

   ```bash
    streamlit run streamlit_app.py

5. Choose your input:
  -Upload a file (.py, .js, .cpp, etc.) — language will be auto-detected
  -Or paste code manually and select the language

6. Get results:
  -🟢 AI-generated explanation with comments
  -🟢 Time complexity in Big O notation
  -🟢 Visual plot of performance
   
---

## 🎯 Sample Output

![image](https://github.com/user-attachments/assets/7a7265eb-d027-456b-aa83-d5866031a54b)

### ➡️ Output:
-Time Complexity: O(n²)
-Annotated Code: Each line is explained with clear comments
-Plot: Matplotlib graph styled like LeetCode’s UI

## 🔗 Links
-🔥 Project Link: [https://code0analysis0app.streamlit.app]
-💻 GitHub Repo: github.com/ramahany/Analysis_app



