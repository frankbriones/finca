$(document).ready(function() {
    $('.loader').hide();
    $('.editar_solicitud').show()
})



$('.editar_solicitud').on('click', function(){
    $(this).hide();
    $('#id_item_detalles').prop('disabled', false);

    id_solicitud = $(this).attr('data-id_solicitud');
    detalle_item = $(this).attr('data-detalle_item');


    // agregar boton de confirmacion
    $('#id_detalles').append(
        `<div class="row" id="accion_edicion">
            <div class="col-12 d-flex justify-content-end m-1">
                <button id="id_boton_confirmar"  class="btn btn-primary" data-detail="`+ detalle_item +`" onclick="confirmarEdicion(`+ id_solicitud+`)" >`+textoboton+`</button>
            </div>
        </div>
    `);
    obtenerOrigenMaterial();
    if(detalle_item != 'SERVICIO GENERICO'){
        $('#id_cant_piedras').prop('disabled', false);
        $('#id_cant_piedras').prop('type', 'number');
        obtenerColores();
        obtenerTallas();
    }
    

})

function obtenerOrigenMaterial(){
    var select = `
            <select  id="id_select_origen" class="form-control">
                <option value="0">---Seleccionar---</option>
            </select>
            <input type="number" hidden="">
            <label for="id_ciudad">Origen de material</label>
        `;
    var divselect = document.getElementById('id_origen_edicion');
	$(divselect).empty()
    $(divselect).append(select)
    $.ajax({
        url : '/transacciones/obtener-origen-material/solicitudes/',
        type: 'GET',
        success: function (data) {
            origenes = data.data
            
            origenes.forEach(origen => {
                var option = document.createElement("option");
                option.value = origen.id_origen;
                option.text = origen.descripcion;
                $('#id_select_origen').append(option);
            })
        }

    });
}

// mostrar select de las tallas para serv de producto
function obtenerTallas(){
    var select = `
            <select  id="id_select_talla" class="form-control">
                <option value="0">---Seleccionar---</option>
            </select>
            <input type="number" hidden="">
            <label for="id_ciudad">Tallas</label>
        `;
    var divselect = document.getElementById('id_talla_edicion');
	$(divselect).empty()
    $(divselect).append(select)
    $.ajax({
        url : '/transacciones/obtener-tallas/solicitudes/',
        type: 'GET',
        success: function (data) {
            tallas = data.data
            tallas.forEach(talla => {
                var option = document.createElement("option");
                option.value = talla.id_talla;
                option.text = talla.talla;
                $('#id_select_talla').append(option);
            })
        }

    });
}


// mostrar select de colores para serv de producto
function obtenerColores(){
    var select = `
            <select  id="id_select_color" class="form-control">
                <option value="0">---Seleccionar---</option>
            </select>
            <input type="number" hidden="">
            <label for="id_ciudad">Colores</label>
        `;
    var divselect = document.getElementById('id_color_edicion');
	$(divselect).empty()
    $(divselect).append(select)
    $.ajax({
        url : '/transacciones/obtener-colores/solicitudes/',
        type: 'GET',
        success: function (data) {
            colores = data.data
            colores.forEach(color => {
                var option = document.createElement("option");
                option.value = color.id_color;
                option.text = color.descripcion;
                $('#id_select_color').append(option);
            })
        }

    });
}

async function confirmarEdicion(id_solicitud){
    var detail = $('#id_boton_confirmar').attr('data-detail');
    var url = "/transacciones/editar/solicitud/"
    let detalle = $('#id_item_detalles').val();
    let id_origen = $('#id_select_origen').val();
    let cantidad_piedras = $('#id_cant_piedras').val();
    let color_id = $('#id_select_color').val();
    let talla_id = $('#id_select_talla').val();

    if(talla_id === '0'){
        toastr.error('Debe seleccionar una talla.', 'Error')
        return false;
    }

    if(color_id === '0'){
        toastr.error('Debe seleccionar un color.', 'Error')
        return false;
    }

    if(cantidad_piedras === ''){
        toastr.error('Debe ingresar una cantidad para las piedras.', 'Error')
        return false;
    }

    if(id_origen === '0'){
        toastr.error('Debe seleccionar origen de material.', 'Error')
        return false;
    }
    if(detalle === ''){
        toastr.error('No puede estar el detalle de la solicitud vacio', titulo);
        return false
    }
    if(detail != 'SERVICIO GENERICO'){
        data = {
            'descripcion_solicitud': detalle,
            'id_solicitud': id_solicitud,
            'id_origen': id_origen,
            'cant_piedras': cantidad_piedras,
            'color_id': color_id,
            'talla_id': talla_id
        }
    }else{
        data = {
            'descripcion_solicitud': detalle,
            'id_solicitud': id_solicitud,
            'id_origen': id_origen,
            'cant_piedras': cantidad_piedras
        }
    }
    
    $.ajax({
        async: true,
        url: url,
        type: 'GET',
        data: data,
        success: function(response){
            mensaje = response.mensaje
            $('#id_item_detalles').prop('disabled', true);
            $('#id_cant_piedras').prop('disabled', true);
            $('#id_select_origen').prop('disabled', true);
            $('#id_select_color').prop('disabled', true);
            $('#id_select_talla').prop('disabled', true);

            

            $('#accion_edicion').hide();
            toastr.success(mensajeexito, titulo);
            return false;
            // email_app_details = $(".email-app-details");
            // email_app_details.toggleClass('show');
            // verDetalleOrden(id_solicitud);
        }
        
    })
    
}