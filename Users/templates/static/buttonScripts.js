// Archivo javascript para darle funcionalidad a los botones

function redirect(link){
    url = "/home/"  // Url de redireccion

    // Funcionalidad de los botones "Cancelar"
    if (link.name.length == 0){
        location.href = url;
    }
    else {
        // Funcionalidad de los botones "Editar"
        if(link.name == 'edit'){ url += link.value + "/edit-user"; }
        // Funcionalidad de los botones "Eliminar"
        else if(link.name == 'delete'){ url += link.value + "/delete-user"; }
        // Funcionalidad del boton "Insertar Nuevo Usuario"
        else{ url += "new-user"; }

        location.href = url;
    }
};