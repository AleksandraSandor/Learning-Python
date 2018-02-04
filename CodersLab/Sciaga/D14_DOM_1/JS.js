document.querySelector("div.ban.article");//todo TAG + CLASSNAME i po ID tez np:<div class="ban article">  # jest po ID . jest po class
document.querySelectorAll("div.ban.article");//todo TAG + CLASSNAME np:<div class="ban article">
document.getElementsByClassName("block");//todo CLASSNAME np:<div class="blocks">
document.getElementById("home");//todo ID np: <header id="home">

document.classList; //todo zwraca tabele calss, dodanije nie nadpisuje
    // document.classList.add("nazwa_klasy");
    // document.classList.remove("nazwa_klasy");
    // document.classList.toggle("nazwa_klasy");
document.className; //todo zwraca "stringa"
//todo pomoższe można też ustawiać
document.id;        //todo zwraca stringa
document.innerHTML; //todo zwraca stringa razem z TAGami
document.outerHTML; //todo zwraca stringa razem z zewnetrzymi TAGami
document.innerText; //todo zwraca stringa z samym txt
document.tagName;   //todo zwraca stringa
document.dataset;   //todo zwraca to co w html jest ustawione przy data

// element.style.background
// element.style.fontSize
// element.style.padding

// console.log(link.hasAttribute("href")); //todo zwraca boolen czy jest taki atrybut
// console.log(link.getAttribute("href")); //todo zwraca wartość atrybuty
// link.removeAttribute("data-user");      //todo usuwa podany atrybut
// link.setAttribute("data-ser", "nowy data set"); //todo ustawia nowy atrybut i wartosc

//todo    <a	data-user="daadsasd" href="www.google.com"	id="glink123" class="topMenu" >
//todo   TAG    ATRYBUT    WARTOŚĆ   ATR.   WAR.            ID              className

//todo --------------------------EVENTY
// button[0].addEventListener("click", function (event) {});
// function clickLicznik(event) {};
//-------------------------------
// function klikniecie(event) {};
// var button3 = document.getElementById("counter3");
// button3.addEventListener("click", klikniecie);
//-------------------------------
// function func_klik (event) {
//     this.removeEventListener("click", func_klik)}

// var foo = document.querySelector("#foo");
//     foo.addEventListener("click", function (e) {
//         console.log("------------")
//         console.log("Target:", e.target.id);
//         console.log("CurrentTarget:", e.currentTarget.id);
//         console.log("TimeStamp:", e.timeStamp);
//         console.log("Type:", e.type);
//         console.log("PreventDefault:", e.preventDefault);
//         console.log("StopPropagation:", e.stopPropagation);
//         console.log("StopImmediatePropagation:", e.stopImmediatePropagation());
//         console.log("Button:", e.button);
//         console.log("ClientX:", e.clientX);
//         console.log("ClientY:", e.clientY);
//         console.log("ScreenX:", e.screenX);
//         console.log("ScreenY:", e.screenY);
//         //są jeszcze event.altKay, ctrlKey, shiftKey, key, code










document.addEventListener("DOMContentLoaded", function() {
    var test = document.querySelector("div.ban.article"); //todo TAG + CLASSNAME np:<div class="ban article">
    console.log(test);
    console.log("------------");
    var test = document.querySelectorAll("div.ban.article");//todo TAG + CLASSNAME np:<div class="ban article">
    console.log(test);
    console.log(test[0]);
    console.log("------------");
    var test = document.getElementsByClassName("block");//todo CLASSNAME np:<div class="blocks">
    console.log(test);
    console.log(test[0]);
    console.log(test[1]);
    console.log(test[2]);
    console.log("------------");
    var test = document.getElementById("home");//todo ID np: <header id="home">
    console.log(test);
    console.log("------------");
    var test2 = test.getElementsByClassName("block");
    console.log(test2);
    console.log(test2[0]);
    console.log(test2[1]);
    console.log(test2[2]);
    console.log("------------");

    var test = document.getElementById("glink");
    test.className = "topMenu";
    console.log(test.className);

    console.log("------------");
    var czyt_id = document.getElementById("glink");
    czyt_id.id = 'nowe';
    console.log(czyt_id.id);

    console.log("------------");
    var czyt_id = document.getElementsByClassName("block");
    console.log(czyt_id[0].outerHTML);
    console.log(czyt_id[0].innerHTML);
    console.log(czyt_id[0].tagName);
    console.log(czyt_id[0].dataset);
    // console.log(czyt_id);

    var strona = document.querySelector("div.ban.article");
    strona.style.backgroundColor = "blue";
    console.log(strona);

    var strona = document.getElementById("myDiv666");
    console.log(strona.classList);
    console.log(strona.className);
    strona.classList.add("testtowannnie");
    console.log(strona.classList);
    strona.classList.remove("testtowannnie");
    console.log(strona.classList);

    var strona = document.getElementById("user");
    console.log(strona);
    var strona = document.querySelector("#user");
    console.log(strona);
    console.log(strona.dataset);
    console.log(strona.dataset.id);
    console.log(strona.dataset.user);
    console.log(strona.dataset.dateOfBirth);
    strona.dataset.dateOfBirth = "99.99.9999";
    console.log(strona.dataset.dateOfBirth);
    strona.dataset.Nowy = "NOWY_Dataset";
    console.log(strona.dataset);

    var	link = document.querySelector("#glink123");
    console.log(link);
    console.log("------------");
    console.log(link.hasAttribute("href"));
    console.log(link.getAttribute("href"));
    link.removeAttribute("data-user");
    console.log(link);
    link.setAttribute("data-ser", "nowy data set");
    console.log(link);
//todo --------------------------EVENTY
    var button = document.querySelectorAll("button");
    var clickCount1 = 0;
    var clickCount2 = 0;
    button[0].addEventListener("click", function (event) {
        document.getElementById("randomW").removeEventListener("click", func_klik);
        clickCount1 += 1;
        console.log("Kliknąłem 1 guzik ", clickCount1, " razy.");
    })
    button[1].addEventListener("click", function (event) {
        clickCount2 += 1;
        console.log("Kliknąłem 2 guzik ", clickCount2, " razy.");
    })


    var clickCount3 = 0;
    function klikniecie(event) {
        clickCount3 += 1;
        console.log("Drugim sposobem klik ", clickCount3, " razy.");
    };
    var button3 = document.querySelectorAll("button");
    button3[2].addEventListener("click", klikniecie);

    var button = document.getElementById("randomW");
    var licznik = 0;
    var slowa = ["Pierwsze", "Drugie", "Trzecie"];
    button.addEventListener("click", func_klik)
    function func_klik (event) {
        licznik += 1;
        // if (licznik == 3){
        //     this.removeEventListener("click", func_klik)
        // }
        var myWord = slowa[Math.floor(Math.random() * slowa.length)];
        console.log("Licznik: ", licznik, " Słowo: ", myWord);
    }

    var buttons = document.querySelectorAll(".btn");
    for(var i = 0; i < buttons.length; i++){
        buttons[i].addEventListener("click", function (event) {
            this.style.backgroundColor = "red";
        })
    }

    var foo = document.querySelector("#foo");
    var bar = document.querySelector("#bar");
    foo.addEventListener("click", function () {
        console.log("Wywołany element #foo")
    })
    bar.addEventListener("click", function () {
        console.log("Wywołany element #bar")
    })

    var foo = document.querySelector("#foo");
    foo.addEventListener("click", function (e) {
        console.log("------------")
        console.log("Target:", e.target.id);
        console.log("CurrentTarget:", e.currentTarget.id);
        console.log("TimeStamp:", e.timeStamp);
        console.log("Type:", e.type);
        console.log("PreventDefault:", e.preventDefault);
        console.log("StopPropagation:", e.stopPropagation);
        console.log("StopImmediatePropagation:", e.stopImmediatePropagation());
        console.log("Button:", e.button);
        console.log("ClientX:", e.clientX);
        console.log("ClientY:", e.clientY);
        console.log("ScreenX:", e.screenX);
        console.log("ScreenY:", e.screenY);
        //są jeszcze event.altKay, ctrlKey, shiftKey, key, code

    var foo = document.querySelector("#foo");
    var bar = document.querySelector("#bar");
    var baz = document.querySelector("#baz");

    foo.addEventListener("click", function (e) {
        console.log("klik na #foo");
    });
    bar.addEventListener("click", function (e) {
        console.log("klik na #bar");
    });
    baz.addEventListener("click", function (e) {
        console.log("klik na #baz");
    });
});
});

var zamianaklasy = function () {
    var strona = document.getElementById("myDiv666");
    strona.classList.toggle("class2");
    console.log(strona);
}




//todo ------------str. 69

