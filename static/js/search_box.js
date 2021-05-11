


function search_items(event){
    var query = document.getElementById("search-box").value
    var type = ''
    var radios = document.getElementsByName('type-radio');

    for (var i = 0, length = radios.length; i < length; i++) {
      if (radios[i].checked) {
          type = radios[i].value
          break;
      }
    }
    console.log("Hello")
    var my_url = ''
    if (query != '') {
        my_url += "/?search_filter=" + query
        if (type != '')
            my_url += "&search_type=" + type
    }
    else if (query == '' && type != '')
        my_url += "/?search_type=" + type
    window.location.href = my_url

    event.preventDefault()

  }