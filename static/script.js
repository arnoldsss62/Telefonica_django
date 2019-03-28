

var side_botton = document.getElementById("sidebarCollapse");
var sidebar = document.getElementById("sidebar");
var side_botton_alter = document.getElementById("sidebarCollapse_alter");


function cerrar() {

    
    sidebar.style.width = "90px";
    document.getElementById("TN").style.display = "none";
    document.getElementById("BC").style.display = "none";
    document.getElementById("Upload").style.display = "none";
    document.getElementById("Calendar").style.display = "none";
    document.getElementById("Form").style.display = "none";
    document.getElementById("home").style.display = "none";
    document.getElementById("Lista").style.display = "none";
    document.getElementById("reporte").style.display = "none";
    document.getElementById("img_home").style.display = "block";
    document.getElementById("img_buscarcliente").style.display = "block";
    document.getElementById("img_tareas").style.display = "block";
    document.getElementById("img_formulario").style.display = "block";
    document.getElementById("img_calendario").style.display = "block";
    document.getElementById("img_upload").style.display = "block";
    document.getElementById("img_listar_usuarios").style.display = "block";
    document.getElementById("img_reporte").style.display = "block";
    
}


function abrir() {

    sidebar.style.width = "250px";
    document.getElementById("TN").style.display = "block";
    document.getElementById("BC").style.display = "block";
    document.getElementById("Upload").style.display = "block";
    document.getElementById("Calendar").style.display = "block";
    document.getElementById("Form").style.display = "block";
    document.getElementById("home").style.display = "block";
    document.getElementById("Lista").style.display = "block";
    document.getElementById("reporte").style.display = "block";
    document.getElementById("img_home").style.display = "none";
    document.getElementById("img_buscarcliente").style.display = "none";
    document.getElementById("img_tareas").style.display = "none";
    document.getElementById("img_formulario").style.display = "none";
    document.getElementById("img_calendario").style.display = "none";
    document.getElementById("img_upload").style.display = "none";
    document.getElementById("img_listar_usuarios").style.display = "none";
    document.getElementById("img_reporte").style.display = "none";
    
    

}


function abrir_cerrar() {


    if (sidebar.style.width == "250px") {

        cerrar()
    } else {

        

        abrir()
    }
}

let up = window.pageYOffset;
window.onscroll = function(){

    let DA = window.pageYOffset;
    if (up >= 50){
        document.getElementById("header_s").style.marginTop = "480px";
        
    }
    else {
        document.getElementById("header_s").style.marginTop = "600px";

    }
    up = DA;
}




let myChart= document.getElementById("myChart")
let massPopChart = new Chart(myChart,{
    type:'line',
    data:{

        labels:[],
        datasets:[{

            label:'Trabajos',
            data:[],
            borderWidth:4,
            borderColor:'black'
  
        }]

    }


});


function seleccion_rangos(){

    if(document.getElementById("rango").value == "mes"){

        document.getElementById("seleccion_años").style.display = "block";
        document.getElementById("seleccion_mes").style.display = "block";
    }


    else if(document.getElementById("rango").value == "año"){

        document.getElementById("seleccion_mes").style.display = "none";
        document.getElementById("seleccion_años").style.display = "block";
    }

    else{
        
        document.getElementById("seleccion_mes").style.display = "none";
        document.getElementById("seleccion_años").style.display = "none";
    }
}













