import Algorithmia
from Algorithmia.acl import ReadAcl, AclType

import settings


if __name__ == '__main__':

    apiKey = settings.API_KEY
    client = Algorithmia.client(apiKey)

    nlp_directory = client.dir(settings.CLIENT_DIR)
    if nlp_directory.exists() is False:
        nlp_directory.create()

    acl = nlp_directory.get_permissions()
    acl.read_acl == AclType.my_algos
