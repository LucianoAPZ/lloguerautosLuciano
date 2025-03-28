from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva

class Command(BaseCommand):
    help = 'Crear 4 automóviles, 8 usuarios y sus reservas'

    def handle(self, *args, **kwargs):
        faker = Faker()

        automoviles = []
        for _ in range(4):
            auto = Automobil.objects.create(
                marca=faker.company(),
                model=faker.word(),
                matricula=faker.unique.bothify(text="???###")
            )
            automoviles.append(auto)

        usuarios = []
        for _ in range(8):
            user = User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password="password123"
            )
            usuarios.append(user)

        for usuario in usuarios:
            num_reservas = random.randint(1, 2)
            for _ in range(num_reservas):
                auto = random.choice(automoviles)
                fecha_inicio = faker.date_between(start_date="today", end_date="+30d")
                fecha_fin = fecha_inicio + timedelta(days=random.randint(1, 7))

                if not Reserva.objects.filter(automobil=auto, fecha_inicio=fecha_inicio).exists():
                    Reserva.objects.create(
                        automobil=auto,
                        usuario=usuario,
                        fecha_inicio=fecha_inicio,
                        fecha_fin=fecha_fin
                    )

