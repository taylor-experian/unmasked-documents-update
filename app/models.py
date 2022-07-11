from bg_update.db import models
from bg_update.db.connection import database
from bg_update.db.models import Task
from peewee import SQL


class UnmaskedSources(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=254, null=False, )

    class Meta:
        table_name = 'unmasked_sources_m'
        constraints = [SQL('UNIQUE (source)')]
        database = database


class UnmaskedDocuments(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254, null=True)
    document = models.CharField(max_length=20, null=True)
    masked_document = models.CharField(max_length=20, null=True)
    source_id = models.ForeignKeyField(UnmaskedSources)

    class Meta:
        table_name = 'unmasked_documents_m'
        constraints = [SQL('UNIQUE (document, source_id)')]
        database = database


unmasked_sources_table_name = UnmaskedSources._meta.table_name
unmasked_documents_table_name = UnmaskedDocuments._meta.table_name

with database.connection_context():
    database.create_tables([Task, UnmaskedSources])
    database.create_tables([Task, UnmaskedDocuments])
