document.addEventListener("DOMContentLoaded", function() {
    const formatCurrency = (value) => {
        return new Intl.NumberFormat('en-PH', {
            style: 'currency',
            currency: 'PHP',
        }).format(value);
    };

    // Selling Price
    const SPriceElements = document.querySelectorAll('#SPrice');
    SPriceElements.forEach(element => {
        const SPriceValue = element.textContent.replace(/[^0-9.-]+/g,"");
        element.textContent = formatCurrency(parseFloat(SPriceValue));
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const formatCurrency = (value) => {
        return new Intl.NumberFormat('en-PH', {
            style: 'currency',
            currency: 'PHP',
        }).format(value);
    };

    // Buying Price
    const SPriceElements = document.querySelectorAll('#BPrice');
    SPriceElements.forEach(element => {
        const SPriceValue = element.textContent.replace(/[^0-9.-]+/g,"");
        element.textContent = formatCurrency(parseFloat(SPriceValue));
    });
});
