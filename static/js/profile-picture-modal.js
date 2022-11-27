const image_input = document.querySelector("#image-input");

image_input.addEventListener("change", function() {

    const reader = new FileReader();
    
    reader.addEventListener("load", () => {
        const uploaded_image = reader.result;
        document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
    });
    reader.readAsDataURL(this.files[0]);
});


$(function () {
    $('.user_profile_btn').click(function(){
        $(".hide_btn").hide("fast");
        $(".profilePictureModal").show("slow");

        //scroll disabled
        $('html, body').css({
            overflow: 'hidden',
            height: '100%'
        });
        })

    $('.modal_close').click(function(){
        $(".hide_btn").show("fast");
        $(".profilePictureModal").hide("slow");
        
        //scroll restore
        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    })

}); 