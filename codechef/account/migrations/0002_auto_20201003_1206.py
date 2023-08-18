# Generated by Django 2.2.16 on 2020-10-03 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tseries', '0001_initial'),
        ('scholarship', '0001_initial'),
        ('course', '0001_initial'),
        ('account', '0001_initial'),
        ('mains_test_series', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_series_enrolment',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tseries.Series'),
        ),
        migrations.AddField(
            model_name='test_series_enrolment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scholarship_test_enrolment',
            name='scholarship_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholarship.Scholarship_Test'),
        ),
        migrations.AddField(
            model_name='scholarship_test_enrolment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mains_test_series_enrolment',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains_test_series.Mains_Test_Series'),
        ),
        migrations.AddField(
            model_name='mains_test_series_enrolment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course_enrolment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='course_enrolment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='test_series',
            field=models.ManyToManyField(through='account.Test_Series_Enrolment', to='tseries.Series'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]