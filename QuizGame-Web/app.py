from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session management

# Quiz Questions
questions = [
    {"text": "What is the capital city of Kenya?", "options": ["Nairobi", "Mombasa", "Kisumu", "Nakuru"], "correct": "Nairobi"},
    {"text": "Who is the current president of Kenya?", "options": ["Uhuru Kenyatta", "Raila Odinga", "Zakayo", "William Ruto"], "correct": "Zakayo"},
    {"text": "How many counties does Kenya have?", "options": ["47", "42", "50", "39"], "correct": "47"},
    {"text": "In what year did Kenya gain independence?", "options": ["1963", "1975", "1950", "1960"], "correct": "1963"},
    {"text": "What is the staple food in Kenya?", "options": ["Sembe", "Ugali", "Rice", "Chapati"], "correct": "Sembe"},
    {"text": "What draws tourists to Kenya?", "options": ["Wild animals", "Beaches", "Mountains", "Shopping"], "correct": "Wild animals"},
    {"text": "Which woman won a Nobel Prize from Kenya?", "options": ["Wangari Maathai", "Ngugi Wa Thiong'o", "Amina Mohamed", "Grace Ogot"], "correct": "Wangari Maathai"},
    {"text": "Which rebels from Central Kenya fought for independence?", "options": ["Mau Mau", "Shifta", "Meru", "Luo"], "correct": "Mau Mau"},
    {"text": "Which Olympic activity does Kenya dominate in?", "options": ["Athletics", "Swimming", "Gymnastics", "Shooting"], "correct": "Athletics"},
    {"text": "Who are the top Kenyan street hip-hop artistes?", "options": ["Wakadinali", "Sauti Sol", "H_art the Band", "K-Drama"], "correct": "Wakadinali"},
]

total_questions = len(questions)

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize session variables
    if "current_index" not in session:
        session["current_index"] = 0
        session["score"] = 0
        session["incorrect_questions"] = []

    current_index = session["current_index"]

    # If all questions answered, redirect to result
    if current_index >= total_questions:
        return redirect(url_for("result"))

    current_question = questions[current_index]

    if request.method == "POST":
        selected = request.form.get("answer")
        if selected != current_question["correct"]:
            # Store incorrect question info
            session["incorrect_questions"].append({
                "question": current_question["text"],
                "answer": selected,
                "correct": current_question["correct"]
            })
        else:
            session["score"] += 1

        session["current_index"] += 1
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        question=current_question,
        total_questions=total_questions,
        current_index=current_index,
        score=session.get("score", 0)
    )

@app.route("/result")
def result():
    score = session.get("score", 0)
    incorrect_questions = session.get("incorrect_questions", [])
    session.clear()  # Reset for next game
    return render_template(
        "result.html",
        score=score,
        total=total_questions,
        incorrect_questions=incorrect_questions
    )

if __name__ == "__main__":
    app.run(debug=True)
