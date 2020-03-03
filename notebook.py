import datetime

last_id = 0


class Note:
    def __init__(self, memo, tags=""):
        """
        Initialize the instance of note
        :param memo: str
        :param tags: str
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Filter the information based on the given argument
        :param filter: str
        :return: bool
        """
        return filter in self.memo or filter in self.tags

    def __str__(self):
        """
        Return function represented in string
        :return: str
        """
        return "ID: {}\nTAGS: {}\nDATA: {}\nMEMO: {}".format(
            str(self.id), self.tags, self.creation_date, self.memo
        )


class Notebook:
    def __init__(self):
        """
        Initialize the instance of notebook
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value"""

        note = self.find_note(note_id)
        if note:
            note.memo = memo

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value"""

        note = self.find_note(note_id)
        if note:
            note.tags = tags

    def search(self, filter):
        """Find all notes that match the given filter string"""
        return [note for note in self.notes if note.match(filter)]

    def find_note(self, note_id):
        """Locate the note with the given id"""

        for note in self.notes:
            if note.id == note_id:
                return note
        return None


