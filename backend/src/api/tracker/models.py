from django.db import models

from django.contrib.auth import get_user_model


class Exercise(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)

    @property
    def get_entries(self):
        return Entries.objects.filter(exercise_id=self.id)

    def get_entries_by_user(self, user_id):
        return Entries.objects.filter(exercise_id=self.id, user_id=user_id)

    def __str__(self):
        return self.name


class Entries(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(blank=False)
    reps = models.IntegerField(blank=False)
    series = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.datetime)


class Protocol(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    exercises = models.ManyToManyField(Exercise, blank=True)

    @property
    def get_exercises_entries(self):
        return Entries.objects.filter(exercise__in=self.exercises.all())

    @classmethod
    def get_exercises_entries_by_user(cls, protocol, user_id, date_from, date_to):
        entries = Entries.objects.filter(
            exercise__in=protocol.exercises.all(),
            user_id=user_id,
            datetime__range=[date_from, date_to],
        )

        return entries

    def __str__(self):
        return self.name
