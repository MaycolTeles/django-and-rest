""""""
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from django.db import models


LEXERS = [lexer for lexer in get_all_lexers() if lexer[1]]
LANGUAGE_CHOICES = sorted([(language_choice[1][0], language_choice[0]) for language_choice in LEXERS])
STYLE_CHOICES = sorted([(style, style) for style in get_all_styles()])


class Snippet(models.Model):
    """
    Class to represent a Snippet of code in django model.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        """
        Meta Class to define some attributes for the Snippet Class.
        """
        ordering = ['created']
