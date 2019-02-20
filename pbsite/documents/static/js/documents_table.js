$(document).ready(function() {
    $('#documents_table').DataTable( {
         "order": [[ 6, "desc" ]],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'print',
        ]
    } );
} );