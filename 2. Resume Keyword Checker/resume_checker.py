# Read the resume
with open("resume.txt", "r") as file:
    resume = file.read().lower()

# Keywords from the sample job posting
keywords = [
    "python",
    "machine learning",
    "data analysis",
    "sql",
    "communication",
    "teamwork",
    "problem solving",
    "leadership",
    "git",
    "embedded systems"
]

# Check which keywords are present or missing
present = []
missing = []

for keyword in keywords:
    if keyword in resume:
        present.append(keyword)
    else:
        missing.append(keyword)

# Display the results
print("RESUME KEYWORD CHECKER")
print("----------------------")

print("\nKeywords Present:")
for keyword in present:
    print("-", keyword)

print("\nKeywords Missing:")
for keyword in missing:
    print("-", keyword)