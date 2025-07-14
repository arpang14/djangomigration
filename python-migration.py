

from django.db import migrations


def insert_city(apps, schema_editor):
    city = apps.get_model('app-name', 'city')
    
    locations = [
               
                'pune',
                'Shanghai',
                'ABC',
                'Russia',
               ]

        
        for location in locations:
        city, is_created \
            = city.objects.get_or_create(title=str(location))



class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0001_migartionfiledepency'),
    ]

    operations = [
        migrations.RunPython(insert_city),
    ]
