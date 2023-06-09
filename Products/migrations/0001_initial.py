# Generated by Django 3.2 on 2023-02-15 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, unique=True)),
                ('image', models.ImageField(default='category_default.png', upload_to='category_img/')),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_color',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_desgin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.PositiveBigIntegerField()),
                ('discount_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='product_img/')),
                ('size', models.PositiveIntegerField(choices=[(1, 'SMALL'), (2, 'MEDIUM'), (3, 'LARGE'), (4, 'XLARGE'), (5, 'XXLARGE')], default=2)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'tbl_product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product_color',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product_design',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_img/', verbose_name='product_image')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product_material',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_star', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_product_rating',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_star', models.FloatField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_product_review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_product_size',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('is_active', models.BooleanField(default=True)),
                ('percentage', models.PositiveBigIntegerField(verbose_name='percentage')),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_promo_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_size',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'tbl_user_cart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserCustomDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75, null=True)),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='customAmount')),
                ('product_image', models.TextField(blank=True, null=True)),
                ('front_desing', models.TextField(blank=True, null=True)),
                ('back_desing', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_user_custom_design',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserCustomProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_user_custom_product_order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
            ],
            options={
                'db_table': 'tbl_user_order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserOrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('has_paid', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=75, unique=True)),
                ('has_delivered', models.BooleanField(default=False, verbose_name='Delivery Status')),
            ],
            options={
                'db_table': 'tbl_user_order_history',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserPromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tbl_user_promo_code',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserWishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
            options={
                'db_table': 'tbl_user_wishlist',
                'managed': True,
            },
        ),
    ]
