from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields for your models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SampleItem(TimeStampedModel):
    """
    A foundational example model. Replace this class and fields
    with the actual data structure your application needs.
    """

    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sample Item"
        verbose_name_plural = "Sample Items"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
