from django.core.mail import EmailMessage

def regionmismatch(serial_number, device_region, user, email_for_notifications_list):
    subject = 'Region Mismatch {} {}'.format(serial_number, user.username)
    from_email = 'noreplay@service.pocketbook-int.com'
    to = email_for_notifications_list
    username = user.username
    userfullname = user.get_full_name()
    usergroupslist = list(user.groups.values_list('name',flat=True))
    html_content = "<b>SN:</b> {}<br><b>Device Region:</b> {} <br><b>User Name:</b> {} {} <br><b>User Groups</b>: {}".format(serial_number, device_region, username, userfullname, usergroupslist)
    msg = EmailMessage(subject, html_content, from_email, to)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()