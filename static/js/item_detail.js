
function inc_qty () {
    var qty = document.getElementById("itemdet-qty-curr");
    var max_qty = document.getElementById("itemdet-stock-quant");
    var number = qty.innerHTML;
    if (number != max_qty.innerHTML) {
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

    /*INSERT GET QTY FROM BASKET THEN ADD TO CURRENT QTY*/
    /*GET CURRENT QTY IN BASKET AND CHANGE NUMBER ON ICON*/
    /*CHECK STOCK STATUS*/



    window.location.href = 'basket/' + item_id + '/' + number

}