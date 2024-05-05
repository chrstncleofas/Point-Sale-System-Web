const previewImage = async (input) => {
    const preview = document.getElementById('imagePreview');
    
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function (e) {
            preview.style.backgroundImage = `url('${e.target.result}')`;
        };
        
        reader.readAsDataURL(input.files[0]);
    } else {
        preview.style.backgroundImage = '';
    }
};

