# Generated by Django 4.2 on 2023-04-24 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('destinateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_recus', to=settings.AUTH_USER_MODEL)),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_envoyes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]