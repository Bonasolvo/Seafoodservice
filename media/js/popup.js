$(document).ready(function () {
    $(".photo_img img").click(function () {
        $("#wrap_frame, #overlay").fadeIn();
    });
    $("#overlay, #close2").click(function () {
        $("#wrap_frame, #overlay").fadeOut();
    });
      positionCenter($("#wrap_frame"));
    
    var licount=$(".photo_img").length;
$("#wrapper .photo_img").each(function() {
    licount++;
    $(this).attr('rel',licount);
});

  var current_li=0;
$(".portfolio li img").click(function () {
    var src = $(this).attr("src");
    current_li = parseInt($(this).parent().attr('rel'));
    var cur_desc = $("li[rel="+current_li+"]").find(".photo_descr").html();
    $(".description").html(cur_desc);
    $("#big_photo_img").attr("src", src);
    $("#wrap_frame, #overlay, .description").fadeIn();
     
});
    $("#right_arrow").click(function() {
    if(current_li<licount)
	{
	    var next_li = parseInt(current_li)+1;
	    var cur_src = $("li[rel="+current_li+"]").find("img").attr("src");
	    var next_src = $("li[rel="+next_li+"]").find("img").attr("src");
	    var cur_desc = $("li[rel="+next_li+"]").find(".photo_descr").html();
	    $(".description").html(cur_desc);
	    $("#frame #big_photo_img").attr("src", next_src);
	    current_li = next_li;
        $("#overlay, #wrap_frame, .description").fadeIn();
	}
 });
    $("#left_arrow").click(function() {
    if(current_li>1)
	{
	    var prev_li = parseInt(current_li)-1;
	    var cur_src = $("li[rel="+current_li+"]").find("img").attr("src");
	    var prev_src = $("li[rel="+prev_li+"]").find("img").attr("src");
	    var cur_desc = $("li[rel="+prev_li+"]").find(".photo_descr").html();
	    $(".description").html(cur_desc);
	    $("#frame #big_photo_img").attr("src", prev_src);
	    current_li = prev_li;
        $("#overlay, #wrap_frame, .description").fadeIn();
	}
    });
    
$("#overlay, #close2").click(function () {
    $("#overlay, #wrap_frame, .description").fadeOut();
});   
    
    function positionCenter(elem) {
    elem.css({
    marginTop: '-' + elem.height() /2 + 'px',
    marginLeft: '-' + elem.width() /2 + 'px'
    });
    }
    
    
    
    $(".sertif img").click(function () {
    //$("#wrap_frame2, #overlay").fadeIn(300);
    });
    $("#overlay, #close").click(function () {
      $("#wrap_frame2, #overlay").fadeOut();
    });
      positionCenter($("#wrap_frame2"));
    
    var licount2=$(".sertif").length;
$("#wrapper .sertif").each(function() {
    licount2++;
    $(this).attr('rel',licount2);
});

  var current_li2=0;
 $(".sertif_portfolio li img").click(function () {
    var src = $(this).attr("src");
    current_li2 = parseInt($(this).parent().attr('rel'));
    var cur_desc = $("li[rel="+current_li2+"]").find(".sertif_descr").html();
    $(".description2").html(cur_desc);
    $("#big_photo_img").attr("src", src);
    //$("#wrap_frame2, #overlay, .description2").fadeIn();
     
});
    $("#right_arrow_sertif").click(function() {
    if(current_li2<licount2)
	{
	    var next_li2 = parseInt(current_li2)+1;
	    var cur_src2 = $("li[rel="+current_li2+"]").find("img").attr("src");
	    var next_src2 = $("li[rel="+next_li2+"]").find("img").attr("src");
	    var cur_desc2 = $("li[rel="+next_li2+"]").find(".sertif_descr").html();
	    //$(".description2").fadeToggle("300");
	    $(".description2").html(cur_desc2);
	    //$("#frame2").fadeToggle("300");
	    $("#frame2 #big_photo_img").attr("src", next_src2);
	    //$("#frame2").fadeToggle("300");
	    //$(".description2").fadeToggle("300");
	    current_li2 = next_li2;
	}
 });
    $("#left_arrow_sertif").click(function() {
    if(current_li2>1)
	{
	    var prev_li2 = parseInt(current_li2)-1;
	    var cur_src2 = $("li[rel="+current_li2+"]").find("img").attr("src");
	    var prev_src2 = $("li[rel="+prev_li2+"]").find("img").attr("src");
	    var cur_desc2 = $("li[rel="+prev_li2+"]").find(".sertif_descr").html();
	    //$(".description2").fadeToggle("300");
	    $(".description2").html(cur_desc2);
	    //$("#frame2").fadeToggle("300");
	    $("#frame2 #big_photo_img").attr("src", prev_src2);
	    //$("#frame2").fadeToggle("300");
	    //$(".description2").fadeToggle("300");
	    current_li2 = prev_li2;
	}
    });
    
$("#overlay, #close").click(function () {
$("#overlay, #wrap_frame2, .description2").fadeOut();
});   
    
    function positionCenter(elem) {
    elem.css({
    marginTop: '-' + elem.height() /2 + 'px',
    marginLeft: '-' + elem.width() /2 + 'px'
    });
    }
});


