
def region_ceker(user, ):
    if not (request.user.groups.filter(
            name='moderator').exists() or request.user.is_superuser or info == False or info == 'Erorr'):
        for data in info:
            if not request.user.groups.filter(name=data['countryEng']).exists():
                regionmismatch(serial_number, data['countryEng'], request.user,
                               list(EmailForNotifications.objects.all()))
