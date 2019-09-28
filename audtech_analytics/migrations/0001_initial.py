# Generated by Django 2.1 on 2019-03-01 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('post_code', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('web_address', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('phone_no', models.CharField(max_length=50, null=True, verbose_name='Contact Number')),
            ],
            options={
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('company_type', models.CharField(blank=True, max_length=60, null=True)),
                ('engagement_name', models.CharField(blank=True, max_length=90, null=True)),
                ('Currency', models.CharField(blank=True, max_length=50, null=True, verbose_name='Entity Currency')),
                ('peroid_frequency', models.CharField(blank=True, choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Half yearly', 'Half yearly'), ('Yearly', 'Yearly')], max_length=90, null=True)),
                ('financial_management_system', models.CharField(blank=True, max_length=90, null=True, verbose_name='System Name')),
                ('fiscal_start_month', models.DateField(blank=True, null=True, verbose_name='Fiscal Start Date')),
                ('fiscal_end_month', models.DateField(blank=True, null=True, verbose_name='Fiscal End Date')),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'permissions': (('create_eng ', 'Create Engagement'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FinalTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('engangement', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('Upload_Date', models.DateField(blank=True, null=True)),
                ('SrNo', models.CharField(blank=True, max_length=50, null=True)),
                ('JournalDate', models.DateTimeField(blank=True, null=True)),
                ('JournalNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('JournalType', models.CharField(blank=True, max_length=200, null=True)),
                ('DivisionCode', models.CharField(blank=True, max_length=200, null=True)),
                ('StatusPostedUnposted', models.CharField(blank=True, max_length=200, null=True)),
                ('PostingDate', models.DateTimeField(blank=True, null=True, verbose_name='Posting Date')),
                ('TransactionType', models.CharField(blank=True, max_length=200, null=True)),
                ('ReferenceNo', models.CharField(blank=True, max_length=200, null=True)),
                ('AccountCategory', models.CharField(blank=True, max_length=200, null=True)),
                ('MainAccountCode', models.CharField(blank=True, max_length=200, null=True)),
                ('MainAccountName', models.CharField(blank=True, max_length=200, null=True)),
                ('SubAccountCode', models.CharField(blank=True, max_length=200, null=True)),
                ('SubAccountName', models.CharField(blank=True, max_length=200, null=True)),
                ('Year', models.CharField(blank=True, max_length=200, null=True)),
                ('GroupName', models.CharField(blank=True, max_length=200, null=True)),
                ('ShortText', models.CharField(blank=True, max_length=200, null=True)),
                ('TaxReference', models.CharField(blank=True, max_length=200, null=True)),
                ('Splitbetweenheads', models.CharField(blank=True, max_length=200, null=True)),
                ('CreatedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('AuthorisedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('CurrencyCode', models.CharField(blank=True, max_length=200, null=True)),
                ('DebitAmount', models.FloatField(blank=True, null=True)),
                ('CreditAmount', models.FloatField(blank=True, null=True)),
                ('DebitAmountFC', models.FloatField(blank=True, null=True)),
                ('CreditAmountFC', models.FloatField(blank=True, null=True)),
                ('DocumentHeaderText', models.CharField(blank=True, max_length=200, null=True)),
                ('EntityCode', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'permissions': (('is_analytics', 'Analytics'), ('is_read', 'Only read'), ('is_import', 'Import Data')),
            },
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng', models.CharField(blank=True, max_length=50, null=True)),
                ('client', models.CharField(blank=True, max_length=200, null=True, verbose_name='Financial System')),
                ('transaction_type', models.CharField(blank=True, max_length=200, null=True)),
                ('final_field', models.CharField(blank=True, max_length=200, null=True, verbose_name='Audtech Field')),
                ('source_filed', models.CharField(blank=True, max_length=200, null=True, verbose_name='System Field')),
                ('column_no', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='OriginalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('engangement', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('upload_date', models.DateField(blank=True, null=True)),
                ('c1', models.CharField(blank=True, max_length=200, null=True)),
                ('c2', models.CharField(blank=True, max_length=200, null=True)),
                ('c3', models.CharField(blank=True, max_length=200, null=True)),
                ('c4', models.CharField(blank=True, max_length=200, null=True)),
                ('c5', models.CharField(blank=True, max_length=200, null=True)),
                ('c6', models.CharField(blank=True, max_length=200, null=True)),
                ('c7', models.CharField(blank=True, max_length=200, null=True)),
                ('c8', models.CharField(blank=True, max_length=200, null=True)),
                ('c9', models.CharField(blank=True, max_length=200, null=True)),
                ('c10', models.CharField(blank=True, max_length=200, null=True)),
                ('c11', models.CharField(blank=True, max_length=200, null=True)),
                ('c12', models.CharField(blank=True, max_length=200, null=True)),
                ('c13', models.CharField(blank=True, max_length=200, null=True)),
                ('c14', models.CharField(blank=True, max_length=200, null=True)),
                ('c15', models.CharField(blank=True, max_length=200, null=True)),
                ('c16', models.CharField(blank=True, max_length=200, null=True)),
                ('c17', models.CharField(blank=True, max_length=200, null=True)),
                ('c18', models.CharField(blank=True, max_length=200, null=True)),
                ('c19', models.CharField(blank=True, max_length=200, null=True)),
                ('c20', models.CharField(blank=True, max_length=200, null=True)),
                ('c21', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'managed': True,
                'default_permissions': (),
            },
        ),
    ]