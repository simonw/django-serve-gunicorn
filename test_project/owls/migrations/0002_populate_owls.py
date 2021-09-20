from django.db import migrations

DEFAULT_OWLS = (
    ("Greater sooty owl", "Tyto tenebricosa", 1),
    ("Lesser sooty owl", "Tyto multipunctata", 2),
    ("Minahassa masked owl", "Tyto inexspectata", 3),
    ("Taliabu masked owl", "Tyto nigrobrunnea", 4),
    ("Moluccan masked owl", "Tyto sororcula", 5),
)


def populate_owls(apps, schema_editor):
    Owl = apps.get_model("owls", "Owl")
    for common_name, binomial_name, ioc_sequence in DEFAULT_OWLS:
        Owl.objects.get_or_create(
            ioc_sequence=ioc_sequence,
            defaults={
                "common_name": common_name,
                "binomial_name": binomial_name,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ("owls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_owls),
    ]
