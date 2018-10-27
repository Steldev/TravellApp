$(document).ready(function () {

    openModal();//вызываем нашу функцию

});


//функция modal
function openModal() {

    //Открываем модалку при клике
    $(".delete_element").click(function () {
        $(".modal").show('fast');//показывает див модалки
    });

//закрывает модалку при клике на кнопку Закрыть

    $(".cancel_button").click(function () {
        $(".modal").hide('fast');//скрывает див модалки

    });
}
;