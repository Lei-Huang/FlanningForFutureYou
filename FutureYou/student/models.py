from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    residentStatus = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    graduation_year = models.CharField(max_length=30)
    owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = self.linenos and 'table' or False
    options = self.title and {'title': self.title} or {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Student, self).save(*args, **kwargs)

