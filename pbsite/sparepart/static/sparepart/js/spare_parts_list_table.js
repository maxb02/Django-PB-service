$(document).ready(function() {
    $('#spare_parts_table').DataTable( {
         "order": [[ 1, "desc" ]],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'print',
        ]
    } );
} );