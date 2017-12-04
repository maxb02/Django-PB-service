import requests

def sn_shipments(sn):
    if sn:
        url = 'http://gw.greendata.com.ua:8008/api/get-device-info'
        try:
            info = requests.get(url,params={'sn': sn}, verify=False).json()
        except:
            return 'Erorr'
        if info:
            return info
        else:
            return False