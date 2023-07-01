from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortinghatapi', '0001_initial'),  # Previous migration file for sortinghatapi app
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(to='sortinghatapi.User', default=1, on_delete=models.CASCADE, related_name='user')),
                ('house', models.ForeignKey(to='sortinghatapi.House', default=1, on_delete=models.CASCADE, related_name='house')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=300)),
            ],
        ),
    ]
