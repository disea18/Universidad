(function(){
    const btnEliminacion=document.querySelectorALL(".btnEliminacion");

btnEliminacion.array.forEach(btn => {
    btn.addEventListener('click',(e)=>{
        const confirmacion = confirm('¿Seguro de eliminar el curso?');
        if(!confirmacion){
            e.preventDefault();
        }
    } )
});
})