import notebook

to_continue = True


class Menu:
    """Display a menu and respond to choices when run"""
    def __init__(self):
        self.notebook = notebook.Notebook()

    def display_menu(self):

        print("""NOTEBOOK MENU:
               1. Show all Notes
               2. Search Notes
               3. Add Note
               4. Modify Note
               5. Quit""")

    def main(self):
        """
        Display the menu and respond to user's choices
        """
        self.display_menu()
        choice = input("Choose number of your next step: ")
        step = {"1": self.show,
                "2": self.search,
                "3": self.add,
                "4": self.modify,
                "5": self.quit
                }
        if choice in step:
            step[choice]()
        else:
            print("-------------------------------------------------")
            print("Ooops...something went wrong! Please try again :)")
            print("-------------------------------------------------")

        global to_continue
        if to_continue:
            self.main()

    def show(self):
        """
        Show to the user all notes which were created
        """
        if not self.notebook.notes:
            print('--------------------------')
            print('This notebook is empty now')
            print('--------------------------')
        for note in self.notebook.notes:
            print(str(note))
            print(" ")

    def search(self):
        """
        Search particular note made by user
        """
        filter = input('Search for: ')
        notes = self.notebook.search(filter)
        if not notes:
            print('--------------------------')
            print('This notebook is empty now')
            print('--------------------------')
        for note in notes:
            print(note)

    def add(self):
        """
        Create a new note
        """
        memo = input('MEMO: ')
        tags = input('TAGS: ')
        self.notebook.new_note(memo, tags)

    def modify(self):
        """
        Modify the user's note
        """
        try:
            id = input('Enter tne id number of the element you want to change: ')
            if int(id) >= len(self.notebook.notes):
                print("You should enter valid ID!")
                return
            memo = input('MEMO: ')
            tags = input('TAGS: ')
            if memo:
                self.notebook.modify_memo(int(id), memo)
            if tags:
                self.notebook.modify_tags(int(id), tags)
        except:
            print("You should enter integer!")

    def quit(self):
        """
        Stop running the program
        """
        global to_continue
        to_continue = False
        print("Bye :)")


menu = Menu()
menu.main()

