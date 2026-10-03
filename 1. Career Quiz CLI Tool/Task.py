# Career Path Quiz Questions and Options

questions = [
    {
        "question": "Q1. Which activity excites you the most?",
        "options": {
            "A": ("Starting a business or trading", "Business"),
            "B": ("Building apps or coding", "Technology"),
            "C": ("Public speaking or writing", "Communication"),
            "D": ("Painting, designing, or performing", "Art")
        }
    },

    {
        "question": "Q2. What type of problem do you enjoy solving?",
        "options": {
            "A": ("Social challenges like resolving conflicts", "Communication"),
            "B": ("Financial challenges like managing investments", "Business"),
            "C": ("Creative challenges like designing a logo", "Art"),
            "D": ("Technical challenges like debugging software", "Technology")
        }
    },

    {
        "question": "Q3. Which tool would you prefer to master?",
        "options": {
            "A": ("Presentation software or social media platforms", "Communication"),
            "B": ("Programming languages", "Technology"),
            "C": ("Photoshop or musical instruments", "Art"),
            "D": ("Excel, trading platforms, or business models", "Business")
        }
    },

    {
        "question": "Q4. Imagine a group project. What role do you take?",
        "options": {
            "A": ("The one who communicates ideas and motivates the team", "Communication"),
            "B": ("The one who handles technical setup", "Technology"),
            "C": ("The one who organizes finances and strategy", "Business"),
            "D": ("The one who designs visuals or creative aspects", "Art")
        }
    },

    {
        "question": "Q5. What kind of success story inspires you most?",
        "options": {
            "A": ("An entrepreneur building a successful company", "Business"),
            "B": ("A journalist or influencer shaping public opinion", "Communication"),
            "C": ("An artist gaining global recognition", "Art"),
            "D": ("A software engineer creating a breakthrough app", "Technology")
        }
    },

    {
        "question": "Q6. Which environment do you thrive in?",
        "options": {
            "A": ("Studios, theaters, or galleries", "Art"),
            "B": ("Offices, trading floors, or startups", "Business"),
            "C": ("Labs, coding bootcamps, or tech hubs", "Technology"),
            "D": ("Conferences, classrooms, or media houses", "Communication")
        }
    },

    {
        "question": "Q7. How do you prefer to express yourself?",
        "options": {
            "A": ("Through speeches, writing, or digital content", "Communication"),
            "B": ("Through colors, music, or performance", "Art"),
            "C": ("Through financial strategies or business ventures", "Business"),
            "D": ("Through innovative software or gadgets", "Technology")
        }
    },

    {
        "question": "Q8. Which skill would you like to be known for?",
        "options": {
            "A": ("Leadership and entrepreneurship", "Business"),
            "B": ("Persuasion and clarity in communication", "Communication"),
            "C": ("Problem-solving with technology", "Technology"),
            "D": ("Creativity and originality", "Art")
        }
    },

    {
        "question": "Q9. If given unlimited resources, what project would you start?",
        "options": {
            "A": ("Start a global awareness campaign", "Communication"),
            "B": ("Create a multinational company", "Business"),
            "C": ("Build an AI-powered app", "Technology"),
            "D": ("Launch an art exhibition or music album", "Art")
        }
    },

    {
        "question": "Q10. Which compliment would make you happiest?",
        "options": {
            "A": ("Your creativity is unmatched!", "Art"),
            "B": ("You're an amazing communicator!", "Communication"),
            "C": ("You're a genius with tech!", "Technology"),
            "D": ("You have a sharp business mind!", "Business")
        }
    }
]


# Starting scores
scores = {
    "Technology": 0,
    "Art": 0,
    "Business": 0,
    "Communication": 0
}


# Run the quiz
for question in questions:
    print("\n" + question["question"])

    for letter, option in question["options"].items():
        print(letter + ". " + option[0])

    answer = input("Choose A, B, C, or D: ").upper()

    while answer not in question["options"]:
        print("Please enter A, B, C, or D.")
        answer = input("Choose A, B, C, or D: ").upper()

    category = question["options"][answer][1]
    scores[category] += 1


# Show the scores
print("\n===== QUIZ RESULTS =====")

for category, score in scores.items():
    print(category + ":", score)


# Find the highest score
highest_score = max(scores.values())

top_categories = []

for category, score in scores.items():
    if score == highest_score:
        top_categories.append(category)


# Show the final result
print("\n===== CAREER RESULT =====")

if len(top_categories) == 1:
    print("Your strongest career area is:", top_categories[0])
else:
    print("You have a tie between:")

    for category in top_categories:
        print("-", category)

input("\nPress Enter to exit...")