class Animal:
    def __init__(self, name, commands=None, birth_date=None):
        self.name = name
        self.commands = commands or []
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.name}: Commands={self.commands}, Birth Date={self.birth_date}"

    def add_command(self, command):
        if command not in self.commands:
            self.commands.append(command)
            return f"Command '{command}' added."
        return f"Command '{command}' already exists."

    def list_commands(self):
        return ", ".join(self.commands) if self.commands else "No commands assigned."
