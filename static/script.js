window.onload = function(){
    var contenedor = document.getElementById('contenedor_carga');
    contenedor.style.display  = 'none';
    
}

var side_botton = document.getElementById("sidebarCollapse");
var sidebar = document.getElementById("sidebar");


function cerrar(){


    sidebar.style.width = "90px";
    document.getElementById("BC").style.display = "none";
    document.getElementById("Upload").style.display = "none";
    document.getElementById("Calendar").style.display = "none";
    document.getElementById("Form").style.display = "none";
    document.getElementById("home").style.display = "none";


    
}


function abrir(){

    sidebar.style.width = "250px";
   document.getElementById("TN").style.displat = "block";
   document.getElementById("BC").style.display = "blck";
   document.getElementById("Upload").style.display = "blck";
   document.getElementById("Calendar").style.display = "block";
   document.getElementById("Form").style.display = "block";
   document.getElementById("home").style.display = "block";
   


}


function abrir_cerrar(){


    if(sidebar.style.width == "250px"){

        cerrar()
    }

    else{

        abrir()
    }
}
