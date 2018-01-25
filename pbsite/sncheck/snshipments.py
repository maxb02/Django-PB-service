import requests
import datetime

def sn_shipments(sn):
    if sn:
        url = 'http://gw.greendata.com.ua:8008/api/get-device-info'
        try:
            info = requests.get(url,params={'sn': sn}, verify=False).json()
            # info = [{"shippingDate":"2015-03-21 12:00:00","manufacturer":"Yitoa","partner":"PB Readers","partnerCountry":"Germany","device":"PocketBook Touch Lux 2","model":"PB626","year":"2015","month":"01","country":"\u0412\u0435\u0441\u044c \u043c\u0438\u0440","color":"\u0411\u0435\u043b\u044b\u0439","countryEng":"WorldWide","colorEng":"White"}]
        except:
            return 'Erorr'
        if info:
            for element in info:
                element['shippingDate'] = datetime.datetime.strptime(element['shippingDate'], "%Y-%m-%d %H:%M:%S")
            return info
        else:
            return False