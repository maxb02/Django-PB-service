$(document).ready(function() {
    $('#refurbishment_device_table').DataTable( {
         "order": [[ 6, "desc" ]],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'print',
        ]
    } );
} );