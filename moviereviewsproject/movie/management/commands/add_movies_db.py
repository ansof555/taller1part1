from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movies.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construir la ruta completa hacia el archivo JSON
        json_file_path = os.path.join(
            'movie', 'management', 'commands', 'movies.json'
        )

        # Cargar los datos desde el archivo JSON
        with open(json_file_path, 'r', encoding='utf-8') as file:
            movies = json.load(file)

        # Insertar hasta 100 películas en la base de datos
        for i in range(100):
            movie = movies[i]

            # Verificar si la película ya existe en la base de datos
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movies/images/default.jpg',  # Imagen por defecto
                    genre=movie['genre'],
                    year=movie['year'],
                    description=movie['plot']
                )

