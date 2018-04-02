# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 23:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0011_auto_20171109_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('Student_name', models.CharField(max_length=100)),
                ('Student_category', models.CharField(choices=[('MO', 'M.Tech. Students Ongoing'), ('MC', 'M.Tech. Students Completed'), ('PO', 'Ph.D. Students continuing'), ('PC', 'Ph.D. Students Completed')], default='select', max_length=2)),
                ('Thesis_title', models.CharField(max_length=3000)),
                ('Supervisors', models.CharField(max_length=3000)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='teaching',
            name='Partners',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='semester',
            field=models.CharField(choices=[('E', 'Even Semester'), ('O', 'Odd Semester')], default='select', max_length=1),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='year',
            field=models.IntegerField(choices=[(1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, verbose_name='year'),
        ),
    ]
