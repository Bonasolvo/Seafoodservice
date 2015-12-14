function set_width_to_media_files() {
   set_width_to_images();
   set_width_to_video_files();
}

function set_width_to_images() {

    var width_of_media = parseInt(document.getElementById('photo_gallery').offsetWidth*(0.90) / 3);
    var photos = document.getElementsByClassName('img_in_gallery');
    for(var i=0; i<photos.length; i++){
        photos[i].width = width_of_media;
    }
}

function set_width_to_certificates() {

    var width_of_media = parseInt(document.getElementById('photo_gallery').offsetWidth*(0.90) / 3);
    var photos = document.getElementsByClassName('certificate_in_gallery');
    for(var i=0; i<photos.length; i++){
        photos[i].width = width_of_media;
    }
}
function set_width_to_video_files() {

    var width_of_media = parseInt(document.getElementById('video_gallery').offsetWidth*(0.90) / 3);
    var  videos = document.getElementsByTagName('video');


}

