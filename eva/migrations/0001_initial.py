# Generated by Django 3.0.3 on 2020-03-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordCount', models.IntegerField()),
                ('rowCount', models.IntegerField()),
                ('colCount', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('num', models.IntegerField()),
                ('url', models.CharField(help_text='This is the relativepath for the pic.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Radical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordId', models.IntegerField()),
                ('url', models.CharField(help_text='This is the relativepath for the pic.', max_length=100)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workName', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=10, null=True)),
                ('pageNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('x1', models.IntegerField(help_text='The x coordinate of upper-left point')),
                ('y2', models.IntegerField(help_text='The y coordinate of lower-right point')),
                ('x2', models.IntegerField(help_text='The x coordinate of lower-right point')),
                ('y1', models.IntegerField(help_text='The y coordinate of upper-left point')),
                ('coreX', models.IntegerField()),
                ('coreY', models.IntegerField()),
                ('num', models.IntegerField()),
                ('pageId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eva.Page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='wordId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eva.Work'),
        ),
    ]
