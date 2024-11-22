import unittest
from src.animals import Animal

class TestAnimal(unittest.TestCase):
    def test_add_command(self):
        animal = Animal("Dog")
        self.assertEqual(animal.add_command("Sit"), "Command 'Sit' added.")
        self.assertEqual(animal.add_command("Sit"), "Command 'Sit' already exists.")

    def test_list_commands(self):
        animal = Animal("Cat", ["Jump"])
        self.assertEqual(animal.list_commands(), "Jump")
        animal.add_command("Climb")
        self.assertEqual(animal.list_commands(), "Jump, Climb")

if __name__ == "__main__":
    unittest.main()
