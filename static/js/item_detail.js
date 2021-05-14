function inc_qty () {
    var qty = document.getElementById("itemdet-qty-curr");
    var max_qty = document.getElementById("itemdet-stock-quant");
    var number = qty.innerHTML;
    if (number != max_qty.innerHTML && max_qty.innerHTML != '0' ) {
        number++;
        qty.innerHTML = number;
    }
}

function dec_qty () {
    var qty = document.getElementById("itemdet-qty-curr");
    var number = qty.innerHTML;
    if (number > 1) {
        number--;
        qty.innerHTML = number;
    }
}

function add_to_basket(item_id) {
    /* Get number from add-to-basket button */
    var qty = document.getElementById("itemdet-qty-curr");
    var number = qty.innerHTML;

    window.location.href = 'basket/' + item_id + '/' + number
}