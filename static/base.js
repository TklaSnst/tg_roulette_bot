console.log("hello world!");
var angle = 0;

const gameStart = (btn_color) => {
    var cells_container = document.getElementById("cells_container");
    var ncell = Math.trunc(Math.random() * 100);
    var s = 0;
    var b;

    document.getElementById("bt-red").disabled = true;
    document.getElementById("bt-green").disabled = true;
    document.getElementById("bt-white").disabled = true;
    document.getElementById("bt-black").disabled = true;
    cells_container.style.transition = '4s';

    ncell %= 40;
    console.log(ncell);
    angle = (360 + ncell * 9);
    cells_container.style.transform = 'rotate(' + String(angle) + 'deg)';
    console.log(cells_container.style.transform);
    ncell ++;
    
    if (ncell == 1){
        b = "green";
        console.log("s-green");
    }
    else if (ncell == 12 || ncell == 32 || ncell == 21){
        b = "white";
        console.log("s-white");
    }
    else if (ncell % 2 == 0) { 
        b = "black";
        console.log("s-black");
    }
    else {
        b = "red";
        console.log("s-red");
    }

    var log = document.getElementById("log");

    if ((btn_color == 1 && b == "red") || 
        (btn_color == 2 && b == "black") ||
        (btn_color == 3 && b == "white") ||
        (btn_color == 4 && b == "green") 
    ){
        console.log("win!");
        setTimeout(() => {
            log.style.color = "#fff";
            log.style.color = "#06681e";
            log.textContent = "WIN!";
        }, 3800)
    }
    else {
        console.log("loose!");
        setTimeout(() => {
            log.style.color = "#fff";
            log.style.color = "#9c1b1b";
            log.textContent = "LOOSE!";
        }, 3800)
    }

    setTimeout(() => {
        cells_container.style.transition = '2s'
        cells_container.style.transform = 'rotate(0deg)';
    }, 8000) 

    setTimeout(() => {
        document.getElementById("bt-red").disabled = false;
        document.getElementById("bt-green").disabled = false;
        document.getElementById("bt-black").disabled = false;
        document.getElementById("bt-white").disabled = false;
    }, 10100);

}

/*
const changeText = () => {
    document.getElementById('text').textContent = "Button has been clicked!";
    var sq = document.getElementById("rectangle")
    angle += 1080
    console.log(angle)
    sq.style.transform = 'rotate(' + String(angle) + 'deg)';
    console.log(sq.style.transform);
}
*/
