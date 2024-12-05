console.log("hello world!");
var angle = 0;

var a = window.Telegram.WebApp;

const gameStart = (btn_color) => {
    var cells_container = document.getElementById("cells_container");
    var ncell = Math.trunc(Math.random() * 100);
    var user_balance = document.getElementById("user_balance").textContent;
    var user_bet = document.getElementById("bet-enter").textContent;
    var log = document.getElementById("log");

    let searchParams = window.location.search.substr(1).split('&');
    let queryParams = {};
    for (let param of searchParams) {
        let [key, value] = param.split('=');
        queryParams[key] = decodeURIComponent(value || "");
    }

    const tgid = parseInt(queryParams.tg_id);

    console.log(user_bet);
    console.log(user_balance);


    if (parseInt(user_bet) > parseInt(user_balance)){
        log.style.color = "#fff";
        log.style.color = "#9c1b1b";
        log.textContent = "TOO BIG BET!";
    }
    else if (parseInt(user_bet) == 0){
        log.style.color = "#fff";
        log.style.color = "#9c1b1b";
        log.textContent = "CAN'T BET 0!";
    }
    else{
        document.getElementById("user_balance").textContent = parseInt(user_balance) - parseInt(user_bet); 
        document.getElementById("bt-red").disabled = true;
        document.getElementById("bt-green").disabled = true;
        document.getElementById("bt-white").disabled = true;
        document.getElementById("bt-black").disabled = true;
        cells_container.style.transition = '4s';

        ncell %= 40;
        angle = (360 + ncell * 9);
        cells_container.style.transform = 'rotate(' + String(angle) + 'deg)';
        ncell ++;
        
        if (ncell == 1){
            b = "green";
        }
        else if (ncell == 12 || ncell == 32 || ncell == 21){
            b = "white";
        }
        else if (ncell % 2 == 0) { 
            b = "black";
        }
        else {
            b = "red";
        }

        const request = fetch(`https://d24e-94-137-3-176.ngrok-free.app/page/dbrequest/?tgid=${tgid}&usr_bet=${user_bet}&usr_btn=${btn_color}&game_res=${b}`).then(
            console.log(request)
        );

        if ((btn_color == 1 && b == "red") || 
            (btn_color == 2 && b == "black") ||
            (btn_color == 3 && b == "white") ||
            (btn_color == 4 && b == "green") ){
            setTimeout(() => {
                log.style.color = "#fff";
                log.style.color = "#06681e";
                log.textContent = "WIN!";
                switch(b){
                    case 'red': 
                    case 'black':
                        var a = parseInt(user_bet) + parseInt(user_balance);
                        document.getElementById("user_balance").textContent = a;
                        break;
                    case 'white':
                        var a = parseInt(user_bet) * 4 + parseInt(user_balance);
                        document.getElementById("user_balance").textContent = a;
                        break;
                    case 'green':
                        var a = parseInt(user_bet) * 9 + parseInt(user_balance);
                        document.getElementById("user_balance").textContent = a;
                        break;
                }
            }, 3800)
        }
        else {
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
