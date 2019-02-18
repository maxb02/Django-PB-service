$(document).ready(function() {
    $('#documents_table').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copy', 'excel', 'pdf',
        ]
    } );
} );