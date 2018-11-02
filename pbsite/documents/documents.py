def get_act_number(act):
    return '{}{}{}{}'.format(act.serial_number[:5],act.id,act.created_by.id,act.created_by.service_center.id)

def send_notification(act):
    subject = 'Document {} {}'.format(act.serial_number, act.status)
    from_email = 'noreplay@service.pocketbook-int.com'
    to = [act.created_by.email, act.created_by.service_center.manager_email]
    cc = list(EmailForNotifications.objects.all())
    emai_template = 'dociments/{}_notifier_letter.html'.format(act.created_by.service_center.language)
    html_content = get_template(emai_template).render(
        {'act': act,
         })
    msg = EmailMessage(subject, html_content, from_email, to, cc=cc, )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
