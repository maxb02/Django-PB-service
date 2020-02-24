$(document).ready(function () {
    $('#serial_number_table').DataTable({
        pading: false,
        "order": [],
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