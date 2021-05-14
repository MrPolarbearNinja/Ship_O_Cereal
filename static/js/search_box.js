function search_items(event, order_by = ''){
    var namne = document.getElementById("cat-search-box").value
    var type = ''
    var radios = document.getElementsByName('type-radio');

    for (var i = 0, length = radios.length; i < length; i++) {
      if (radios[i].checked) {
          type = radios[i].value
          break;
      }
    }

    var query_ar = []
    if (namne != '')
        query_ar.push("search_filter=" + namne)
    if (type != '')
        query_ar.push("search_type=" + type)
    if (order_by != '')
        query_ar.push(order_by)

    var my_url = "/?"
    var i;
    for (i = 0; i < query_ar.length; i++) {
        my_url += query_ar[i] + "&"
    }

    my_url = my_url.slice(0, -1)

    window.location.href = my_url
    event.preventDefault()
}

function sort_by_name_func(event) {
    search_items(event, 'sort_by_name=1')
}

function sort_by_price_func(event) {
    search_items(event, 'sort_by_price=1')
}
