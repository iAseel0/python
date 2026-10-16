import random
import tkinter as tk
from tkinter import messagebox


class RoundedButton(tk.Canvas):
  

  def __init__(
      self,
      master,
      text,
      command,
      bg_color="#FF6B97",
      fg_color="#FFFFFF",
      width=180,
      height=40,
      radius=15,
  ):
    super().__init__(
        master,
        width=width,
        height=height,
        bg=master["bg"],
        highlightthickness=0,
    )
    self.command = command
    self.bg_color = bg_color
    self.fg_color = fg_color
    self.text = text
    self.radius = radius
    self.width = width
    self.height = height

    self.draw_rounded_rect()
    self.bind("<Button-1>", lambda e: self.command())

  def draw_rounded_rect(self):
    self.delete("all")
    r = self.radius
    w = self.width
    h = self.height

  
    self.create_arc(0, 0, 2 * r, 2 * r, start=90, extent=90, fill=self.bg_color, outline=self.bg_color)
    self.create_arc(w - 2 * r, 0, w, 2 * r, start=0, extent=90, fill=self.bg_color, outline=self.bg_color)
    self.create_arc(0, h - 2 * r, 2 * r, h, start=180, extent=90, fill=self.bg_color, outline=self.bg_color)
    self.create_arc(w - 2 * r, h - 2 * r, w, h, start=270, extent=90, fill=self.bg_color, outline=self.bg_color)
    
    self.create_rectangle(r, 0, w - r, h, fill=self.bg_color, outline=self.bg_color)
    self.create_rectangle(0, r, w, h - r, fill=self.bg_color, outline=self.bg_color)


    self.create_text(w / 2, h / 2, text=self.text, fill=self.fg_color, font=("Verdana", 9, "bold"))


class TicTacToeApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Tic-Tac-Toe Dashboard")
    self.root.geometry("540x640")
    self.root.configure(bg="#FDF8F9")  # Soft Light Cream Background
    self.root.resizable(False, False)

    # Game state variables
    self.board = [" "] * 9
    self.current_player = "X"
    self.user_symbol = "X"
    self.computer_symbol = "O"
    self.game_mode = "Computer"
    self.game_active = False

    # Score board
    self.scores = {"X": 0, "O": 0, "Draws": 0}

    # Main Container
    self.container = tk.Frame(self.root, bg="#FDF8F9")
    self.container.pack(fill="both", expand=True)

    self.show_welcome_screen()

 
  def show_welcome_screen(self):
    for widget in self.container.winfo_children():
      widget.destroy()

    welcome_frame = tk.Frame(self.container, bg="#FDF8F9")
    welcome_frame.pack(fill="both", expand=True, padx=30, pady=40)

    tk.Label(welcome_frame, text="", bg="#FDF8F9").pack(pady=20)

    # Title
    lbl_title = tk.Label(
        welcome_frame,
        text=" T I C - T A C - T O E ",
        font=("Verdana", 20, "bold"),
        fg="#D94680",
        bg="#FDF8F9",
    )
    lbl_title.pack(pady=10)

    lbl_sub = tk.Label(
        welcome_frame,
      
        font=("Verdana", 10),
        fg="#6B7280",
        bg="#FDF8F9",
        justify="center",
    )
    lbl_sub.pack(pady=10)

    # Canvas for Smooth Graphic animation
    self.canvas = tk.Canvas(
        welcome_frame,
        width=180,
        height=140,
        bg="#FDF8F9",
        highlightthickness=0,
    )
    self.canvas.pack(pady=15)
    self.anim_step = 0
    self.animate_welcome()

    # Smooth Start Button
    btn_start = RoundedButton(
        welcome_frame,
        text="✨ START GAME ✨",
        command=self.show_game_screen,
        bg_color="#FF6B97",
        fg_color="#FFFFFF",
        width=200,
        height=45,
        radius=20,
    )
    btn_start.pack(pady=20)

    # Footer Signature
    lbl_signature = tk.Label(
        welcome_frame,
        text="made with love by Aseel ",
        font=("Verdana", 8, "italic"),
        fg="#9CA3AF",
        bg="#FDF8F9",
    )
    lbl_signature.pack(side="bottom", pady=10)

  def animate_welcome(self):
    if not hasattr(self, "canvas") or not self.canvas.winfo_exists():
      return
    self.canvas.delete("all")
    colors = ["#FF6B97", "#8A4FFF", "#10B981", "#F59E0B"]
    c1 = colors[self.anim_step % len(colors)]
    c2 = colors[(self.anim_step + 1) % len(colors)]

    # رسم أشكال دائرية ناعمة متحركة
    self.canvas.create_oval(20, 20, 90, 90, outline=c1, width=3)
    self.canvas.create_oval(100, 40, 160, 100, outline=c2, width=3)
    self.canvas.create_text(
        95, 120, text="PLAY NOW", font=("Verdana", 11, "bold"), fill="#374151"
    )

    self.anim_step += 1
    self.root.after(700, self.animate_welcome)

  # ==========================================
  # 2. GAME DASHBOARD SCREEN (لوحة اللعب بحواف ناعمة ومنحنية)
  # ==========================================
  def show_game_screen(self):
    for widget in self.container.winfo_children():
      widget.destroy()

    main_layout = tk.Frame(self.container, bg="#FDF8F9")
    main_layout.pack(fill="both", expand=True, padx=15, pady=15)

    # --- LEFT SIDEBAR (لوحة النتائج بحواف دائرية ناعمة) ---
    left_panel = tk.Frame(
        main_layout,
        bg="#FFFFFF",
        highlightbackground="#F3E8EE",
        highlightthickness=2,
        width=150,
    )
    left_panel.pack(side="left", fill="y", padx=(0, 10))
    left_panel.pack_propagate(False)

    btn_back = tk.Button(
        left_panel,
        text="☰ الرئيسية",
        font=("Verdana", 9, "bold"),
        bg="#FFF0F3",
        fg="#D94680",
        relief="flat",
        cursor="hand2",
        command=self.show_welcome_screen,
    )
    btn_back.pack(fill="x", padx=10, pady=15)

    tk.Label(
        left_panel,
        text="SCORE BOARD",
        font=("Verdana", 9, "bold"),
        fg="#9CA3AF",
        bg="#FFFFFF",
    ).pack(pady=(10, 5))

    self.lbl_score_side = tk.Label(
        left_panel,
        text="Player X: 0\n\nPlayer O: 0\n\nDraws: 0",
        font=("Verdana", 9, "bold"),
        fg="#374151",
        bg="#FFFFFF",
        justify="left",
    )
    self.lbl_score_side.pack(padx=10, pady=10)

    tk.Label(
        left_panel,
        text="MODE",
        font=("Verdana", 9, "bold"),
        fg="#9CA3AF",
        bg="#FFFFFF",
    ).pack(pady=(20, 2))
    self.mode_var = tk.StringVar(value="Computer")
    tk.Radiobutton(
        left_panel,
        text="vs CPU",
        variable=self.mode_var,
        value="Computer",
        bg="#FFFFFF",
        fg="#10B981",
        selectcolor="#FDF8F9",
        activebackground="#FFFFFF",
        font=("Verdana", 8),
    ).pack(anchor="w", padx=15)
    tk.Radiobutton(
        left_panel,
        text="2 Players",
        variable=self.mode_var,
        value="Two Players",
        bg="#FFFFFF",
        fg="#10B981",
        selectcolor="#FDF8F9",
        activebackground="#FFFFFF",
        font=("Verdana", 8),
    ).pack(anchor="w", padx=15)

    # --- RIGHT CONTENT AREA ---
    right_panel = tk.Frame(main_layout, bg="#FDF8F9")
    right_panel.pack(side="right", fill="both", expand=True)

    header_box = tk.Frame(
        right_panel,
        bg="#FFFFFF",
        highlightbackground="#F3E8EE",
        highlightthickness=2,
    )
    header_box.pack(fill="x", pady=(0, 8), ipady=8)

    tk.Label(
        header_box,
        text="TIC-TAC-TOE",
        font=("Verdana", 14, "bold"),
        fg="#D94680",
        bg="#FFFFFF",
    ).pack()

    self.lbl_status = tk.Label(
        header_box,
        text="GAME STATUS: READY",
        font=("Verdana", 9, "italic"),
        fg="#10B981",
        bg="#FFFFFF",
    )
    self.lbl_status.pack(pady=(2, 0))

    board_card = tk.Frame(
        right_panel,
        bg="#FFFFFF",
        highlightbackground="#F3E8EE",
        highlightthickness=2,
    )
    board_card.pack(pady=5)

    self.board_frame = tk.Frame(board_card, bg="#FFFFFF")
    self.board_frame.pack(padx=10, pady=10)

    self.buttons = []
    for i in range(9):
      btn = tk.Button(
          self.board_frame,
          text=" ",
          font=("Verdana", 22, "bold"),
          width=4,
          height=2,
          bg="#FFF0F3",
          fg="#374151",
          activebackground="#FFE3EC",
          activeforeground="#374151",
          relief="flat",
          command=lambda pos=i: self.on_button_click(pos),
          state="disabled",
      )
      btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
      self.buttons.append(btn)

    actions_frame = tk.Frame(right_panel, bg="#FDF8F9")
    actions_frame.pack(fill="x", pady=8)

    btn_new = tk.Button(
        actions_frame,
        text="NEW GAME",
        font=("Verdana", 9, "bold"),
        bg="#FFFFFF",
        fg="#D94680",
        activebackground="#FFF0F3",
        activeforeground="#D94680",
        relief="flat",
        cursor="hand2",
        command=self.start_new_game,
    )
    btn_new.pack(side="left", expand=True, fill="x", padx=(0, 4), ipady=4)

    btn_reset = tk.Button(
        actions_frame,
        text="RESET SCORE",
        font=("Verdana", 9, "bold"),
        bg="#FFFFFF",
        fg="#6B7280",
        activebackground="#FFF0F3",
        activeforeground="#6B7280",
        relief="flat",
        cursor="hand2",
        command=self.reset_score_board,
    )
    btn_reset.pack(side="right", expand=True, fill="x", padx=(4, 0), ipady=4)

    lbl_signature = tk.Label(
        right_panel,
        text="made with love by Aseel fox wydn",
        font=("Verdana", 7, "italic"),
        fg="#9CA3AF",
        bg="#FDF8F9",
    )
    lbl_signature.pack(side="bottom", pady=2)

  # ==========================================
  # GAME LOGIC METHODS
  # ==========================================
  def start_new_game(self):
    self.board = [" "] * 9
    self.game_mode = self.mode_var.get()
    self.game_active = True

    for btn in self.buttons:
      btn.config(
          text=" ", bg="#FFF0F3", fg="#374151", state="normal", relief="flat"
      )

    self.current_player = "X"
    self.lbl_status.config(text="GAME STATUS: X's TURN!")

    if self.game_mode == "Computer" and self.current_player == self.computer_symbol:
      self.root.after(400, self.computer_move)

  def reset_score_board(self):
    self.scores = {"X": 0, "O": 0, "Draws": 0}
    self.update_scores_display()

  def is_position_available(self, pos):
    return self.board[pos] == " "

  def check_win(self, symbol):
    win_patterns = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in win_patterns:
      if (
          self.board[a] == self.board[b] == self.board[c] == symbol
          and self.board[a] != " "
      ):
        return (a, b, c)
    return None

  def check_draw(self):
    return " " not in self.board

  def on_button_click(self, pos):
    if not self.game_active or not self.is_position_available(pos):
      return

    self.make_move(pos, self.current_player)

    if self.game_active and self.game_mode == "Computer" and self.current_player == self.computer_symbol:
      self.lbl_status.config(text="GAME STATUS: CPU THINKING...")
      self.root.after(350, self.computer_move)

  def make_move(self, pos, symbol):
    self.board[pos] = symbol
    color = "#D94680" if symbol == "X" else "#8A4FFF"
    self.buttons[pos].config(text=symbol, fg=color)

    win_combo = self.check_win(symbol)
    if win_combo:
      self.game_active = False
      for idx in win_combo:
        self.buttons[idx].config(bg="#A7F3D0", fg="#065F46")

      self.scores[symbol] += 1
      self.update_scores_display()

      msg = f"PLAYER {symbol} WINS! 🎉"
      self.lbl_status.config(text=f"GAME STATUS: {msg}")
      messagebox.showinfo("Game Over", msg)
      self.prompt_play_again()
      return

    if self.check_draw():
      self.game_active = False
      self.scores["Draws"] += 1
      self.update_scores_display()
      self.lbl_status.config(text="GAME STATUS: IT'S A DRAW!")
      messagebox.showinfo("Game Over", "It's a Draw! 🤝")
      self.prompt_play_again()
      return

    self.current_player = "O" if self.current_player == "X" else "X"
    self.lbl_status.config(
        text=f"GAME STATUS: {self.current_player}'s TURN!"
    )

  def computer_move(self):
    if not self.game_active:
      return

    available_moves = [
        i for i in range(9) if self.is_position_available(i)
    ]
    if not available_moves:
      return

    for move in available_moves:
      self.board[move] = self.computer_symbol
      if self.check_win(self.computer_symbol):
        self.board[move] = " "
        self.make_move(move, self.computer_symbol)
        return
      self.board[move] = " "

    user_symbol = "O" if self.computer_symbol == "X" else "X"
    for move in available_moves:
      self.board[move] = user_symbol
      if self.check_win(user_symbol):
        self.board[move] = " "
        self.make_move(move, self.computer_symbol)
        return
      self.board[move] = " "

    chosen_move = random.choice(available_moves)
    self.make_move(chosen_move, self.computer_symbol)

  def update_scores_display(self):
    self.lbl_score_side.config(
        text=(
            f"Player X: {self.scores.get('X', 0)}\n\nPlayer O:"
            f" {self.scores.get('O', 0)}\n\nDraws: {self.scores.get('Draws', 0)}"
        )
    )

  def prompt_play_again(self):
    if messagebox.askyesno("Play Again", "Do you want to start a new match?"):
      self.start_new_game()
    else:
      self.lbl_status.config(text="GAME STATUS: SESSION ENDED")


if __name__ == "__main__":
  root = tk.Tk()
  app = TicTacToeApp(root)
  root.mainloop()