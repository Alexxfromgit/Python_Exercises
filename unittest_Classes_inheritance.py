import unittest
from Classes_inheritance import *


class TestAnimals(unittest.TestCase):

    def test_some_animal_paw(self):
        self.assertEqual(some_animal.paw, 4)

    def test_some_animal_tail(self):
        self.assertEqual(some_animal.tail, 1)

    def test_some_animal_wool(self):
        self.assertTrue(some_animal.wool)

    def test_doggy_paw(self):
        self.assertEqual(doggy.paw, 4)

    def test_doggy_tail(self):
        self.assertEqual(doggy.tail, 1)

    def test_doggy_wool(self):
        self.assertTrue(doggy.wool)

    def test_doggy_say_something(self):
        self.assertEqual(Dog.say_something(), "Woof - woof")

    def test_kitty_paw(self):
        self.assertEqual(kitty.paw, 4)

    def test_kitty_tail(self):
        self.assertEqual(kitty.tail, 1)

    def test_kitty_wool(self):
        self.assertTrue(kitty.wool)

    def test_kitty_say_something(self):
        self.assertEqual(Cat.say_something(), "Meow - meow")

    def test_gib_paw(self):
        self.assertEqual(kitty.paw, 4)

    def test_gib_tail(self):
        self.assertEqual(kitty.tail, 1)

    def test_gib_wool(self):
        self.assertFalse(SphynxCat.wool)

    def test_gib_say_something(self):
        self.assertEqual(SphynxCat.say_something(), "Murr - murr")

    def test_petya_paw(self):
        self.assertEqual(petya.paw, 2)

    def test_petya_tail(self):
        self.assertEqual(petya.tail, 1)

    def test_petya_wool(self):
        self.assertFalse(Rooster.wool)

    def test_petya_say_something(self):
        self.assertEqual(Rooster.say_something(), "Cocorico")


if __name__ == '__main__':
    unittest.main()
