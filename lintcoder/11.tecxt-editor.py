class CustomStack:
    def __init__(self):
        self.text = ""
        self.history = []  # Stack to keep track of operations for undo


    def insert(self,text):
        self.text += text
        self.history.append(("insert",text))


    def delete(self, value):
        value = int(value)
        deleted_text = self.text[-value:]
        self.history.append(("delete", deleted_text))
        self.text = self.text[:-value]

    def get(self, value):
        value = int(value) - 1  # Convert to zero-based index
        if 0 <= value < len(self.text):
            print(self.text[value])
        else:
            print("Invalid index")
    def undo(self):
        if not self.history:
            return  # Nothing to undo
        last_command, value = self.history.pop()
        if last_command == "insert":
            self.text = self.text[:-len(value)]
        elif last_command == "delete":
            self.text += value

def process_commands(commands):
    editor = CustomStack()
    for command in commands.split(","):
        parts = command.strip().split(" ", 1)
        cmd = parts[0]
        if cmd == "1":  # Insert
            editor.insert(parts[1])
        elif cmd == "2":  # Delete
            editor.delete(parts[1])
        elif cmd == "3":  # Get
            editor.get(parts[1])
        elif cmd == "4":  # Undo
            editor.undo()


# Test the CustomStack class

process_commands("1 abc,3 3,2 3,4,3 1,4,3 2,4")  # Output: a

process_commands("1 abc,1 def,3 4,2 3,4,3 2,4,4,4")  # Output: a
