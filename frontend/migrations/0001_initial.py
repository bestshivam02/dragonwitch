# Generated by Django 3.2 on 2023-02-15 18:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='countdown_banner/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('redirect_link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_category_banner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('image', models.ImageField(blank=True, null=True, upload_to='our_contact_info_img/')),
                ('mobile_no', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator('^^(\\+\\d{1,3})?,?\\s?\\d{8,13}', 'Only numbers are allowed.')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tbl_our_contact_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CustomeShirtBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='countdown_banner/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('redirect_link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_custom_shirt_banner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HomeFaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=300, null=True)),
                ('answer', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'tbl_home_faq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MainCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_carousel/')),
                ('description', models.CharField(blank=True, max_length=650, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('redirect_link', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'tbl_main_carousel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SaleBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sale_banner/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('discounts', models.CharField(blank=True, max_length=250, null=True)),
                ('redirect_link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_sale_banner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('review', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials_img/')),
                ('rating_star', models.FloatField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='update', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_testimonials',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CountdownBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='countdown_banner/')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('sale_end_date', models.DateTimeField(blank=True, null=True)),
                ('redirect_link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
            options={
                'db_table': 'tbl_countdown_banner',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('subject', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_contact_us', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_contact_us',
                'managed': True,
            },
        ),
    ]
