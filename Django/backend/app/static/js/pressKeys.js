const form = document.getElementById('search-form');
document.getElementById('search').addEventListener('keypress', function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        form.submit();
    }
});
