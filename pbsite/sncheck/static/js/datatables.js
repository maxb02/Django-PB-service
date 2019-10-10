$(document).ready(function () {
    $('#seral_number_table').DataTable({
        paging: false,
        "order": [],
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excel',
                title: ''
            },
            {
                extend: 'copy',
                title: '',
                header: ''

            },
            {
                extend: 'print',
                title: ''
            }
        ]
    });
});