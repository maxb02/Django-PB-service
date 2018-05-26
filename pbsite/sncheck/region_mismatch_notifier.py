from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import EmailForNotifications


def region_mistmatch_notifier(serial_number, device_data, user, language):
    subject = 'Region Mismatch {}'.format(serial_number, )
    from_email = 'noreplay@service.pocketbook-int.com'
    to = [user.email]
    cc = list(EmailForNotifications.objects.all())
    if language == 'ru':
        emai_template = 'sncheck/region_mismatch_notifier letter_ru.html'
    else:
        emai_template = 'sncheck/region_mismatch_notifier letter_en.html'

    html_content = get_template(emai_template).render(
        {'serial_number': serial_number,
             'device_data': device_data
             })
    msg = EmailMessage(subject, html_content, from_email, to, cc=cc, reply_to=['maxbondar02@gmail.com'])
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()