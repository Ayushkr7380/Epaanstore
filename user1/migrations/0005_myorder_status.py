# Generated by Django 5.0.2 on 2024-05-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user1", "0004_remove_flavourpaan_orders_remove_paanaroma_orders_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="myorder",
            name="status",
            field=models.CharField(default="Order Confirmed", max_length=200),
        ),
    ]
