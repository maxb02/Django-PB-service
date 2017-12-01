import requests

def snvalidator(sn):
    url = 'https://1093.72.149.183/bl.php'
    try:
        key = requests.get(url, params={'sn': sn}, verify=False).text
    except:
        return 'Erorr'
    if key == ' No such key':
        return False
    else:
        return True