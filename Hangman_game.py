import random


def shfaq_hangman(tentime):
    """Shfaq personin sipas tentimeve te mbetura"""
    faza = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,  # 0 tentime - personi i plote
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        """,  # 1 tentim
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        """,  # 2 tentime
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
        """,  # 3 tentime
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
        """,  # 4 tentime
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        """,  # 5 tentime
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        """,  # 6 tentime
        """
           --------
           |      
           |      
           |      
           |      
           |      
        """  # 7 tentime - bosh
    ]
    print(faza[tentime])


def merr_fjale():
    """Gjeneron nje fjale te rastesishme"""
    fjale = [
        "kompjuter", "python", "makine", "laptop", "dritare", "programim",
        "shkence", "teknologji", "universitet", "shok", "mobile", "internet",
        "tastiere", "monitor", "muzike", "libri", "shkolla", "klase"
    ]
    return random.choice(fjale)


def luaj():
    """Funksioni kryesor i lojes"""
    print("=" * 40)
    print("       LOJA HANGMAN       ")
    print("=" * 40)

    fjala = merr_fjale()
    fjala_e_fshedhur = ["_" for _ in fjala]
    tentime = 7
    shkronjat = set()

    while tentime > 0 and "_" in fjala_e_fshedhur:
        shfaq_hangman(tentime)
        print("\nFjala:", " ".join(fjala_e_fshedhur))
        print(f"Tentimet e mbetura: {tentime}")
        print(f"Shkronjat e perdorura: {', '.join(sorted(shkronjat)) if shkronjat else 'Asnje'}")
        print("-" * 40)

        shkronje = input("Shkruaj nje shkronje: ").lower()

        if len(shkronje) != 1 or not shkronje.isalpha():
            print("⚠️  Ju lutem shtypni vetem nje shkronje!")
            continue
        if shkronje in shkronjat:
            print("⚠️  Kjo shkronje eshte perdorur me pare.")
            continue

        shkronjat.add(shkronje)

        if shkronje in fjala:
            print("✓ Sakte!")
            for i, c in enumerate(fjala):
                if c == shkronje:
                    fjala_e_fshedhur[i] = shkronje
        else:
            tentime -= 1
            print("✗ Gabim! Humbisni nje tentim.")

    shfaq_hangman(tentime)
    print("\n" + "=" * 40)

    if "_" not in fjala_e_fshedhur:
        print("🎉 URIME! FITOVE!")
        print(f"Fjala ishte: {fjala.upper()}")
    else:
        print("💀 HUMBE!")
        print(f"Fjala ishte: {fjala.upper()}")
    print("=" * 40)


if __name__ == "__main__":
    luaj()

    # Pyetje per te luajtur perseri
    while input("\nDo te luash perseri? (po/jo): ").lower() == "po":
        print("\n" * 2)
        luaj()
