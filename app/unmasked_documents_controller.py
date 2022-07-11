from bg_update.services import (DatabaseService, FileService)

from app.unmasked_documents_service import UnmaskedDocumentsService


class UnmaskedDocumentsController:
    def __init__(self):
        database_service = DatabaseService()
        file_service = FileService()

        self.__unmasked_documents = UnmaskedDocumentsService(file_service=file_service,
                                                             database_service=database_service)

    def update(self, first_p, second_p):
        self.__unmasked_documents.update(first_p, second_p)

    def upload_to_s3(self, path):
        self.__unmasked_documents.upload_to_s3(path)

    def download_from_s3(self, s3_path):
        self.__unmasked_documents.download_from_s3(s3_path)
