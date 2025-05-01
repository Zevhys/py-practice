"""
! Category: Easy
Todo: Create a program that prints a formatted shopping receipt using string escape characters. Your receipt should include: 1. Store name as a title with double quotes around it (using escape characters), 2. A horizontal line made of hyphens below the store name, 3. At least 3 products with their prices, each on a new line, 4. Each product must be indented with a tab character, 5. Total price at the bottom with an empty line before it, 6. End the receipt with a file path (for example, C:\receipts\today.txt).
"""

print(
    '"python grocery store"\n----------------------\n\tapples: $2.99\n\tbread: $3.50\n\tmilk: $4.25\n\ntotal: $10.74\nfile: C:\\receipts\\today.txt\n'
)

"""
! Category: Medium
Todo: Write a Python program that creates a multi-line string for a console-based menu system. The program must: 1. Create one string variable (using triple quotes or escape characters) that displays a formatted menu, 2. Include a title for the menu with both single and double quotes (using escape characters), 3. Display at least 4 menu options, each preceded by a number and on a new line, 4. Include special characters like ► or → before each menu option (use Unicode escape sequence \u25ba for ►), 5. Include one menu option that has a tabbed submenu with at least 2 items, 6. End with a prompt asking for the user's choice.
"""

menu = """'john\'s "python menu" system'
=============================
1. \u25ba new game
2. \u25ba load game
3. \u25ba options
\t\u25ba sound: on
\t\u25ba difficulty: hard
4. \u25ba quit

enter your choice (1-4): """

print(menu)
