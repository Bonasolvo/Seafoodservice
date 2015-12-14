$(document).ready(function () {
	var slides = [];
	var controls = [];
	var currentImage = 0;
    var control;
    var div_controls = $("#controls");
    $("div .slide").each(function(index, element) {
        slides.push($(element).find("img").attr('src'));
        d=document.createElement('div');
        if(index==0){
            $(d).addClass("active_control");
        }
        $(div_controls).append($(d));
        controls.push($(d));
    });
  
$(".right").click(listRight);
$(".left").click(listLeft);
    
function listLeft(){
    if(currentImage != 0) {
        currentImage--;
        changeControls(currentImage);
    }
    else{
        currentImage = slides.length-1;
        changeControls(currentImage);   
    }
}

function listRight(){
        if(currentImage != slides.length-1) {
        currentImage++;
        changeControls(currentImage);
    }
    else{
        currentImage = 0;
        changeControls(currentImage);   
    }
}

function changeControls(number){
    for	(var index = 0; index < controls.length; index++) {
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
    $("#img").attr("src", slides[currentImage]);
    }, 10);
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
	alert("PreloadImages()"+arguments);
  for(var i = 0; i<arguments.length; i++)
    {
	$("<img />").attr("src", arguments);
    }
} 
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