from django.db import models

GENDER_CHOICES = [
    ('F', 'Female'),
    ('M', 'Male'),
    ('T', 'Transgender')
]
QUOTE_STATES = [
    ('new', 'New'),
    ('quoted', 'Quoted'),
    ('bound', 'Bound'),
]
POLICY_TYPES = [
    ('PA', 'Personal Accident'),
    ('LI', 'Life Insurance'),
]


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField('Date of Birth', max_length=8)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.email)


class Policy(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    premium = models.IntegerField()
    cover = models.IntegerField()
    state = models.CharField(max_length=10, choices=QUOTE_STATES, default='new')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='policies')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "policies"

    def __str__(self):
        return '{} {} {} {}'.format(self.pk, self.name, self.type, self.state)



