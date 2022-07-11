import csv
import datetime
import os
import re
from datetime import datetime

from bg_update.db.connection import database
from bg_update.utils import warning

from app import settings
from app.models import unmasked_documents_table_name, unmasked_sources_table_name


class UnmaskedDocumentsService:
    def __init__(self, file_service, database_service):
        self.__database_service = database_service
        self.__file_service = file_service

        if not os.path.exists('./app/data'):
            os.mkdir('./app/data')

    def update(self, first_p, second_p):
        warning('Duplicating tables...')
        self.__database_service.duplicate_table(unmasked_sources_table_name)
        self.__database_service.duplicate_table(unmasked_documents_table_name)

        source = database.execute_sql(
            f"SELECT id FROM public.{unmasked_sources_table_name} WHERE source = '{first_p}';")
        source_id = source.fetchone()
        if not source_id:
            insert = f"INSERT INTO {unmasked_sources_table_name} (source) VALUES ('{first_p}') RETURNING id;"
            result = database.execute_sql(insert)
            source_id = result.fetchone()[0]
        else:
            source_id = source_id[0]

        f = open(second_p, 'r')
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lines = list(reader)
        f.close()

        count = 0

        for line in lines:
            # document validator
            document = line[1]
            if re.match(r"[^\d]", document):
                continue

            # normalize document mask
            masked_document = line[2]
            if not masked_document:
                if len(document) == 14:
                    temp_masked = document[3:-2]
                    masked_document = f"**.*{temp_masked[:2]}.{temp_masked[2:5]}/{temp_masked[5:]}-**"
                elif len(document) == 11:
                    masked_document = f"***.{document[3:6]}.{document[6:9]}-**"
            else:
                masked_document = masked_document[:-2]+"-**"

            # name processing and cleaning
            nome = line[0].replace("'", "''")
            nome = re.sub(r"[%]", '', nome)

            values = f"'{nome}', '{document}', '{masked_document}', {source_id}"

            upsert = f"""
                INSERT INTO {unmasked_documents_table_name} as temp
                    (nome, document, masked_document, source_id)
                VALUES ({values})
                ON CONFLICT (document, source_id)
                DO UPDATE SET nome = '{nome}'
                WHERE
                     temp.document = '{document}' AND
                     temp.source_id = {source_id};"""
            try:
                database.execute_sql(upsert)
            except Exception as error:
                print(upsert)
                raise error
            count += 1
            print(f"\rInserted {count} of {len(lines)}", end='')

    def upload_to_s3(self, path):
        filename = path.split(os.sep)[-1]
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        s3_file = f"{settings.S3_PREFIX}{timestamp}-{filename}"
        self.__file_service.upload_file_to_s3(path, s3_file)
        warning(f"Uploaded file {path} to S3 named {s3_file}")

    def download_from_s3(self, s3_path):
        local = f"./app/data/{s3_path.split('/')[-1]}"
        self.__file_service.download_file_from_s3(s3_path, local)
        warning(f"Downloaded file in {local}")
