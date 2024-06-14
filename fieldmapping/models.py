from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone


# Create your models here.
class Location(models.Model):
    LABEL_CHOICES = [
        ('farms', 'Farm'),
        ('processing-facilities', 'Processing Facility'),
        ('distribution-centers', 'Distribution Center'),
        ('warehouses', 'Warehouse'),
        ('restaurants', 'Restaurant'),
        ('supermarkets', 'Supermarket')
    ]
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, choices=LABEL_CHOICES)
    location = gis_models.PointField(srid=4326)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Locations'


class Farmer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length = 20)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Farmers'


class Produce(models.Model):
    produce_type= models.CharField(max_length=100)
    variety = models.CharField(max_length=225, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.variety:
            return f'{self.produce_type} variety: {self.variety}'
        else:
            return f'{self.produce_type}'

    class Meta:
        verbose_name_plural = 'Crops'

        
class Farm(models.Model):
    REGION_CHOICES = [
        ('central', 'Central'),
        ('coast', 'Coast'),
        ('eastern', 'Eastern'),
        ('nairobi', 'Nairobi'),
        ('north_eastern', 'North Eastern'),
        ('nyanza', 'Nyanza'),
        ('rift_valley', 'Rift Valley'),
        ('western', 'Western')
    ]
    name = models.CharField(max_length=100)
    farm_area =gis_models.PolygonField(srid=4326)
    description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='farms')
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farms')
    produce = models.ManyToManyField(Produce, related_name='farms')
    
    
    @property
    def calculate_area(self):
        transformed_polygon = self.farm_area.transform(3857, clone=True)
        return f'{transformed_polygon.area:.2f} square meters'
    

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Farms'



