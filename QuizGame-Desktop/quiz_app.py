import tkinter as tk
from tkinter import messagebox
import random

# -------------------------------
# QUIZ DATA (Question, [Options], Correct Option)
# -------------------------------
questions = [
    ("What is the capital city of Kenya?",
     ["Nairobi", "Mombasa", "Kisumu", "Eldoret"], "Nairobi"),

    ("Who is the current president of Kenya?",
     ["Uhuru Kenyatta", "William Ruto", "Raila Odinga", "Musalia Mudavadi"], "William Ruto"),

    ("How many counties does Kenya have?",
     ["42", "45", "47", "50"], "47"),

    ("In what year did Kenya gain independence?",
     ["1963", "1978", "1952", "1980"], "1963"),

    ("What is the staple food in Kenya?",
     ["Rice", "Chapati", "Ugali", "Potatoes"], "Ugali"),

    ("What draws tourists to Kenya?",
     ["Mountains", "Wildlife", "Lakes", "Caves"], "Wildlife"),

    ("Which woman won a Nobel Prize from Kenya?",
     ["Grace Onyango", "Charity Ngilu", "Wangari Maathai", "Martha Karua"], "Wangari Maathai"),

    ("Which rebels from Central Kenya fought for independence?",
     ["Kikuyu Council", "Mau Mau", "Freedom Front", "Kamba Warriors"], "Mau Mau"),

    ("Which Olympic activity does Kenya dominate in?",
     ["Swimming", "Athletics", "Boxing", "Cycling"], "Athletics"),

    ("Who are the top Kenyan street hip-hop artistes?",
     ["Khaligraph Jones", "Wakadinali", "Octopizzo", "Nyashinski"], "Wakadinali"),
]

# Shuffle the questions for variety each time you play
random.shuffle(questions)


# -------------------------------
# APP CLASS
# -------------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇰🇪 Kenyan Quiz Game")
        self.root.geometry("600x450")
        self.root.config(bg="#f2f2f2")

        self.score = 0
        self.q_index = 0

        self.title_label = tk.Label(
            root, text="Kenyan Quiz Game 🇰🇪", font=("Helvetica", 18, "bold"), bg="#f2f2f2"
        )
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(
            root, text="", font=("Helvetica", 14), wraplength=500, justify="center", bg="#f2f2f2"
        )
        self.question_label.pack(pady=20)

        # Radio buttons for choices
        self.choice_var = tk.StringVar()
        self.buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                root,
                text="",
                variable=self.choice_var,
                value="",
                font=("Helvetica", 12),
                bg="#f2f2f2",
                anchor="w",
                justify="left"
            )
            btn.pack(fill="x", padx=100, pady=2)
            self.buttons.append(btn)

        self.submit_btn = tk.Button(
            root, text="Submit", command=self.check_answer,
            font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white"
        )
        self.submit_btn.pack(pady=15)

        self.status_label = tk.Label(
            root, text="", font=("Helvetica", 12), bg="#f2f2f2"
        )
        self.status_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q, options, _ = questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index + 1}. {q}")
            self.choice_var.set(None)
            random.shuffle(options)

            for i, opt in enumerate(options):
                self.buttons[i].config(text=f"{chr(65 + i)}. {opt}", value=opt)

            self.status_label.config(text=f"Question {self.q_index + 1} of {len(questions)}")
        else:
            self.end_game()

    def check_answer(self):
        selected = self.choice_var.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer before submitting!")
            return

        correct = questions[self.q_index][2]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ Correct answer!")
        else:
            messagebox.showerror("Wrong!", f"❌ Wrong! Correct answer: {correct}")

        self.q_index += 1
        self.load_question()

    def end_game(self):
        percentage = round((self.score / len(questions)) * 100, 2)
        messagebox.showinfo(
            "Quiz Complete 🎉",
            f"You scored {self.score}/{len(questions)} ({percentage}%)"
        )
        self.root.destroy()


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
