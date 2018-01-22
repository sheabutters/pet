(function(){
    var bgCanvas = document.getElementById('bg'),
    ctx = bgCanvas.getContext('2d');
    // 이벤트 크기 조정 및 캔버스 그리기를 시작.
    init();
    function init(){
        // resizeCanvas() 함수를 호출하는 이벤트 리스너 등록. *on resize: 개체의 크기가 바뀔 때 발생.
        window.addEventListener('resize', resizeCanvas, false);
        resizeCanvas();
    }

    // DOM 윈도우 크기 조절 이벤트가 발생할 때마다 실행.
    function resizeCanvas(){
        bgCanvas.width = window.innerWidth;
        bgCanvas.height = window.innerHeight;
        var times = new Date();
        switch (times.getHours()){
            // Sunrise & Sunset
            case 05:
            case 06:
            case 07:
            case 17:
            case 18:
            case 19:
                sky('#ffb224', '#ff5100');
                ctx.fillStyle = '#ffedb6';
                break
            // Night
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
                sky('#556392', '#171841');
                ctx.fillStyle = '#bb67a6';
                break
            // BlueSky
            default:
                sky('#bff5ff', '#30c1e6');
                ctx.fillStyle = '#fff';    
        };
        // Random Clouds
        for (var i = 0; i < 15; i++){
            var randomX = Math.floor(Math.random() * 800),
                randomY = Math.floor(Math.random() * 100),
                randomS = Math.floor(Math.random() + 1.2),
                randomA = Math.floor(Math.random() + 0.4);
            cloud(randomX, randomY, randomA, randomS);
        };
    };

    // Background Gradient
    function sky(top, bottom){
        var grd = ctx.createLinearGradient(0, 0, 0, window.innerHeight);
        grd.addColorStop(0, top);
        grd.addColorStop(1, bottom);
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);        
    };
    
    // Base Cloud
    function cloud(x, y, angle, scale){
        ctx.beginPath();
        ctx.moveTo(x + 0, y + 140);
        ctx.lineTo(x + 0, y + 146);
        ctx.lineTo(x + 0, y + 159);
        ctx.lineTo(x + 28, y + 169);
        ctx.lineTo(x + 31, y + 174);
        ctx.lineTo(x + 50, y + 180);
        ctx.lineTo(x + 60, y + 180);
        ctx.lineTo(x + 90, y + 178);
        ctx.lineTo(x + 105, y + 170);
        ctx.lineTo(x + 110, y + 169);
        ctx.lineTo(x + 120, y + 168);
        ctx.lineTo(x + 130, y + 156);
        ctx.lineTo(x + 128, y + 140);
        ctx.lineTo(x + 120, y + 131);
        ctx.lineTo(x + 104, y + 132);
        ctx.lineTo(x + 94, y + 126);
        ctx.lineTo(x + 90, y + 118);
        ctx.lineTo(x + 59, y + 100);
        ctx.lineTo(x + 38, y + 110);
        ctx.lineTo(x + 28, y + 128);
        ctx.lineTo(x + 11, y + 127);
        ctx.fill();
        ctx.scale(scale, scale);
    };
})();