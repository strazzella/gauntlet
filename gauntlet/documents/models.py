from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    last_accessed = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('Document', null=True, blank=True,on_delete=models.CASCADE)

    def get_full_path(self):
        path = [self]

        parent = self.parent
        while parent:
            path.append(parent)
            parent = parent.parent

        path.reverse()
        return path

    def __str__(self):
        return 'Document - %s: %s' % (self.id, self.title)
