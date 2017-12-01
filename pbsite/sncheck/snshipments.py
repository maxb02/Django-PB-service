import requests

def sn_shipments(sn):
    url = 'http://shipments.pbi.office/api/get-device-info?sn={}'.format(sn)
    try:
        info = requests.get(url,params={'sn': sn}, verify=False).json()
    except:
        return 'Erorr'
    return  info