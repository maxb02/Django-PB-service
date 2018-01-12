from django.core.mail import send_mail

def regionmismatch(serial_number, device_region, user, email_for_notifications_list):
    send_mail(
        'Region Mismatch {} {}'.format(serial_number, user.username),
        'SN:{} /n Device Region:{} /n User Groups:{} /n User name:{} /n {}'.format(serial_number, device_region, list(user.groups.values_list('name',flat=True)), user.username, user.get_full_name()),
        'noreplay@service.pocketbook-int.com',
        email_for_notifications_list,
        fail_silently=False,
    )