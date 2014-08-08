var up = true;
var y = window.innerHeight;
var x = 0;
var t = 0;
var d = 10;

$(document).ready(function() {
    animate_flappy();

    $('.message').on('click',function() {
        window.location = '/';
    });
});

function animate_flappy() {

    $('.flappy').animate({
        top:y+'px',
        left:x+'px',
    },t, function() {
        x += 30 - 10*(y/window.innerHeight);
        if(up) {
            y += 40;
            t -= d;
        } else {
            y -= 40;
            t += d;
        }

        if(y>window.innerHeight-300) up = false
        if(y<100) up = true

        if(x>=$('.pipeline').offset().left) {
            $('.flappy').css({'left':'0px'});
            x = 0;
        }

        animate_flappy();
    });
}