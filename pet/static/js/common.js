// 참고문서
// https://code.i-harness.com/ko/q/196711
// http://htmlcheats.com/html/resize-the-html5-canvas-dyamically/
// https://www.html5rocks.com/en/tutorials/casestudies/gopherwoord-studios-resizing-html5-games/
// https://www.matthewdawkins.co.uk/2016/07/animated-star-field-javascript-canvas/
(function() {
    var bgCanvas = document.getElementById('bg'),
    ctx = bgCanvas.getContext('2d');
    // 이벤트 크기 조정 및 캔버스 그리기를 시작.
    init();
    function init() {
        // resizeCanvas () 함수를 호출하는 이벤트 리스너 등록. *on resize: 개체의 크기가 바뀔 때 발생.
        window.addEventListener('resize', resizeCanvas, false);
        resizeCanvas();
    }

    function orangeSky() {
        // x0 Gradient 시작점의 x 좌표
        // y0 Gradient 시작점의 y 좌표
        // x1 Gradient 끝점의 x 좌표
        // y1 Gradient 끝점의 y 좌표
        var grd = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        grd.addColorStop(0, '#ffa600');
        grd.addColorStop(1, '#ff5100');
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    }
    
    function blueSky() {
        var grd = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        grd.addColorStop(0, '#bff5ff');
        grd.addColorStop(1, '#30c1e6');
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    }
    
    function navySky() {
        var grd = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        grd.addColorStop(0, '#2d4db4');
        grd.addColorStop(1, '#0f0f33');
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    }
    // DOM 윈도우 크기 조절 이벤트가 발생할 때마다 실행.
    function resizeCanvas() {
        bgCanvas.width = window.innerWidth;
        bgCanvas.height = window.innerHeight
        var times = new Date();
        switch (times.getHours()) {
            // Sunrise & Sunset
            case 05:
            case 06:
            case 07:
            case 17:
            case 18:
            case 19:
                orangeSky();
                break
            // night
            case 19:
            case 20:
            case 21:
            case 22:
            case 23:
            case 24:
            case 01:
            case 02:
            case 03:
            case 04:
                navySky();
                break
            // blueSky
            default:
                blueSky();        
        }
    }
})();