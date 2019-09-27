$(document).ready(function() {
    $('#documents_table').DataTable( {
         "order": [[ 0, "desc" ]],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'print',
        ]
    } );
} );