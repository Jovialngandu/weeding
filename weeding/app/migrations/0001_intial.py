# migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        
        migrations.CreateModel(
            name='AptitudePhysique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.BooleanField()),
                ('audition', models.BooleanField()),
                ('mobilite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('dateNaissance', models.DateField()),
                ('lieuNaissance', models.CharField(max_length=100)),
                ('aptitudePhysique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.AptitudePhysique')),
                ('nationalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Nation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Officier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Bourgoumestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDemande', models.DateField()),
                ('etatDemande', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personne1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personne1', to='app.Personne')),
                ('personne2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personne2', to='app.Personne')),
            ],
        ),
        migrations.CreateModel(
            name='Mariage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCelebration', models.DateField()),
                ('lieuCelebration', models.CharField(max_length=100)),
                ('bourgoumestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Bourgoumestre')),
                ('couple', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Couple')),
                ('officier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Officier')),
            ],
        ),
    ]