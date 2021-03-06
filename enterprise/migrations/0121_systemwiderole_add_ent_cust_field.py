# Generated by Django 2.2.17 on 2021-01-26 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0120_systemwiderole_applies_to_all_contexts'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemwideenterpriseuserroleassignment',
            name='enterprise_customer',
            field=models.ForeignKey(blank=True, help_text='The EnterpriseCustomer for which the role is assigned for the user.  If creating a new assignment, you must first provide a user email and role, then click "Save and continue editing" BEFORE selecting from this dropdown.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='system_wide_role_assignments', to='enterprise.EnterpriseCustomer'),
        ),
    ]
