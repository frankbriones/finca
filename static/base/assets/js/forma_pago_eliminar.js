$(document).ready(function() {
    $('.loader').hide();
});

$(document).on('click','.eliminar_forma_pago',function() {	
	var forma_pago = $(this).attr('data-forma_pago');
	var descripcion = $(this).attr('data-descripcion');
	data={
		'forma_pago': forma_pago
	}
	$("#modal_eliminar_forma_pago .forma_pago_descripcion").text(descripcion);
	$("#modal_eliminar_forma_pago .id_forma_pago_eliminar").val(forma_pago);
    $('#modal_eliminar_forma_pago').modal('show');
})


$("#modal_eliminar_forma_pago .delete_forma_pago").click(function ()
{
	var forma_pago = $("#modal_eliminar_forma_pago .id_forma_pago_eliminar").val();
	var parametros = {
			"forma_pago": forma_pago,
        };
	eliminar_forma_pago(parametros);
    
})



function eliminar_forma_pago(parametros)
{
	$.ajax({
		url: '/configuraciones/formaspago/eliminar',
		type: 'GET',
		data: parametros,

		success: function(data){
			if(data.estado==1){
                $('#modal_eliminar_forma_pago').modal('hide');
                document.location.href='/configuraciones/formaspago/lista';
                $('.loader').hide();                
			}else if(data.estado==2){
				$('#modal_eliminar_forma_pago').modal('hide');
				toastr.error("Froma de pago no puede ser eliminada.",'Error');
			}
			else{
				toastr.error("Forma de pago No existe.",'Error');
			}
		}

	})

}

