def print_keyboard_instructions():
    print("To type \"m²\" (m2) on a keyboard, you typically use special characters or symbols. Here's how you can do it on different platforms:\n")

    while True:
        # Ask for the operating system
        print("Select your operating system:")
        print("1. Windows")
        print("2. macOS")
        print("3. Linux")
        choice = input("Enter your choice (1/2/3): ")

        # Print instructions based on the user's choice
        if choice == "1":
            # Instructions for Windows
            print("Windows:")
            print("Using Alt Code (Numeric Keypad):")
            print("- Press and hold the Alt key.")
            print("- While holding the Alt key, type 0178 on the numeric keypad.")
            print("- Release the Alt key. This should display \"²\".\n")

            print("Using Character Map:")
            print("- Open the Character Map utility by searching for it in the Start menu.")
            print("- Find the \"²\" character and click on it to select it.")
            print("- Click the \"Copy\" button.")
            print("- Paste the copied character where you want it.\n")
            break

        elif choice == "2":
            # Instructions for macOS
            print("macOS:")
            print("Using Keyboard Shortcut:")
            print("- Press Option + Shift + 2 simultaneously. This will produce the \"²\" character.\n")

            print("Using Character Viewer:")
            print("- Open any text field where you can type.")
            print("- Press Control + Command + Space to open the Character Viewer.")
            print("- Search for \"superscript\" or \"superscript 2\".")
            print("- Double-click the \"²\" character to insert it into your text.\n")
            break

        elif choice == "3":
            # Instructions for Linux
            print("Linux:")
            print("Using Compose Key:")
            print("- If configured, you can use the Compose key followed by ^2 to produce \"²\".\n")

            print("Using Character Map:")
            print("- Open the Character Map utility and find the \"²\" character.")
            print("- Click on the character to copy it, then paste it where you want.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

            