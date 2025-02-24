# Generated by Django 5.1.6 on 2025-02-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_cart_category_menuitem_order_orderitem_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("guest_number", models.SmallIntegerField(default=1)),
                ("date", models.DateField(null=True)),
                ("comment", models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="category",
        ),
        migrations.RemoveField(
            model_name="order",
            name="delivery_crew",
        ),
        migrations.RemoveField(
            model_name="order",
            name="user",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="order",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="menuitem",
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderItem",
        ),
    ]
