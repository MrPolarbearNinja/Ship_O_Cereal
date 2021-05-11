
function inc_qty () {
    var qty = document.getElementById("itemdet-qty-curr");
    var number = qty.innerHTML;
    if (number != 9) {
        number++;
        qty.innerHTML = number;
    }
}

function dec_qty () {
    var qty = document.getElementById("itemdet-qty-curr");
    var number = qty.innerHTML;
    if (number != 0) {
        number--;
        qty.innerHTML = number;
    }
}

function add_to_basket() {
    /* Get number from add-to-basket button */
    var qty = document.getElementById("itemdet-qty-curr");
    var number = qty.innerHTML;

    /*INSERT GET QTY FROM BASKET THEN ADD TO CURRENT QTY*/
    /*GET CURRENT QTY IN BASKET AND CHANGE NUMBER ON ICON*/
    /*CHECK STOCK STATUS*/

    /* Get current basket qty */
    var bask_qty = document.getElementById("bask-qty");

    /* Change values */
    var new_qty = Number(number) + Number(bask_qty.innerHTML);
    bask_qty.innerHTML = new_qty
    qty.innerHTML = 0;
}