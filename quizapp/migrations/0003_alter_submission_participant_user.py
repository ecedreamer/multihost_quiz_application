# Generated by Django 4.0.4 on 2022-05-18 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
        ('quizapp', '0002_quizsession_allow_multiple_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='participant_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authapp.participantuser'),
        ),
    ]