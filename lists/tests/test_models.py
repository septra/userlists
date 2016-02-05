from django.test import TestCase
from lists.models import Item, User

class ModelTest(TestCase):

    def test_user_creation(self):
        user_one = User()
        user_one.user_name = "user_one"
        user_one.name = "User One"
        user_one.save()

        user_two = User()
        user_two.user_name = "user_two"
        user_two.name = "User Two"
        user_two.save()

        users = User.objects.all()

        self.assertEqual(users.count(), 2)
        self.assertEqual(users[0].user_name, 'user_one')
        self.assertEqual(users[1].user_name, 'user_two')

    def test_list_item_creation(self):
        user_one = User.objects.create(user_name='user_one', name="User One")
        user_two = User.objects.create(user_name='user_two', name="User Two")

        item_one = Item.objects.create(
                        user=user_one,
                        text="The first item on User One's list"
        )
        item_two = Item.objects.create(
                        user=user_two,
                        text="The first item on User Two's list"
        )

        items = Item.objects.all()

        self.assertEqual(items[0], item_one)
        self.assertEqual(items[1], item_two)
        self.assertEqual(items[0].text, "The first item on User One's list")
        self.assertEqual(items[1].text, "The first item on User Two's list")
        self.assertEqual(items[0].user, user_one)
        self.assertEqual(items[1].user, user_two)
