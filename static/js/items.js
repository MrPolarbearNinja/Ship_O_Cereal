$(document).ready(function () {
    $('#search-btn').on ('click', function (e) {
       e.preventDefault();
       var search_text = $('#search-box').val();
       $.ajax({
           url: '/catalog?search_filt=' + search_text,
           type: 'GET',
           success: function (resp) {
               var new_html = resp.data.map(d => {
               });
               $('.cat-list').html(new_html.join(''));
               $('search-box').val('')
           },
           error: function (xhr, status, error){
               console.error(error)
           }
       })
    });
});
