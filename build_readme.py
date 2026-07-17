import os
import re
import json
import urllib.request
from datetime import datetime, timezone

# Path configuration
REPO_ROOT = "."
README_PATH = "README.md"

def get_problem_folders():
    folders = []
    # Matches folders named like '0001-two-sum' or '0001-Two-Sum'
    pattern = re.compile(r"^(\d{4})-(.+)$")
    
    for entry in os.listdir(REPO_ROOT):
        full_path = os.path.join(REPO_ROOT, entry)
        if os.path.isdir(full_path):
            match = pattern.match(entry)
            if match:
                num = match.group(1)
                slug = match.group(2)
                folders.append((num, slug, full_path, entry))
    return sorted(folders, key=lambda x: x[0])

def fetch_leetcode_difficulty(title_slug):
    """Fetches real difficulty directly from LeetCode's GraphQL API"""
    url = "https://leetcode.com/graphql"
    graphql_query = {
        "query": """
        query questionTitle($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": title_slug.lower()}
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(graphql_query).encode("utf-8"), 
            headers=headers, 
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            difficulty = res_data["data"]["question"]["difficulty"]
            return difficulty  # Returns "Easy", "Medium", or "Hard"
    except Exception:
        return "Easy" # Safe fallback fallback if API drops out

def parse_problem_metadata(folder_path, slug):
    # Fetch accurate live difficulty status 
    difficulty = fetch_leetcode_difficulty(slug)
    language = "Python 3"
    
    # Check for solution file extension to track languages used
    for file in os.listdir(folder_path):
        if file.endswith(".py"):
            language = "Python 3"
        elif file.endswith(".cpp"):
            language = "C++"
        elif file.endswith(".java"):
            language = "Java"
        elif file.endswith(".sql"):
            language = "MySQL"

    # Capture the historical file modification date
    date_str = datetime.now().strftime("%Y-%m-%d")
    for file in os.listdir(folder_path):
        if not file.startswith("."):
            mtime = os.path.getmtime(os.path.join(folder_path, file))
            date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            break

    return difficulty, language, date_str

def generate_dashboard():
    problems = get_problem_folders()
    
    stats = {"Easy": 0, "Medium": 0, "Hard": 0}
    table_rows = []
    
    print(f"Processing {len(problems)} problems. Fetching structural metadata...")
    for num, slug, folder_path, folder_name in problems:
        difficulty, language, date_str = parse_problem_metadata(folder_path, slug)
        stats[difficulty] = stats.get(difficulty, 0) + 1
        
        # Format the title strings cleanly
        problem_title = slug.replace("-", " ").title()
        problem_title = problem_title.replace("Of ", "of ").replace("In ", "in ").replace("And ", "and ").replace("To ", "to ")
        
        problem_link = f"https://leetcode.com/problems/{slug.lower()}/"
        solution_link = f"./{folder_name}"
        
        row = f"| {num} | [{problem_title}]({problem_link}) | [{folder_name}]({solution_link}) | {difficulty} | {language} | {date_str} |"
        table_rows.append(row)
        
    total_solved = len(problems)
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    
    # Building Markdown UI layout
    markdown = f"""# 🏆 LeetCode Solutions

<p align="center">
  <img src="https://img.shields.io/badge/TOTAL%20SOLVED-{total_solved}-blue?style=for-the-badge&logo=leetcode" />
  <img src="https://img.shields.io/badge/EASY-{stats['Easy']}-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MEDIUM-{stats['Medium']}-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/HARD-{stats['Hard']}-red?style=for-the-badge" />
</p>

## 📊 Statistics

| Metric | Count |
| :--- | :--- |
| **Total Solved** | {total_solved} |
| **Easy** | {stats['Easy']} |
| **Medium** | {stats['Medium']} |
| **Hard** | {stats['Hard']} |
| **Languages** | MySQL, Python 3 |
| **Last Updated** | {current_time} |

## 📁 Solutions

| # | Problem | Solution | Difficulty | Language | Date |
| :-: | :--- | :--- | :-: | :-: | :-: |
""" + "\n".join(table_rows) + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)
    print("Dashboard generated successfully!")

if __name__ == "__main__":
    generate_dashboard()
