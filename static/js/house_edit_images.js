$(document).ready(function(){
    $('#id_image').change(function(e){
        var images = e.target.files;

        console.log(images);
        for (index in images) {
            if (images[index] instanceof File) {
                var reader = new FileReader();
                // Closure to capture the file information.
                reader.onload = (function (theFile) {
                    return function (e) {
                        // Render thumbnail.
                        var r = $('#house-images-board');
                        r.after('<img src="' + e.target.result + '" class="house-image img-fluid">');
                    };
                })(images[index]);
                // Read in the image file as a data URL.
                reader.readAsDataURL(images[index]);
            }
        }
    });
});