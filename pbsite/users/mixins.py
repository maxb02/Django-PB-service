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


class CreatedByUserMixin:
    created_by_field = 'created_by'

    def form_valid(self, form):
        created_by = self.request.user
        setattr(form.instance, self.created_by_field, created_by)
        return super().form_valid(form)
