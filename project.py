import tkinter as tk
from tkinter import messagebox
import random
# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Game Hub")
root.geometry("600x600")
root.config(bg="#0f172a")
# ---------------- LOGO ----------------
logo = tk.Label(
    root,
    text="🎮 4ByteGames 🎮",
    font=("Arial", 26, "bold"),
    fg="#22c55e",
    bg="#0f172a"
)
logo.pack(pady=20)
#-------------Tag Line-----------------
tagline = tk.Label(
    root,
    text="Play Smart. Play Fast",
    font=("Arial", 12, "bold"),
    fg="#facc15",
    bg="#0f172a"
)
tagline.pack(pady=5)
# ---------------- BUTTON STYLE ----------------
def game_button(text, command):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 12, "bold"),
        bg="#1e293b",
        fg="#38bdf8",
        activebackground="#334155",
        activeforeground="white",
        width=25,
        height=2,
        bd=0
    )
def sub_button(parent, text, command, width=20):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg="#1e293b",
        fg="#38bdf8",
        activebackground="#334155",
        activeforeground="white",
        width=width,
        height=2,
        bd=0
    )
def sub_label(parent, text, font=("Arial", 12), fg="white"):
    return tk.Label(parent, text=text, bg="#0f172a", fg=fg, font=font)
def styled_window(title, size="380x420"):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry(size)
    win.config(bg="#0f172a")
    return win
# =====================================================
# 🎯 TIC TAC TOE (GUI)
# =====================================================
def tic_tac_toe():
    mode_win = styled_window("Select Mode", "300x200")
    sub_label(mode_win, "Choose Mode", fg="#22c55e").pack(pady=15)
    def start_game(vs_ai):
        mode_win.destroy()
        launch(vs_ai)
    def launch(vs_ai):
        window = styled_window("Tic Tac Toe", "380x420")
        board = [""] * 9
        player = ["X"]
        def check_win(p):
            wins = [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]
            return any(board[a]==board[b]==board[c]==p for a,b,c in wins)
        def ai_move():
            empty = [i for i in range(9) if board[i] == ""]
            if empty:
                i = random.choice(empty)
                board[i] = "O"
                buttons[i].config(text="O")
        def play_again():
            window.destroy()
            launch(vs_ai)
        def click(i):
            if board[i] == "":
                board[i] = player[0]
                buttons[i].config(text=player[0])

                if check_win(player[0]):
                    window.update()
                    again = messagebox.askyesno("Winner", f"{player[0]} Wins! 🎉\nPlay again?")
                    if again:
                        play_again()
                    else:
                        window.destroy()
                    return

                if "" not in board:
                    again = messagebox.askyesno("Draw", "Match Draw! 🤝\nPlay again?")
                    if again:
                        play_again()
                    else:
                        window.destroy()
                    return

                player[0] = "O" if player[0] == "X" else "X"

                if vs_ai and player[0] == "O":
                    ai_move()
                    window.update()

                    if check_win("O"):
                        again = messagebox.askyesno("Winner", "AI Wins! 💻\nPlay again?")
                        if again:
                            play_again()
                        else:
                            window.destroy()
                        return
                    if "" not in board:
                        again = messagebox.askyesno("Draw", "Match Draw! 🤝\nPlay again?")
                        if again:
                            play_again()
                        else:
                            window.destroy()
                        return
                    player[0] = "X"
        frame = tk.Frame(window, bg="#0f172a")
        frame.pack(pady=20)
        buttons = []
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20),
                            width=5, height=2,
                            command=lambda i=i: click(i),
                            bg="#1e293b", fg="white", bd=0,
                            activebackground="#334155")
            btn.grid(row=i//3, column=i%3, padx=4, pady=4)
            buttons.append(btn)
    sub_button(mode_win, "👥 Player vs Player", lambda: start_game(False)).pack(pady=8)
    sub_button(mode_win, "🤖 Player vs AI", lambda: start_game(True)).pack(pady=8)
# =====================================================
# 🔢 GUESS
# =====================================================
def number_guess():
    mode_win = styled_window("Select Mode", "300x200")
    sub_label(mode_win, "Choose Mode", fg="#22c55e").pack(pady=15)
    def number_mode():
        mode_win.destroy()
        launch_number()
    def launch_number():
        num = random.randint(1, 100)
        win = styled_window("Number Guess", "350x280")
        sub_label(win, "Guess (1-100)", fg="#22c55e").pack(pady=15)
        entry = tk.Entry(win, font=("Arial", 12), bg="#1e293b", fg="white",
                         insertbackground="white", width=10, justify="center")
        entry.pack(pady=5)
        label = sub_label(win, "")
        label.pack(pady=5)
        def check():
            try:
                g = int(entry.get())
                if g > num:
                    label.config(text="Too High 📈", fg="#f87171")
                elif g < num:
                    label.config(text="Too Low 📉", fg="#facc15")
                else:
                    again = messagebox.askyesno("Win", "🎉 Correct!\nPlay again?")
                    if again:
                        win.destroy()
                        launch_number()
                    else:
                        win.destroy()
            except ValueError:
                label.config(text="Invalid", fg="#f87171")
        sub_button(win, "✅ Check", check).pack(pady=10)
    def word_mode():
        mode_win.destroy()
        launch_word()
    def load_words():
        with open(r"C:\Users\Aarav\OneDrive\Desktop\python\word.txt", "r",) as f:
            words = [line.strip().lower() for line in f if line.strip().isalpha()]
        return words
    def launch_word():
        words = load_words()
        word = random.choice(words)
        attempts = [0]
        revealed = ["_"] * len(word)
        win = styled_window("Word Guess", "400x360")
        sub_label(win, f"Guess the word  |  {len(word)} letters", fg="#22c55e").pack(pady=10)
        blanks_label = sub_label(win, " ".join(revealed), font=("Arial", 20, "bold"), fg="#facc15")
        blanks_label.pack(pady=5)
        attempts_label = sub_label(win, f"Attempts: {attempts[0]}", fg="#38bdf8")
        attempts_label.pack()
        hint_label = sub_label(win, f"Hint: First letter is '{word[0].upper()}'", fg="gray")
        hint_label.pack(pady=3)
        entry = tk.Entry(win, font=("Arial", 12), bg="#1e293b", fg="white",
                         insertbackground="white", width=15, justify="center")
        entry.pack(pady=8)
        result_label = sub_label(win, "")
        result_label.pack(pady=3)
        def reveal_letter():
            for idx, ch in enumerate(word):
                if revealed[idx] == "_":
                    revealed[idx] = ch.upper()
                    break
            blanks_label.config(text=" ".join(revealed))
        def check():
            guess = entry.get().lower().strip()
            entry.delete(0, tk.END)
            if guess == word:
                blanks_label.config(text=" ".join(list(word.upper())))
                again = messagebox.askyesno("Win", f"🎉 Correct! The word was '{word}'\nPlay again?")
                if again:
                    win.destroy()
                    launch_word()
                else:
                    win.destroy()
                return
            attempts[0] += 1
            attempts_label.config(text=f"Attempts: {attempts[0]}")
            if attempts[0] % 2 == 0:
                reveal_letter()
                hint_label.config(text="💡 A letter has been revealed!", fg="#facc15")
            else:
                hint_label.config(text=f"Hint: First letter is '{word[0].upper()}'", fg="gray")
            result_label.config(text="Wrong ❌ Try again!", fg="#f87171")
        sub_button(win, "✅ Check", check).pack(pady=8)
    sub_button(mode_win, "🔢 Number Guess", number_mode).pack(pady=8)
    sub_button(mode_win, "🔤 Word Guess", word_mode).pack(pady=8)
# =====================================================
# ✊ RPS
# =====================================================
def rps():
    def launch():
        choices = ["rock", "paper", "scissors"]
        choice_buttons = []
        def play(user):
            for btn in choice_buttons:
                btn.config(state="disabled")
            comp = random.choice(choices)
            icons = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
            if user == comp:
                result.set(f"You: {icons[user]}  vs  AI: {icons[comp]}\nDraw 🤝")
                result_label.config(fg="#facc15")
            elif (user == "rock" and comp == "scissors") or \
                    (user == "paper" and comp == "rock") or \
                    (user == "scissors" and comp == "paper"):
                result.set(f"You: {icons[user]}  vs  AI: {icons[comp]}\nYou Win 🎉")
                result_label.config(fg="#22c55e")
            else:
                result.set(f"You: {icons[user]}  vs  AI: {icons[comp]}\nComputer Wins 💻")
                result_label.config(fg="#f87171")
            result_label.config(text=result.get())
            again_btn.pack(pady=8)
        win = styled_window("Rock Paper Scissors", "380x320")
        sub_label(win, "Make your choice!", fg="#22c55e").pack(pady=15)
        result = tk.StringVar()
        btn_frame = tk.Frame(win, bg="#0f172a")
        btn_frame.pack(pady=10)
        for c in choices:
            btn = sub_button(btn_frame, c.capitalize(), lambda c=c: play(c), width=10)
            btn.pack(side="left", padx=6)
            choice_buttons.append(btn)
        result_label = sub_label(win, "", fg="white")
        result_label.pack(pady=10)
        def again():
            win.destroy()
            launch()
        again_btn = sub_button(win, "🔄 Play Again", again, width=15)
    launch()
# =====================================================
# 🧠 MEMORY GAME
# =====================================================
def memory_game():
    def launch():
        nums = [str(random.randint(0,9)) for _ in range(4)]
        win = styled_window("Memory Game", "380x300")
        sub_label(win, "Memorize the numbers!", fg="#22c55e").pack(pady=10)
        label = tk.Label(win, text=" ".join(nums), fg="#facc15", bg="#0f172a",
                         font=("Arial", 28, "bold"))
        label.pack(pady=10)
        hint = sub_label(win, "Memorize them... 👀", fg="gray")
        hint.pack()
        entry = tk.Entry(win, font=("Arial", 12), bg="#1e293b", fg="white",
                         insertbackground="white", width=15, justify="center",
                         state="disabled")
        entry.pack(pady=10)
        submit_btn = sub_button(win, "✅ Submit", lambda: None)
        submit_btn.config(state="disabled")
        submit_btn.pack(pady=5)
        def hide_numbers():
            label.config(text="❓ ❓ ❓ ❓")
            hint.config(text="Type the numbers separated by spaces")
            entry.config(state="normal")
            submit_btn.config(state="normal", command=check)
        def check():
            if entry.get().split() == nums:
                again = messagebox.askyesno("Result", "🎉 Correct!\nPlay again?")
            else:
                again = messagebox.askyesno("Result", f"❌ Wrong! Answer was {' '.join(nums)}\nPlay again?")
            if again:
                win.destroy()
                launch()
            else:
                win.destroy()
        win.after(2000, hide_numbers)
    launch()
# =====================================================
# 🎮 BUTTONS
# =====================================================
game_button("🎯 Tic Tac Toe", tic_tac_toe).pack(pady=10)
game_button("🔢 Guess Game", number_guess).pack(pady=10)
game_button("✊ Rock Paper Scissors", rps).pack(pady=10)
game_button("🧠 Memory Game", memory_game).pack(pady=10)
exit_btn = tk.Button(
    root,
    text="❌ Exit",
    command=root.destroy,
    font=("Arial", 12, "bold"),
    bg="#ef4444",          # red background
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    width=25,
    height=2,
    bd=0
)
exit_btn.pack(pady=20)
# ---------------- FOOTER ----------------
tk.Label(
    root,
    text="Gaming UI Project 💻",
    bg="#0f172a",
    fg="gray"
).pack(side="bottom", pady=10)
# ---------------- RUN ----------------
root.mainloop()