from django.test import TestCase
from lists.models import Item, UserProfile
import datetime

class ModelTest(TestCase):

    def test_user_creation(self):
        user_one = UserProfile()
        user_one.userName = "user_one"
        user_one.firstName = "User"
        user_one.lastName = "One"
        user_one.dob = datetime.datetime.today()
        user_one.save()

        user_two = UserProfile()
        user_two.userName = "user_two"
        user_two.firstName = "User"
        user_two.lastName = "Two"
        user_two.dob = datetime.datetime.today()
        user_two.save()

        users = UserProfile.objects.all()

        self.assertEqual(users.count(), 2)
        self.assertEqual(users[0].userName, 'user_one')
        self.assertEqual(users[1].userName, 'user_two')

    def test_list_item_creation(self):
        user_one = UserProfile.objects.create(
                    userName='user_one',
                    firstName='User',
                    lastName='One',
                    dob=datetime.datetime.today()
        )
        user_two = UserProfile.objects.create(
                    userName='user_two',
                    firstName='User',
                    lastName='Two',
                    dob=datetime.datetime.today()
        )

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
