# Generated by Django 5.1.3 on 2024-11-17 06:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='usd', max_length=10)),
                ('stripe_payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('students', models.ManyToManyField(related_name='enrolled_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
