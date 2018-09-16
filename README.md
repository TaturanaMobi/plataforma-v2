# Criando o admin user

Para criar usuários admin que possam acessar o admin-v2 execute:

```bash
docker-compose run backend_web python manage.py createsuperuser
```

# Carregando lista inicial de e-mails

Os e-mails padrão estão em uma fixture, que vc carrega da seguinte forma:

```bash
docker-compose run backend_web python manage.py loaddata messagery/fixtures/initial_data.json
```

# Sincronizando todos os filmes

Para sincronziar todos os filmes inicialmente é preciso rodar um código python.
Execute:

```bash
docker-compose run backend_web python manage.py shell_plus
```

e cole o seguinte código no shell do python

```
from mongo_sync.tasks import sync_task
[sync_task.delay('film', f._id) for f in MongoFilm.objects.all()]
```

