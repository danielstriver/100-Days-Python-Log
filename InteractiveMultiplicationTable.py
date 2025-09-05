# 🚀✨ Welcome to the Multiplication Adventure! ✨🚀
# ------------------------------------------------
# This fun little terminal game helps you practice multiplication tables 🎯
# Inspired by the courage to guide my nieces (and future kids 😅👨‍👧‍👦).
# Stay sharp, stay curious, and let’s lock in that math knowledge 💪🧠

print("🌟👋 Welcome, Math Explorer! 👋🌟")
print("Today, we’re going on a journey through multiplication tables 🔢✨")
print("Answer all the questions to prove your math superpowers! 🦸‍♂️🦸‍♀️\n")

user_attempts = 0

# 🎲 Ask the player what number they want to practice
number = int(input("👉 Enter the number you want to learn (e.g., 2, 5, 7): "))

print(f"\n🎉 Awesome choice! Let’s explore the {number} multiplication table together! 🎉\n")

# 🔁 Loop through 1–12 to quiz the player
for i in range(1, 13):
    user_answer = int(input(f"{number} x {i} = ? 🤔 "))
    correct_answer = number * i
    
    if user_answer == correct_answer:
        print("✅ Woohoo! You got it right! 🎊")
        user_attempts += 1
    else:
        print(f"❌ Oops! The correct answer is {correct_answer}. Keep going, champ! 💪")

# 🏆 End of game results
print("\n🔔 Results Time! 🔔")
if user_attempts == 12:
    print("🌟 Congratulations, Math Master! 🌟 You got ALL of them right! 🎉🔥")
else:
    print(f"👏 You got {user_attempts} out of 12 right.")
    print("💡 Pro tip: Re-run the game to keep sharpening those math skills! 🚀")
