import os
import sys
from bg_update.utils import warning

from bg_update.conf import ENVIRONMENT_VARIABLE

from app import settings

sys.dont_write_bytecode = True

if __name__ == "__main__":
    params = sys.argv
    os.environ.setdefault(ENVIRONMENT_VARIABLE, "app.settings")
    from app.unmasked_documents_controller import UnmaskedDocumentsController
    unmasked_documents_controller = UnmaskedDocumentsController()
    if len(params) < 3:
        warning(settings.USAGE_MESSAGE)
    elif len(params) == 3:
        first_p = params[1]
        second_p = params[2]
        if first_p == 'upload':
            unmasked_documents_controller.upload_to_s3(second_p)
        elif first_p == 'download':
            unmasked_documents_controller.download_from_s3(second_p)
        else:
            print(first_p, second_p)
            if not os.path.exists(second_p):
                warning(f"cannot find file {second_p}")
            else:
                unmasked_documents_controller.update(first_p, second_p)
