class UserServiceCenterObjectOnlyMixin:
    """Mixin which limits query set to objects where the 'service center' of the user is the same
    with current 'user service' center"""
    user_field = 'user'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            kwargs = {'{}__service_center'.format(self.user_field): self.request.user.service_center}
            queryset = queryset.filter(**kwargs)

        return queryset
