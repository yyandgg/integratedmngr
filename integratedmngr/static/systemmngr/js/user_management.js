var UserManagement = function(){
    
    var initDataTables = function(){
	
	//initiate dataTables plugin
	var myTable = $('#dynamic-table').DataTable({
					bAutoWidth: false,
					"aoColumns": [
					  { "bSortable": false },
					  null,null,null,null,
					  { "bSortable": false }
					],
					"aaSorting": [],
					
					
					//"bProcessing": true,
	                                //"bServerSide": true,
			                //"sAjaxSource": "http://127.0.0.1/table.php"	,
			
					//,
					//"sScrollY": "200px",
					//"bPaginate": false,
			
					//"sScrollX": "100%",
					//"sScrollXInner": "120%",
					//"bScrollCollapse": true,
					//Note: if you are applying horizontal scrolling (sScrollX) on a ".table-bordered"
					//you may want to wrap the table inside a "div.dataTables_borderWrap" element
			
					//"iDisplayLength": 50
			
			
					select: {
						style: 'multi'
					}
			    } );
	$.fn.dataTable.Buttons.defaults.dom.container.className = 'dt-buttons btn-overlap btn-group btn-overlap';
	new $.fn.dataTable.Buttons( myTable, {
	    buttons: [
		{
		    "extend": "colvis",
		    "text": "<i class='fa fa-search bigger-110 blue'></i> <span class='hidden'>Show/hide columns</span>",
		    "className": "btn btn-white btn-primary btn-bold",
		    columns: ':not(:first):not(:last)'
		},
		{
		    "extend": "copy",
		    "text": "<i class='fa fa-copy bigger-110 pink'></i> <span class='hidden'>Copy to clipboard</span>",
		    "className": "btn btn-white btn-primary btn-bold"
		},
		{
		    "extend": "csv",
		    "text": "<i class='fa fa-database bigger-110 orange'></i> <span class='hidden'>Export to CSV</span>",
		    "className": "btn btn-white btn-primary btn-bold"
		},
		{
		    "extend": "excel",
		    "text": "<i class='fa fa-file-excel-o bigger-110 green'></i> <span class='hidden'>Export to Excel</span>",
		    "className": "btn btn-white btn-primary btn-bold"
		},
		{
		    "extend": "pdf",
		    "text": "<i class='fa fa-file-pdf-o bigger-110 red'></i> <span class='hidden'>Export to PDF</span>",
		    "className": "btn btn-white btn-primary btn-bold"
		},
		{
		    "extend": "print",
		    "text": "<i class='fa fa-print bigger-110 grey'></i> <span class='hidden'>Print</span>",
		    "className": "btn btn-white btn-primary btn-bold",
		    autoPrint: false,
		    message: 'This print was produced using the Print button for DataTables'
		}		  
	    ]
	} );
	myTable.buttons().container().appendTo( $('.tableTools-container') );
	
	
	myTable.on( 'select', function ( e, dt, type, index ) {
	    if ( type === 'row' ) {
		$( myTable.row( index ).node() ).find('input:checkbox').prop('checked', true);
	    }
	} );
	myTable.on( 'deselect', function ( e, dt, type, index ) {
	    if ( type === 'row' ) {
		$( myTable.row( index ).node() ).find('input:checkbox').prop('checked', false);
	    }
	} );
	
	//table checkboxes
	$('th input[type=checkbox], td input[type=checkbox]').prop('checked', false);
	
	//select/deselect all rows according to table header checkbox
	$('#dynamic-table > thead > tr > th input[type=checkbox], #dynamic-table_wrapper input[type=checkbox]').eq(0).on('click', function(){
	    var th_checked = this.checked;//checkbox inside "TH" table header
	    
	    $('#dynamic-table').find('tbody > tr').each(function(){
		var row = this;
		if(th_checked) myTable.row(row).select();
		else  myTable.row(row).deselect();
	    });
	});
	
	//select/deselect a row when the checkbox is checked/unchecked
	$('#dynamic-table').on('click', 'td input[type=checkbox]' , function(){
	    var row = $(this).closest('tr').get(0);
	    if(this.checked) myTable.row(row).deselect();
	    else myTable.row(row).select();
	});
	
	
	
	$(document).on('click', '#dynamic-table .dropdown-toggle', function(e) {
	    e.stopImmediatePropagation();
	    e.stopPropagation();
	    e.preventDefault();
	});
	
    };
    var initContents = function(){
	$(".remove-profile").click(function(){
	    var remove_profile_full_id = $(this).attr("id").split("-");
	    var remove_profile_id = remove_profile_full_id[2];
	    
	    $.post("/user/delete-profile/" + remove_profile_id +"/", function(resp_msg){
		location.reload();
	    });
	});
    };

    return {
	init: function(){
	    initDataTables();
	    initContents();
	}
    }
}();
