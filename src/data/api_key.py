import random as rd

API_KEY_1 = "jDRziy0rPDlXjCY9gvzEcV4BxfVCSQ4BavvnJ011"
API_KEY_2 = "7HJV6CGrabnCQWomhg45iZHzDuOHiI91RfkrhDNr"

def get_api_key():
    """
    This function returns a random API key from the list of API keys.
    """
    return rd.choice([API_KEY_1, API_KEY_2])
