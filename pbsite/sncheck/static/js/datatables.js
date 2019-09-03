$(document).ready(function () {
    $('#seral_number_table').DataTable({
        "order": [],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'print',
        ]
    });
});