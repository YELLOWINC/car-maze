from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
# bore-stroke, parking sensors, compression ratio, topspeed, acc

MANUFACTURER = (
        ('Audi', 'Audi'),
        ('Maruti-Suzuki', 'Maruti-Suzuki'),
        ('Tata Motors', 'Tata Motors'),
        ('Hyundai', 'Hyundai'),
        ('Honda', 'Honda'),
        ('Volkswagen', 'Volkswagen'),
        ('Toyota', 'Toyota'),
        ('Mahindra', 'Mahindra'),
        ('Renault', 'Renault'),
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Porsche', 'Porsche'),
        ('Nissan', 'Nissan'),
        ('Datsun', 'Datsun'),
        ('Jaguar', 'Jaguar'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('BMW', 'BMW'),
        ('Land Rover', 'Land Rover'))

class Car(models.Model):
    # Choice variables
    petrol = 'Petrol'
    diesel = 'Diesel'

    hatchback = 'Hatchback'
    suv = 'SUV'
    sedan = 'Sedan'
    crossover = 'Crossover'
    muv = 'MUV'
    mini_suv = 'Mini SUV'

    rack_and_pinion = 'Rack and Pinion'

    # Choices
    FUEL_CHOICE = (
        (petrol, 'Petrol'),
        (diesel, 'Diesel'))

    DRIVE_TYPE = ()

    TYPE_CHOICE = (
        (hatchback, 'Hatchback'),
        (suv, 'SUV'),
        (sedan, 'Sedan'),
        (crossover, 'Crossover'),
        (muv, 'MUV'),
        (mini_suv, 'Mini SUV'))

    STEER_CHOICES = (
        (rack_and_pinion, 'Rack and Pinion'),
    )


    # Basic info
    manufacturer = models.CharField(blank=True, max_length=50, choices=MANUFACTURER)
    full_name = models.CharField(blank=True, max_length=100)
    keyword = models.CharField(blank=True, max_length=50)
    type = models.CharField(blank=True, max_length=50, choices=TYPE_CHOICE)
    price = models.IntegerField(blank=True)
    mileage = models.FloatField(blank=True, null=True)
    fuel = models.CharField(choices=FUEL_CHOICE, blank=True, max_length=50)
    slug = models.SlugField(null=True, blank=True)
    manufacturer_slug = models.SlugField(null=True, blank=True)
    front_view = models.URLField(max_length=300, null=True, blank=True)
    side_view = models.URLField(max_length=300, null=True, blank=True)
    rear_view = models.URLField(max_length=300, null=True, blank=True)
    interior1 = models.URLField(max_length=300, null=True, blank=True)
    interior2 = models.URLField(max_length=300, null=True, blank=True)

    # Performance
    top_speed = models.IntegerField(blank=True, null=True)
    acceleration = models.FloatField(blank=True, null=True)
    engine_displacement = models.IntegerField(blank=True, null=True)
    power = models.CharField(blank=True, max_length=50, null=True)
    torque = models.CharField(blank=True, max_length=50, null=True)
    engine_description = models.CharField(blank=True, max_length=80, null=True)
    turning_radius = models.FloatField(blank=True, null=True)
    cylinders = models.IntegerField(blank=True, null=True)
    drive_type = models.CharField(blank=True, max_length=5, choices=DRIVE_TYPE, null=True)
    turbocharger = models.NullBooleanField(blank=True, null=True)
    supercharger = models.NullBooleanField(blank=True, null=True)
    valves_per_cylinder = models.IntegerField(blank=True, null=True)
    compression_ratio = models.CharField(blank=True, max_length=10, null=True)
    fuel_supply = models.CharField(blank=True, max_length=8, null=True)
    gearbox = models.IntegerField(blank=True, null=True)
    steer_type = models.CharField(blank=True, max_length=20, choices=STEER_CHOICES, null=True)

    # Capacity
    seating_capacity = models.IntegerField(blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    ground_clearance = models.IntegerField(blank=True, null=True)
    wheel_base = models.IntegerField(blank=True, null=True)
    front_tread = models.IntegerField(blank=True, null=True)
    rear_tread = models.IntegerField(blank=True, null=True)
    kerb_weight = models.IntegerField(blank=True, null=True)
    gross_weight = models.IntegerField(blank=True, null=True)
    front_headroom = models.IntegerField(blank=True, null=True)
    front_legroom = models.IntegerField(blank=True, null=True)
    rear_headroom = models.IntegerField(blank=True, null=True)
    rear_legroom = models.IntegerField(blank=True, null=True)
    tank_capacity = models.IntegerField(blank=True, null=True)
    tyre_type = models.CharField(blank=True, null=True, max_length=50)
    wheel_size = models.IntegerField(blank=True, null=True)
    alloy_wheel_size = models.IntegerField(blank=True, null=True)

    # Comfort
    air_conditioner = models.NullBooleanField(blank=True, null=True)
    power_steering = models.NullBooleanField(blank=True, null=True)
    rear_ac_vents = models.NullBooleanField(blank=True, null=True)
    startstop_button = models.NullBooleanField(blank=True, null=True)
    remote_trunk_opener = models.NullBooleanField(blank=True, null=True)
    remote_fuel_lid_opener = models.NullBooleanField(blank=True, null=True)
    accessory_power_outlet = models.NullBooleanField(blank=True, null=True)
    transmission_type = models.CharField(blank=True, max_length=30)
    foldable_rear_seat = models.CharField(blank=True, null=True, max_length=40)
    nav_system = models.NullBooleanField(blank=True, null=True)
    adjustable_seats = models.NullBooleanField(blank=True, null=True)
    cassette_player = models.NullBooleanField(blank=True, null=True)
    cd_player = models.NullBooleanField(blank=True, null=True)
    cd_changer = models.NullBooleanField(blank=True, null=True)
    dvd_player = models.NullBooleanField(blank=True, null=True)
    radio = models.NullBooleanField(blank=True, null=True)
    audio_system_remote_control = models.NullBooleanField(blank=True, null=True)
    speakers_front = models.NullBooleanField(blank=True, null=True)
    speakers_rear = models.NullBooleanField(blank=True, null=True)
    integrated_2din_audio = models.NullBooleanField(blank=True, null=True)
    bluetooth = models.NullBooleanField(blank=True, null=True)
    usb_aux = models.NullBooleanField(blank=True, null=True)
    low_fuel_light_warning = models.NullBooleanField(blank=True, null=True)
    automatic_climate_control = models.NullBooleanField(blank=True, null=True)
    air_quality_control = models.NullBooleanField(blank=True, null=True)
    rear_reading_lamp = models.NullBooleanField(blank=True, null=True)
    rear_seat_headrest = models.NullBooleanField(blank=True, null=True)
    rear_seat_center_armrest = models.NullBooleanField(blank=True, null=True)
    heated_seats_front = models.NullBooleanField(blank=True, null=True)
    heated_seats_rear = models.NullBooleanField(blank=True, null=True)
    leather_seats = models.NullBooleanField(blank=True, null=True)
    fabric_upholstery = models.NullBooleanField(blank=True, null=True)
    voice_control = models.NullBooleanField(blank=True, null=True)
    cup_holders_front = models.NullBooleanField(blank=True, null=True)
    cup_holders_rear = models.NullBooleanField(blank=True, null=True)
    shock_absorbers_type = models.CharField(blank=True, max_length=30)
    trunk_light = models.NullBooleanField(blank=True, null=True)
    vanity_mirror = models.NullBooleanField(blank=True, null=True)
    glove_box_cooling = models.NullBooleanField(blank=True, null=True)
    bottle_holder = models.CharField(blank=True, max_length=30)
    seat_lumbar_support = models.NullBooleanField(blank=True, null=True)
    cruise_control = models.NullBooleanField(blank=True, null=True)
    multi_function_steering_wheel = models.NullBooleanField(blank=True, null=True)
    touch_screen = models.NullBooleanField(blank=True, null=True)
    front_suspension = models.CharField(blank=True, max_length=30)
    rear_suspension = models.CharField(blank=True, max_length=30)

    # Safety
    antilock_braking_system = models.NullBooleanField(blank=True, null=True)
    parking_sensors = models.NullBooleanField(blank=True, null=True)    
    central_locking = models.NullBooleanField(blank=True, null=True)
    driver_airbag = models.NullBooleanField(blank=True, null=True)
    passenger_airbag = models.NullBooleanField(blank=True, null=True)
    side_airbag_front = models.NullBooleanField(blank=True, null=True)
    side_airbag_rear = models.NullBooleanField(blank=True, null=True)
    rear_seatbelts = models.NullBooleanField(blank=True, null=True)
    smart_access_card_entry = models.NullBooleanField(blank=True, null=True)
    seat_belt_warning = models.NullBooleanField(blank=True, null=True)
    brake_assist = models.NullBooleanField(blank=True, null=True)
    door_ajar_warning = models.NullBooleanField(blank=True, null=True)
    crash_sensor = models.NullBooleanField(blank=True, null=True)
    anti_theft_alarm = models.NullBooleanField(blank=True, null=True)
    power_door_locks = models.NullBooleanField(blank=True, null=True)
    child_safety_locks = models.NullBooleanField(blank=True, null=True)
    side_impact_beams = models.NullBooleanField(blank=True, null=True)
    front_impact_beams = models.NullBooleanField(blank=True, null=True)
    day_and_night_rear_view_mirrors = models.NullBooleanField(blank=True, null=True)
    passenger_side_rear_view_mirror = models.NullBooleanField(blank=True, null=True)
    engine_immobilizer = models.NullBooleanField(blank=True, null=True)
    centrally_mounted_fuel_tank = models.NullBooleanField(blank=True, null=True)
    rear_camera = models.NullBooleanField(blank=True, null=True)
    traction_control = models.NullBooleanField(blank=True, null=True)
    automatic_headlamps = models.NullBooleanField(blank=True, null=True)
    follow_me_home_headlamps = models.NullBooleanField(blank=True, null=True)
    front_brake_type = models.CharField(blank=True, max_length=30, null=True)
    rear_brake_type = models.CharField(blank=True, max_length=30, null=True)
    drag_coefficient = models.NullBooleanField(blank=True, null=True)
    braking_time = models.NullBooleanField(blank=True, null=True)
    height_adjustable_front_seat_belts = models.NullBooleanField(blank=True, null=True)

    # Others
    bore_stroke = models.CharField(blank=True, max_length=30, null=True)
    synchronizers = models.NullBooleanField(blank=True, null=True)
    emission_norm_compliance = models.CharField(blank=True, max_length=30, null=True)
    emission_control_system = models.CharField(blank=True, max_length=30, null=True)
    country_of_assembly = models.CharField(blank=True, max_length=30, null=True)
    country_of_manufacture = models.CharField(blank=True, max_length=30, null=True)

    def __str__(self):
        return self.full_name

    # Auto create slugs on save
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.full_name)
            self.manufacturer_slug = slugify(self.manufacturer)


class UserProfile(models.Model):

    STATES = (
        ('Kerala', 'Kerala'),
    )

    DISTRICTS = (
        ('Ernakulam', 'Ernakulam'),
        ('Thriruvananthapuram', 'Thriruvananthapuram'),
        ('Kollam', 'Kollam'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Alappuzha', 'Alappuzha'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki'),
        ('Thissur', 'Thissur'),
        ('Palakkad', 'Palakkad'),
        ('Malappuram', 'Malappuram'),
        ('Kozhikode', 'Kozhikode'),
        ('Wayanad', 'Wayanad'),
        ('Kannur', 'Kannur'),
        ('Kasargod', 'Kasargod'),
    )

    CITIES = (
        ('Kochi', 'Kochi'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.OneToOneField(User)
    status = models.BooleanField(default=True)
    is_dealer = models.BooleanField(default=False)
    district = models.CharField(max_length=25, choices=DISTRICTS)
    DOB = models.CharField(blank=True, max_length=11, null=True)
    gender = models.CharField(max_length=10,choices=GENDER, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Dealer(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    manufacturer = models.CharField(blank=False, max_length=50, choices=MANUFACTURER)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    flag = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class TestDrive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    flag = models.BooleanField(default=False)
    scheduled = models.DateTimeField(blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
