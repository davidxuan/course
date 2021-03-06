# Generated by Django 2.0.7 on 2018-07-24 01:22

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duration', models.TimeField()),
                ('level', models.CharField(max_length=20)),
                ('audience', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sideLink', models.CharField(max_length=50)),
                ('codeLink', models.CharField(max_length=50)),
                ('textExplanation', models.TextField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duration', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('discourse', models.URLField(blank=True, null=True)),
                ('about', models.TextField()),
                ('profilepic', models.FileField(blank=True, null=True, upload_to='profile_pic')),
                ('github', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_author', to='mainapp.UserProfile'),
        ),
        migrations.AddField(
            model_name='section',
            name='courseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Course'),
        ),
        migrations.AddField(
            model_name='courseitem',
            name='section',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_author', to='mainapp.UserProfile'),
        ),
    ]
