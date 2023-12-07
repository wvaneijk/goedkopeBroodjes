from xata.client import XataClient

client = XataClient(api_key="xau_YLGR4E6bzbx0RRr0o8v8eo97tHpR8MvG1", db_url="https://m-lalmohamed-s-workspace-t5jh8f.eu-central-1.xata.sh/db/pepper-en-zuur")

def get_db_client():
    return client