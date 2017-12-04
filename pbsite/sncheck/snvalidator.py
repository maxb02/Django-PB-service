import requests

def snvalidator(sn):
    if sn:
        url = 'https://109.72.149.183/bl.php'
        try:
            key = requests.get(url, params={'sn': sn}, verify=False).text
        except:
            return 'Erorr'
        if key == ' No such key':
            return False
        else:
            return True