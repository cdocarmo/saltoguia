/**
 * @author Gabriel Oriol Fernández Rodríguez
 * Este script reune de una sola todas las funcionalidades necesarias
 */

function detectarNavegador(){
	
	//~~~~~~~~~~~~~~Detecta compatibilidad de navegadores~~~~~~~~~~~~~~~~
	//var navName = navigator.appCodeName;
	var navVersion = navigator.appVersion;
	
	var regex = /MSIE/;
	var resultado = navVersion.match(regex);
	if (resultado != null) {
		var regex = /MSIE 9\.0/;
		var resultado = navVersion.match(regex);
		if (resultado == null) {
			crearAdvertencia();
		}
	}
	//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

//~~~~~~~~~~~~~~~~~~~~~~~~~Metodos varios~~~~~~~~~~~~~~~~~~~~~~~~~~
function crearAdvertencia(){
	//Crea un div de advertencia cuando se usa un navegador obsoleto
	var html = '<div class="advertencia"><p>Posiblemente no puedes visualizar correctamente' + 
	' este sitio debido a que usas un navegador desactualizado ' +
	'por tal motivo te solicitamos que actualices tu navegador haciendo' +
	'clic en uno de los siguientes enlaces: <a href="http://www.mozilla.org/es-ES/firefox/new/">Firefox</a>, ' + 
	'<a href="http://www.opera.com/browser/download/">Opera</a>, <a href="http://windows.microsoft.com/es-ES/internet-explorer/products/ie/home">Internet Explorer</a></p><img src="/media/images/cerrar.gif">';
	$('#wrapper_header').before(html);
}

function eliminarAdvertencia(){
	//Elimina la advertencia creada por causa de un navegador obsoleto
	$('.advertencia').remove();
}
