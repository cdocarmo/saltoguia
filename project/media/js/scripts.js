/**
 * @author Gabriel Oriol Fernández Rodríguez
 * Este script reune de una sola todas las funcionalidades necesarias
 */

function detectarNavegador(){
	
	//~~~~~~~~~~~~~~Detecta compatibilidad de navegadores~~~~~~~~~~~~~~~~
	var navName = navigator.appCodeName;
	var navVersion = navigator.appVersion;
	var regex = /MSIE 9\.0/;
	var resultado = navVersion.match(regex);
	if (resultado == null) {
		crearAdvertencia();
	}
	var regex = /MSIE 9\.0/;
	var resultado = navVersion.match(regex);
	if (resultado == null) {
		crearAdvertencia();
	}
	//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
};

//~~~~~~~~~~~~~~~~~~~~~~~~~Metodos varios~~~~~~~~~~~~~~~~~~~~~~~~~~
function crearAdvertencia(){
	//Crea un div de advertencia cuando se usa un navegador obsoleto
	var html = '<div class="advertencia">Este sitio no se visualiza correctamente' + 
	'porque est&aacute;s utilizando un navegador desactualizado' +
	'que no respeta los est&aacute;ndares Web,' + 
	'por tal motivo te pedimos encarecidamente que actualices tu navegador haciendo' +
	'clic en uno de los siguientes enlaces: <a href="">Mozilla Firefox</a>, ' + 
	'<a href="">Opera</a>, <a href="">Internet Explorer</a><span>X</span>';
	$('#wrapper_header').before(html);
}

function eliminarAdvertencia(){
	//Elimina la advertencia creada por causa de un navegador obsoleto
	$('.advertencia').remove();
}
