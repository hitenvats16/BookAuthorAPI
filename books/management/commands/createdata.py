from random import randint
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from books.models import Book

fake = Faker()

import string
import random

class Command(BaseCommand):
    help = "This command will generate 100 random users and data"
    # genrating random data with faker

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def generate_random_password(self):
        ## length of password from the user
        length = 20

        ## shuffling the characters
        random.shuffle(self.characters)
        
        ## picking random characters from the list
        password = []
        for i in range(length):
            password.append(random.choice(self.characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        return "".join(password)

    def generateUsersAndBooks(self):
        # for user
        username = fake.user_name()
        email = fake.email()
        password = self.generate_random_password()
        display_name = fake.name()
        mobile = fake.msisdn()

        user = get_user_model().objects.create(username=username,password=make_password(password),email=email,display_name=display_name,mobile_phone=mobile)
        user.save()

        # for book
        nb = randint(1,3)
        title = fake.sentence(nb_words=nb)
        author = user

        book = Book.objects.create(author=author,title=title)
        book.save()
        user.no_of_books_published=1+user.no_of_books_published
        user.save()
        return username, password
        

    def handle(self, *args, **options):
        n=20
        file = open('UserWithPass.txt','w')
        for i in range(0,20):
            username , password = self.generateUsersAndBooks()
            file.write(str(username)+" "+str(password)+'\n')
            self.stdout.write(self.style.SUCCESS('Successfully created user'))