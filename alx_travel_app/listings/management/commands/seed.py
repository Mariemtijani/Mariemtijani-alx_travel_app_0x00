from django.core.management.base import BaseCommand
from listings.models import Listing, Booking
from faker import Faker
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()

        self.stdout.write('Old data cleared.')

        # Create sample listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                price=round(random.uniform(50, 500), 2),
                available=random.choice([True, False])
            )

            # Add 0–3 bookings for each listing
            for _ in range(random.randint(0, 3)):
                Booking.objects.create(
                    listing=listing,
                    customer_name=fake.name(),
                    booking_date=fake.date_between(start_date='-30d', end_date='+30d'),
                    created_at=fake.date_time_this_year()
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
