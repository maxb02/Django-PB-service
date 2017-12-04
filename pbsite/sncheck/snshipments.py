import requests
import datetime

def sn_shipments(sn):
    if sn:
        url = 'http://gw.greendata.com.ua:8008/api/get-device-info'
        try:
            info = requests.get(url,params={'sn': sn}, verify=False).json()
        except:
            return 'Erorr'
        if info:
            for element in info:
                element['shippingDate'] = datetime.datetime.strptime(element['shippingDate'], "%Y-%m-%d %H:%M:%S")
            return info
        else:
            return False