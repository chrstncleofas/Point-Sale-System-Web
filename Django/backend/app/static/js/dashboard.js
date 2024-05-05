document.addEventListener("DOMContentLoaded", function() {
    const formatCurrency = (value) => {
        return new Intl.NumberFormat('en-PH', {
            style: 'currency',
            currency: 'PHP',
        }).format(value);
    };
    const monthlySalesElement = document.getElementById('monthly-sales');
    const monthlySalesValue = monthlySalesElement.textContent.replace(/[^0-9.-]+/g,"");
    monthlySalesElement.textContent = formatCurrency(parseFloat(monthlySalesValue));
});