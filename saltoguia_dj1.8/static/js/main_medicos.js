var fila_seleccionada = null;

$(document).ready(function(){

    $('#guardar').on('click', function(){
        var data = {};
        var postdata = {};

        postdata['nombres'] = $('#nuevo-nombres').val();
        postdata['apellidos'] = $('#nuevo-apellidos').val();
        postdata['domicilio'] = $('#nuevo-domicilio').val();
        postdata['ci'] = $('#nuevo-ci').val();
        postdata['email'] = $('#nuevo-email').val();
        postdata['comentarios'] = $('#nuevo-comentarios').val();
        postdata['csrfmiddlewaretoken'] = $('#nuevo-csrf-token').val();

        console.log(postdata);

        data['url'] = $('#formulario-nuevo').attr('action');
        data['type'] = 'POST';
        data['data'] = postdata;
        data['datatype'] = 'json';
        data['success'] = function(response) {
            var fila = $('<tr class="fila-dato" data-id="' + response.ultimo_id + '" data-token="{{ csrf_token }}">\
                      <td>' + response.ultimo_id + '</td>\
                      <td>' + postdata.nombres + '</td>\
                      <td>' + postdata.apellidos + '</td>\
                      <td>' + postdata.ci + '</td>\
                      <td> - - </td>\
                      <td>' + postdata.domicilio + '</td>\
                      <td>' + postdata.email + '</td>\
                    </tr>');
            $('.contenedor-listado table tbody').append(fila);
            $('#modal-nuevo-medico').modal('hide');
            console.log(JSON.stringify(response));
        }

        ajax(data);
    });

    $('#btn-actualizar').on('click', function(){
        $('#actualizar-id').val($(fila_seleccionada).find('.medico-id').html());  //oculto, TODO: revisar seguridad de esto
        $('#actualizar-nombres').val($(fila_seleccionada).find('.medico-nombres').html());
        $('#actualizar-apellidos').val($(fila_seleccionada).find('.medico-apellidos').html());
        $('#actualizar-domicilio').val($(fila_seleccionada).find('.medico-domicilio').html());
        $('#actualizar-ci').val($(fila_seleccionada).find('.medico-ci').html());
        $('#actualizar-email').val($(fila_seleccionada).find('.medico-email').html());
        $('#actualizar-comentarios').val($(fila_seleccionada).find('.medico-comentarios').html());
        return true;
    });

    $('#actualizar').on('click', function(){
        var data = {};
        var postdata = {};

        postdata['nombres'] = $('#actualizar-nombres').val();
        postdata['apellidos'] = $('#actualizar-apellidos').val();
        postdata['domicilio'] = $('#actualizar-domicilio').val();
        postdata['ci'] = $('#actualizar-ci').val();
        postdata['email'] = $('#actualizar-email').val();
        postdata['comentarios'] = $('#actualizar-comentarios').val();
        postdata['csrfmiddlewaretoken'] = $('#actualizar-csrf-token').val();

        console.log(postdata);

        data['url'] = $('#formulario-actualizar').attr('action') + $('#actualizar-id').val() + '/';
        data['type'] = 'PUT';
        data['data'] = postdata;
        data['datatype'] = 'json';
        data['success'] = function(response) {
            $(fila_seleccionada).find('.medico-nombres').html(postdata['nombres']);
            $(fila_seleccionada).find('.medico-apellidos').html(postdata['apellidos']);
            $(fila_seleccionada).find('.medico-domicilio').html(postdata['domicilio']);
            $(fila_seleccionada).find('.medico-ci').html(postdata['ci']);
            $(fila_seleccionada).find('.medico-email').html(postdata['email']);
            $(fila_seleccionada).find('.medico-email').html(postdata['comentarios']);
            alert('Actualizado correctamente.');
            $('#modal-actualizar-medico').modal('hide');
            console.log(JSON.stringify(response));
        }

        ajax(data);
    });

    $('#btn-eliminar').on('click', function(){
        var data = {};
        var postdata = {};

        postdata['id'] = $(fila_seleccionada).attr('data-id');
        postdata['csrfmiddlewaretoken'] = $(fila_seleccionada).attr('data-token');

        //console.log(postdata['csrfmiddlewaretoken']);

        data['url'] = $('#formulario-eliminar').attr('action');
        data['type'] = 'DELETE';
        data['data'] = postdata;
        data['datatype'] = 'json';
        data['success'] = function(response) {
            $(fila_seleccionada).remove();
            $('#btn-actualizar, #btn-eliminar').addClass('disabled');
            alert('Eliminado correctamente.');
            console.log(JSON.stringify(response));
        }

        ajax(data);
    });

    //=====================================
    //              EVENTOS
    //=====================================
    $('.fila-dato td').on('click', function(){
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
    });

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
// UTILIDADES
function agregarMedico(data) {
    console.log(data);
}