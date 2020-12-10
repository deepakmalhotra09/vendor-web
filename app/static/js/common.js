var base_url = window.location.origin;
var csrftoken = getCookie('csrftoken');

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

$('#page_form').submit(function() {
        var form_data = JSON.stringify($('#page_form').serializeObject());
        var method_name = $('#form_method_name').val();
        var list_slug = $('#list_slug').val();
        url = base_url+'/ajax/'+method_name;
        $.ajax({
          type: "POST",
          url: url,
          dataType: 'json',
          data: {data: form_data},
          success: function(data, status){
            if(status == 'success'){
                window.location = '/'+list_slug;
            }
          }
        });
        return false;
});

$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

$(document).ready(function(){

$('.datepicker').datepicker({
//    startDate: '-3d',
    autoclose: true,
    calendarWeeks: false,
    todayHighlight: true
});

$( ".country_list" ).change(function() {
  var optionSelected = $("option:selected", this);
  var country_code = optionSelected.attr('code');
  $('.country_code').val(country_code);
});

$( "#project_client_id" ).change(function() {
  var optionSelected = $("option:selected", this);
  var client_id = optionSelected.attr('client_id');
  $('.project_client_id').val(client_id);
});

$('.project_assignee_form #project').change(function(){
    var optionSelected = $("option:selected", this);
    var project_id = optionSelected.attr('project_id');
    $('.project_assignee_form .project_id').val(project_id);
});

$('.project_assignee_form #vendor').change(function(){
    var optionSelected = $("option:selected", this);
    var vendor_id = optionSelected.attr('vendor_id');
    $('.project_assignee_form .vendor_id').val(vendor_id);
});


//$("[data-country=append]").each(function(index, element){
//    url = base_url+'/ajax/get_countries';
//    $.ajax({
//      type: "POST",
//      url: url,
//      dataType: 'json',
//      success: function(data, status){
//        var option_html = ''
//        $.each(data, function(index, value){
//            option_html += "<option code='"+value.code+"'>"+value.name+"</option>"
//        });
//        $(element).append(option_html)
//      }
//    });
//});

$(document).on('click','.company_details_c_b',function(){
    $('.company_details').toggleClass('d-none');
});

$(document).on('click','.delete_record',function(){
    var id = $(this).data('id');
    var method_name = $(this).data('method-name');
    var url = base_url+'/ajax/'+method_name;
    $.ajax({
      type: "POST",
      url: url,
      data: {id: id},
      success: function(data, status){
        window.location.reload();
      }
    });
})
$('#dataTable').DataTable({
    buttons: [
        'copy', 'excel', 'pdf'
    ]
    });
});