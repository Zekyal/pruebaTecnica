function redirect(link){
    url = "/home/"

    if (link.name.length == 0){
        location.href = url;
    }
    else {
        if(link.name == 'edit'){ url += link.value + "/edit-user"; }
        else if(link.name == 'delete'){ url += link.value + "/delete-user"; }
        else{ url += "new-user"; }

        location.href = url;
    }
};