$(document).ready(function () {
     var controls = {
        video: $("#myVideo"),
        video2: $("#myVideo2"),
        video3: $("#myVideo3"),
        video4: $("#myVideo4"),
        video5: $("#myVideo5"),
        video6: $("#myVideo6"),
        playpause: $("#playpause"),                 
        playpause2: $("#playpause2"),                 
        playpause3: $("#playpause3"),                 
        playpause4: $("#playpause4"),                 
        playpause5: $("#playpause5"),                
        playpause6: $("#playpause6")                 
    };
                
    var video = controls.video[0];
    var video2 = controls.video2[0];
    var video3 = controls.video3[0];
    var video4 = controls.video4[0];
    var video5 = controls.video5[0];
    var video6 = controls.video6[0];
               
    controls.playpause.click(function(){
        if (video.paused) {
            video.play();
            $(this).css({'opacity': '0'});
            $("#.full").css({'height':'193'});
        } else {
            video.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused");
        
    });

        controls.playpause2.click(function(){
        if (video2.paused) {
            video2.play();
            $(this).css({'opacity': '0'});    
        } else {
            video2.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused2"); 
    });
    controls.playpause3.click(function(){
        if (video3.paused) {
            video3.play();
            $(this).css({'opacity': '0'});    
        } else {
            video3.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused3"); 
    });
    controls.playpause4.click(function(){
        if (video4.paused) {
            video4.play();
            $(this).css({'opacity': '0'});    
        } else {
            video4.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused4"); 
    });
    controls.playpause5.click(function(){
        if (video5.paused) {
            video5.play();
            $(this).css({'opacity': '0'});    
        } else {
            video5.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused5"); 
    });
    controls.playpause6.click(function(){
        if (video6.paused) {
            video6.play();
            $(this).css({'opacity': '0'});    
        } else {
            video6.pause();
             $(this).css({'opacity': '1'}); 
        }
                
        $(this).toggleClass("paused6"); 
    });
});