document.addEventListener("DOMContentLoaded",
    function () {
        const elm = document.getElementById('main');
        const childcount = elm.childElementCount;

        for ( let i = 1; i < childcount; i++) {
            let a = String(i) + String(i) + "1"
            let blank = document.getElementById(a)
            blank.classList.replace('plus','trp')
        }
})

document.addEventListener("DOMContentLoaded",
    function () {
        const elm = document.getElementById('kakemain');
        const childcount = elm.childElementCount;
        for (let j = 1; j < childcount; j++) {
            for ( let i = 1; i < 11; i++) {
                let b = String(j) + String(i);
                 let kakeblank = document.getElementById("kakeans"+ b);
                 let kakeplusA = document.getElementById("kakeplusA"+ b);
                 let kakeplusB = document.getElementById("kakeplusB"+ b);
                 if (kakeblank.innerText.indexOf('a') == 0) {
                    kakeblank.innerText = kakeblank.innerText.replace('a','')
                    kakeplusA.classList.replace('kakeplus','kaketrp')
                     }
                if (kakeblank.innerText.indexOf('b') == 0) {
                    kakeblank.innerText = kakeblank.innerText.replace('b','')
                    kakeplusB.classList.replace('kakeplus','kaketrp')
                        }
                }
            }})

document.addEventListener("DOMContentLoaded",
function () {
const elm = document.getElementById('warimain');
const childcount = elm.childElementCount;
for (let j = 1; j < childcount; j++) {
    for ( let i = 1; i < 11; i++) {
        let b = String(j) + String(i);
            let wariblank = document.getElementById("warians"+ b);
            let wariplusA = document.getElementById("wariplusA"+ b);
            let wariplusB = document.getElementById("wariplusB"+ b);
            if (wariblank.innerText.indexOf('a') == 0) {
            wariblank.innerText = wariblank.innerText.replace('a','')
            wariplusA.classList.replace('wariplus','waritrp')
                }
        if (wariblank.innerText.indexOf('b') == 0) {
            wariblank.innerText = wariblank.innerText.replace('b','')
            wariplusB.classList.replace('wariplus','waritrp')
                }
        }
    }})


document.getElementById("warizanbottun").addEventListener("click",
    function(e) {
        e.preventDefault();
        let ed = document.getElementById("id_warieddigit")
        let ing = document.getElementById("id_wariingdigit")
        let edjudge =ed.selectedIndex
        let ingjudge =ing.selectedIndex
        if (edjudge < ingjudge) {
            alert("わる数はわられる数より小さい値を入力してください");
        }
        else {
            document.form1.submit();
        }
    })
//document.getElementById('1').innerText = 'a'+
