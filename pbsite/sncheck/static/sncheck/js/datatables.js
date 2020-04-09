$(document).ready(function () {
    $('#serial_number_table').DataTable({
        "paging": false,
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


// $(document).ready(function () {
//     $('#serial_number_table').DataTable({
//         "order": [],
//
//         dom: 'Bfrtip',
//         buttons: [
//             'copy', 'excel', 'print',
//         ]
//     });
// });