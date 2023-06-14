from django.db import models

class Job(models.Model):
    POSITION_CHOICES = (
        ('fulltime', 'Full-Time'),        
        ('parttime', 'Part-Time'),        
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),        
    )
    job_title = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, null=True)
    image = models.ImageField(upload_to='jobs/', null=True, blank=True)
    desc = models.TextField(null=True)
    apply_url = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.job_title
