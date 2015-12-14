$(document).ready(function () {
var currentImage = 0;
preloadImages ("images/slide1.png",
           "images/slide2.png",
           "images/slide3.png",
           "images/slide4.png",
            "images/video.mp4",
            "images/video.ogg",
            "images/video.webM");
    
var images = ["images/slide1.png",
           "images/slide2.png",
           "images/slide3.png",
           "images/slide4.png"
          ];
var controls = ["#first_control",
           "#second_control",
           "#third_control",
           "#fourth_control",
           "#fifth_control",
           "#sixth_control"
          ];
changeControls(currentImage);
    
$("#first_control").click(function () {
    changeControls(0);
});    
$("#second_control").click(function () {
    changeControls(1);
});    
$("#third_control").click(function () {
    changeControls(2);
});
$("#fourth_control").click(function () {
    changeControls(3);
});
$("#fifth_control").click(function () {
    changeControls(4);
});
$("#sixth_control").click(function () {
    changeControls(5);
});
    
$(".right").click(listRight);
$(".left").click(listLeft);
    
function listLeft(){
    if(currentImage != 0) {
        currentImage--;
        changeControls(currentImage);
    }
    else{
        currentImage = images.length-1;
        changeControls(currentImage);   
    }
}

function listRight(){
        if(currentImage != images.length-1) {
        currentImage++;
        changeControls(currentImage);
    }
    else{
        currentImage = 0;
        changeControls(currentImage);   
    }
}

function changeControls(number){
    var index;
    for	(index = 0; index < controls.length; index++) {
        if(index != number){
            $(controls[index]).removeClass('active_control');    
        }
        else{
            $(controls[index]).addClass('active_control');
            currentImage = index;
            changeImage();
        }
    }    
}
      
function changeImage(){
    $("#img").fadeToggle("fast");
    setTimeout(function() {
    $("#img").attr("src", images[currentImage]);
    }, 200);
    $("#img").fadeToggle("fast");
}

var delay = 7000;
setTimeout(startSlider,delay);
    
function startSlider(){
    listRight();
    setTimeout(startSlider,delay);
}
function preloadImages()
{
  for(var i = 0; i<arguments.length; i++)
    {
	$("<img />").attr("src", arguments);
    }
}
    
    //--review-slider--//   
    var animationSpeed = 1000;
    var currentLogoSlide = 3;
    var $carousel_Slides = $(".carousel_slides");
        
    $(".logo_right").click(function() {
        if(currentLogoSlide != $carousel_Slides.length){
            currentLogoSlide += 3;
            $("#carousel_slides").animate({'margin-left': '-=633'}, animationSpeed);
        }
        else{
            currentLogoSlide = 3;
            $("#carousel_slides").animate({'margin-left': '0'}, animationSpeed);
        }
        
    });
    
    $(".logo_left").click(function() {
        if(currentLogoSlide != 3){
             currentLogoSlide -= 3;
            $("#carousel_slides").animate({'margin-left': '+=633'}, animationSpeed);
        }
        else{
            currentLogoSlide = 3;
             $("#carousel_slides").animate({'margin-left': '0'}, animationSpeed);
        }
    });
    

});