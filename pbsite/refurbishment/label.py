from collections import namedtuple

from django.http import HttpResponse
from reportlab.graphics.barcode import code128
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from device.serial_number_parser import get_model_sku_color
from refurbishment.models import RefurbishmentDevice

LabelData = namedtuple('LabelData', ['serial_number', 'model', 'sku', 'color', 'date_field_name', 'date'])


def get_sku_with_suffix(sku, sku_suffix):
    """return SKU with suffix for refurbishment device"""
    if sku_suffix:
        return '{}-{}'.format(sku, sku_suffix)
    return sku


def get_info_for_label(pk):
    """prepare info for label"""
    refurbishment_device = RefurbishmentDevice.objects.select_related('condition').get(pk=pk)
    serial_number = refurbishment_device.new_serial_number
    create_date = refurbishment_device.create_date
    sku_suffix = refurbishment_device.condition.sku_suffix
    date_field_name = refurbishment_device.condition.get_label_date_field_name_display()
    model_sku_color = get_model_sku_color(serial_number)
    sku_with_suffix = get_sku_with_suffix(sku=model_sku_color['skus__name'],
                                          sku_suffix=sku_suffix)
    label_data = LabelData(serial_number=serial_number,
                           model=model_sku_color['name'],
                           color=model_sku_color['skus__color__name'],
                           sku=sku_with_suffix,
                           date_field_name=date_field_name,
                           date=create_date)
    return label_data


def create_label_response(label_data: LabelData, number=1):
    """create label and return response object with PDF label file"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="{}-barcode.pdf"'.format(label_data.serial_number)
    barcode = code128.Code128(label_data.serial_number, barHeight=10 * mm, barWidth=0.211 * mm, quiet=False)
    page = canvas.Canvas(response)
    page.setPageSize((51 * mm, 30 * mm))

    for i in range(number):
        page.setFontSize(6)
        page.drawString(2 * mm, 27 * mm, 'Model: {}'.format(label_data.model))
        page.drawString(2 * mm, 24 * mm, 'Color: {}'.format(label_data.color))
        page.drawString(2 * mm, 21 * mm, 'Item No./SKU: {}'.format(label_data.sku))
        page.drawString(7 * mm, 16 * mm, 'Serial No: {}'.format(label_data.serial_number))

        barcode.drawOn(page, 2 * mm, 5 * mm)
        page.lines([(2 * mm, 4 * mm, 49 * mm, 4 * mm), (2 * mm, 18.5 * mm, 49 * mm, 18.5 * mm)])
        page.drawString(2 * mm, 1 * mm,
                        '{}: {}'.format(label_data.date_field_name, label_data.date.strftime("%d.%m.%Y")))
        page.showPage()
    page.save()

    return response
