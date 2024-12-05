document.addEventListener("DOMContentLoaded", function() {
    // Simulate missing product name in product 2
    const productName2 = document.getElementById("name-2");
    if (!productName2.innerText) {
        console.error("Product name missing for Product 2");
    }

    // Simulate missing product price in product 3
    const productPrice3 = document.getElementById("price-3");
    if (!productPrice3.innerText) {
        console.error("Product price missing for Product 3");
    }

    // Simulate broken image in product 1
    const productImg1 = document.getElementById("img-1");
    productImg1.onerror = function() {
        console.error("Broken image for Product 1");
    };

    // Simulate button click without price for product 3
    const buyButton3 = document.getElementById("buy-3");
    buyButton3.addEventListener("click", function() {
        if (!productPrice3.innerText) {
            console.error("Cannot buy Product 3 because the price is missing.");
            alert("Price is missing! Cannot proceed with purchase.");
        }
    });
});
