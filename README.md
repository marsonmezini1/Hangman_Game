# Hangman (English) – Word Guessing Game (Python)

**Hangman** is a simple console-based Python game where the player guesses a hidden word one letter at a time, with up to **7 attempts** before the hangman is completed.

---

## Features

| Feature | Description |
| --- | --- |
| Random word selection | Picks a random word from an internal word list. |
| Hangman ASCII stages | Displays the hangman drawing based on remaining attempts. |
| Input validation | Accepts only a single alphabetical character and rejects invalid input. |
| Used letters tracking | Stores and shows previously used letters (sorted). |
| Replay mode | Asks if you want to play again (`yes/no` logic in the script). |

---

## How it works

1. The program selects a random word from a predefined list.
2. The word is displayed as underscores (`_`) and updates as you guess correct letters.
3. Each wrong letter reduces the remaining attempts by 1.
4. The game ends when you guess the word or run out of attempts.

---

## Tech stack

| Technology | Purpose |
| --- | --- |
| Python | Game logic + console input/output |
| `random` (stdlib) | Random word choice |

---

## Installation
1) Clone the repository

```bash
git clone https://github.com/marsonmezini1/Hangman_Game
