# Generated by Django 3.2 on 2023-02-15 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpromocode',
            name='promocode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.promocode'),
        ),
        migrations.AddField(
            model_name='userpromocode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userorderhistory',
            name='tranastion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.transaction'),
        ),
        migrations.AddField(
            model_name='userorderhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userorder',
            name='order_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.userorderhistory'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='tranastion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.transaction'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercustomproductorder',
            name='order_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.userorderhistory'),
        ),
        migrations.AddField(
            model_name='usercustomproductorder',
            name='tranastion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.transaction'),
        ),
        migrations.AddField(
            model_name='usercustomproductorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercustomproductorder',
            name='user_design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.usercustomdesign'),
        ),
        migrations.AddField(
            model_name='usercustomdesign',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='usercart',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.size'),
        ),
        migrations.AddField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productsize',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.size'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.productrating'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productrating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_rating', to='Products.product'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.material'),
        ),
        migrations.AddField(
            model_name='productmaterial',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.design'),
        ),
        migrations.AddField(
            model_name='productdesign',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.color'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
    ]
