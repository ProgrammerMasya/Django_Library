from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Book


class AnimalTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            username='testuser1',
            first_name='TestName1',
            last_name='TestLast_name1',
            password='test1test1'
        )
        User.objects.create(
            username='testuser2',
            first_name='TestName2',
            last_name='TestLast_name2',
            password='test2test2'
        )
        user1 = User.objects.get(username='testuser1')
        user2 = User.objects.get(username='testuser2')
        Book.objects.create(
            name="Harry Potter",
            author="J. K. Rowling",
            user=user1,
        )
        Book.objects.create(
            name="Learning Python",
            author="Mark Lutz",
            user=user2,
        )

    def test_name_label(self):
        book = Book.objects.get(name="Harry Potter")
        field_label = book._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        book = Book.objects.get(name="Learning Python")
        max_length = book._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_get_user_book(self):
        user = User.objects.get(username='testuser1')
        book = Book.objects.get(user=user)
        self.assertEquals(book.name, 'Harry Potter')

    def test_book_absolute_url(self):
        book1 = Book.objects.get(id=1)
        book2 = Book.objects.get(id=2)
        self.assertEqual(book1.get_absolute_url(), '/1/edit/')
        self.assertEqual(book2.get_absolute_url(), '/2/edit/')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


