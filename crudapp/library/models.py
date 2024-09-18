from django.db import models
from django.core.exceptions import ValidationError


def validate_0_to_10(value):
    if value < 0 or value > 10:
        raise ValidationError(
            'Value must be between 0 and 10.',
            code='invalid_range'
        )


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    year_published = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=2000)
    rating = models.IntegerField(validators=[validate_0_to_10])

