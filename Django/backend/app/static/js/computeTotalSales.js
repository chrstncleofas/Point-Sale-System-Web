document.addEventListener("DOMContentLoaded", function() {
    // Function to calculate total amount
    function calculateTotalAmount() {
        var totalAmount = 0;
        var totalAmountCells = document.getElementsByClassName('totalAmount');
        for (var i = 0; i < totalAmountCells.length; i++) {
            totalAmount += parseFloat(totalAmountCells[i].innerText);
        }
        return totalAmount.toFixed(2);
    }

    // Function to update total amount display
    function updateTotalAmountDisplay() {
        var totalAmount = calculateTotalAmount();
        var totalAmountInput = document.getElementById('totalAmountDisplay');
        if(totalAmountInput) {
            totalAmountInput.value = totalAmount;
        }
    }

    // Call the update function when the page loads
    updateTotalAmountDisplay();
});