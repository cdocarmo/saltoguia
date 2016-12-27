var fila_seleccionada = null;

$(document).ready(function(){

    $('#guardar').on('click', function(){
        var data = {};
        var postdata = {};
        
        postdata['paciente'] = $('#nuevo-entrada-paciente').val();
        postdata['medico'] = $('#nuevo-entrada-medico').val();
        postdata['acto_medico_id'] = $('#nuevo-entrada-acto-medico option:selected' ).val();
        postdata['acto_medico_nombre'] = $('#nuevo-entrada-acto-medico option:selected' ).text();
        postdata['descripcion'] = $('#nuevo-entrada-descripcion').val();
        postdata['csrfmiddlewaretoken'] = $('#nuevo-entrada-csrf-token').val();
        
        console.log(postdata);
        
        data['url'] = $('#formulario-nuevo').attr('action');
        data['type'] = 'POST';
        data['data'] = postdata;
        data['datatype'] = 'json';
        data['success'] = function(response) {
            var fila = $('<tr class="fila-dato" data-id="' + response.ultimo_id + '" data-token="{{ csrf_token }}">\
                      <td>' + response.creado + '</td>\
                      <td>' + postdata.medico + '</td>\
                      <td>' + postdata.acto_medico_nombre + '</td>\
                      <td>' + postdata.descripcion + '</td>\
                    </tr>');
            $(fila).find('td').on('click', seleccionarFila); //rebind event
            $('.contenedor-listado table tbody').append(fila).addEvent;
            $('#modal-nuevo-paciente').modal('hide');
            console.log(JSON.stringify(response));
        }
        
        ajax(data);
    });
    
    $('#btn-actualizar').on('click', function(){
        var acto = $(fila_seleccionada).find('.entrada-acto-medico span').html()
        $('#actualizar-entrada-acto-medico').find("option[value='" + acto + "']").attr("selected",true);
        $('#actualizar-entrada-descripcion').val($(fila_seleccionada).find('.entrada-descripcion').html());
        return true;
    });
    
    $('#actualizar').on('click', function(){
        var data = {};
        var postdata = {};
        
        postdata['entrada_id'] = $(fila_seleccionada).attr('data-id');
        postdata['acto_medico_id'] = $('#actualizar-entrada-acto-medico option:selected' ).val();
        postdata['acto_medico_nombre'] = $('#actualizar-entrada-acto-medico option:selected' ).text();
        postdata['descripcion'] = $('#actualizar-entrada-descripcion').val();
        postdata['csrfmiddlewaretoken'] = $('#actualizar-entrada-csrf-token').val();
        
        console.log(postdata);
        
        data['url'] = $('#formulario-actualizar').attr('action');
        data['type'] = 'PUT';
        data['data'] = postdata;
        data['datatype'] = 'json';
        data['success'] = function(response) {
            //$(fila_seleccionada).find('.entrada-fecha').html(postdata['nombres']);
            //$(fila_seleccionada).find('.entrada-medico').html(postdata['apellidos']);
            $(fila_seleccionada).find('.entrada-acto-medico').html(postdata['acto_medico_nombre']);
            $(fila_seleccionada).find('.entrada-acto-medico span').html(postdata['acto_medico_id']);
            $(fila_seleccionada).find('.entrada-descripcion').html(postdata['descripcion']);
            alert('Actualizado correctamente.');
            $('#modal-actualizar-paciente').modal('hide');
            console.log(JSON.stringify(response));
        }
        
        ajax(data);
    });
    
    //$('#btn-eliminar').on('click', function(){
    //    
    //});
    
    //=====================================
    //              EVENTOS
    //=====================================
    $('.fila-dato td').on('click', seleccionarFila);

});

//========================================
//AJAXAJAXAJAXAJAXAJAXAJAXAJAXAJAXAJAXAJAX
//========================================

function ajax(data) {
    if (data.type != 'POST' && data.type != 'GET') {
        //alert('entra a metodo ' + data.type)
        $.ajax({
            url : data.url,
            type : 'POST',
            data: data.data,
            dataType: data.datatype,
            headers: {'X-HTTP-Method-Override': data.type},
            success : data.success,
            error : function(request, error)
            {
                alert("Error - Comuníquese a soporte@muelitas.uy");
                console.log("Request: "+JSON.stringify(request))
            }
        });
    } else {
        $.ajax({
            url : data.url,
            type : data.type,
            data: data.data,
            dataType: data.datatype,
            success : data.success,
            error : function(request, error)
            {
                alert("Error - Comuníquese a soporte@muelitas.uy");
                console.log("Request: "+JSON.stringify(request))
            }
        });
    }
}

//========================================
// MANEJADORES DE EVENTOS
function seleccionarFila() {
    var styles_selected = {
                    backgroundColor : "blue",
                    color: "white"
                };
    var styles_deselected = {
                    backgroundColor : "white",
                    color: "black"
                };
    
    $('tr[class*=fila-dato]').each(function(){
        if ($(this).hasClass('fila-dato-selected')) {
            //alert(this);
            $(this).removeClass('fila-dato-selected').addClass('fila-dato');
            $(this).css(styles_deselected);
        }
        
    });
    $(this).parent().removeClass('fila-dato').addClass('fila-dato-selected');
    $(this).parent().css(styles_selected);
    $('#btn-actualizar, #btn-eliminar').removeClass('disabled');
    fila_seleccionada = $(this).parent();
    //alert($(fila_seleccionada).attr('data-id'));
}

//========================================
// UTILIDADES
