function editMaruza(){
    let edit_btn = document.querySelector('.edit_btn');
    $.ajax({
        url: "edit_maruza",
        type: 'get',
        data: { attr: edit_btn.getAttribute('data-edit')},
        success: function (data) {
            showEditData(data.split(','));
            addItemBtn();
        }
    });
}
  
function showEditMaruza(items){
    let form_block = document.querySelectorAll('.form_block input');
    form_block[1].value = items[0]
    form_block[2].value = items[1]
}