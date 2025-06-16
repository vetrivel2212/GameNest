def play():
    import sys

    questions = (
        "1. How many elements are in the periodic table?",
        "2. How many bones are there in the human body?",
        "3. What is the capital of France?",
        "4. What is the largest planet in our solar system?",
        "5. Who wrote 'Romeo and Juliet'?",
        "6. What is the chemical symbol for water?",
        "7. How many continents are there on Earth?",
        "8. What is the hardest natural substance on Earth?",
        "9. Who painted the Mona Lisa?",
        "10. What is the smallest prime number?",
        "11. What is the boiling point of water?",
        "12. Who is known as the father of computers?",
        "13. What is the longest river in the world?",
        "14. What is the most spoken language in the world?",
        "15. What is the largest ocean on Earth?",
        "16. Who discovered penicillin?",
        "17. What is the speed of light?",
        "18. How many planets are there in our solar system?",
        "19. Who was the first president of the United States?",
        "20. What is the currency of Japan?"
    )

    options = (
        ("A. 117", "B. 118", "C. 119", "D. 120"),
        ("A. 205", "B. 206", "C. 207", "D. 208"),
        ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
        ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
        ("A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"),
        ("A. H2O", "B. H2", "C. O2", "D. OH"),
        ("A. 5", "B. 6", "C. 7", "D. 8"),
        ("A. Gold", "B. Diamond", "C. Iron", "D. Granite"),
        ("A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Claude Monet"),
        ("A. 1", "B. 2", "C. 3", "D. 5"),
        ("A. 90°C", "B. 100°C", "C. 110°C", "D. 120°C"),
        ("A. Isaac Newton", "B. Charles Babbage", "C. Alan Turing", "D. Thomas Edison"),
        ("A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"),
        ("A. English", "B. Spanish", "C. Mandarin", "D. Hindi"),
        ("A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"),
        ("A. Alexander Fleming", "B. Marie Curie", "C. Louis Pasteur", "D. Gregor Mendel"),
        ("A. 299,792,458 m/s", "B. 150,000,000 m/s", "C. 3,000,000 m/s", "D. 30,000 m/s"),
        ("A. 7", "B. 8", "C. 9", "D. 10"),
        ("A. Abraham Lincoln", "B. George Washington", "C. Thomas Jefferson", "D. John Adams"),
        ("A. Yuan", "B. Yen", "C. Won", "D. Rupee")
    )

    answers = ["B", "B", "C", "C", "B", "A", "C", "B", "A", "B",
               "B", "B", "B", "C", "D", "A", "A", "B", "B", "B"]

    print("🎮 Welcome to the GameNest Quiz Center!")
    name = input("What's your name, champ? 🧠: ").title()
    print(f"\nAlright {name}, let's see how sharp you are!\n")

    score = 0
    questions_answered = 0

    for i in range(len(questions)):
        print("\n" + "*" * 50)
        print(questions[i])
        for opt in options[i]:
            print(opt)

        while True:
            guess = input("Enter your answer (A/B/C/D): ").strip().upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("❌ Invalid option. Choose A, B, C, or D.")

        if guess == answers[i]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is {answers[i]}")

        questions_answered += 1

        if i != len(questions) - 1:
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == 'n':
                break

    print("\n🎉 Well played, " + name + "!")
    print(f"🏆 Final Score: {score}/{questions_answered}")
    percentage = (score / questions_answered) * 100
    print(f"📊 Your accuracy: {percentage:.2f}%")

# Optional for testing
if __name__ == '__main__':
    play()
