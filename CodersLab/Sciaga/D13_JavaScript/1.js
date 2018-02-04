console.log("Hello World")
var liczba = 10;
var text = "ala ma kota";
var bool = true;
var foo = null;
var bar = undefined;
var kot = {
    imie: "Mruczek",
    wiek: 3,
}
var tab = [1, 2, "ala"]
var liczba_string = "100";

console.log(liczba);
console.log(text);
console.log(bool);
console.log(foo);
console.log(bar);
console.log(kot);
console.log(tab);

console.log(typeof liczba);
console.log(liczba + kot.wiek);
console.log(text + " " + kot.imie);
console.log(parseInt(liczba_string, 2));
console.log(liczba + parseInt(liczba_string,2));

var a = 2;
var b = 20;
if(a == b){
    console.log("a == b");
} else if (a < b){
    console.log("a < b")
}

switch (a) {
    case 1:
        console.log("a = 1");
        break;
    case 2:
        console.log("a = 2");
        break;
}

var resoult = 999;
for (var i = 0; i < 10; i++){
    resoult = resoult + 1;
}
console.log(resoult)

var i = 0;
i = Math.random() * 100;
console.log(i);
i = Math.floor(i);
console.log(i);

while (i <= 10){
    i = Math.floor(Math.random() * 100);
    console.log(i);
}
console.log("-------");
do {
    if (i >= 70) {
        break;
    }
    i = Math.floor(Math.random() * 100);
    console.log(i);

} while (i <= 50);
console.log("--------");
var a = 10;
var b = "10";

if (a === parseInt(b, 10)){
    console.log("równe");
} else {
    console.log("nie równe");
}

var text1 = "3";
var liczba1 = 2;
console.log(typeof (text1 + liczba1));
console.log(text1 - liczba1);
console.log(a % 4);

var a = 5;
var b = 5;
var c = 5;
if ((a == 6) || (b == 5) && (c == 5)){
    console.log("równe");
} else {
    console.log("nie równe");
}

var liczba3 = 23;
console.log((liczba3 != 23) && (liczba3 > 10));
console.log((liczba3 != 23) || (liczba3 > 10));
console.log(!(liczba3 > 22));
console.log((liczba3 != 23) ^ (liczba3 < 10));

console.log("----------")
getName();
function getName(){
    console.log("Ala");
}
getName();
var foo = function getName2() {

    console.log("Ala2");
}
var fooo = function(){

    console.log("Ala3");
}

foo();
fooo();

function getNa(te){
    console.log("Ala" + te);
    return(te + " i lala");
}

getNa(" srala");
var a = getNa(" kichala");
console.log(a);


function Duzo_zmiennych() {
    return(arguments[2]); // + arguments.length);
}
console.log("--------");
console.log(Duzo_zmiennych(1, 2, 3, 4, 5));
var a = Duzo_zmiennych("a", "b", "c");
console.log(a);//.length);

console.log("--------");
var mixTypes =
    ["ala",
        23,
    "temat",
    true,
        {name:"Robert", age: 49},
    function () {return 2;},
    null,
];

console.log(mixTypes[0]);
console.log(mixTypes[4].age);
console.log(mixTypes[3]);
console.log(mixTypes[5]());

console.log("------------");
var tabmatrix =
    [[1,2,3,4,5,],
        [6,7,8,9,0]];
console.log(tabmatrix[1][1]);

tabmatrix[2] = [66,77,88,99];
console.log(tabmatrix[2][3]);

var teacher = {
    name: "jan",
    surname: "kowal",
    subject: "pol",
    teach: function () {
        return "Uczę pol";
    },
    opisz: function () {
        console.log(this.name);
    }
};

console.log("------------");
console.log(teacher.teach());
teacher.opisz();

teacher.students = ["ala", "ola", "lola"];
console.log(teacher.students[2]);


console.log("-----------");
var Car = function (aa, bb, cc) {
    this.a = aa;
    this.b = bb;
    this.c = cc;
    this.km = 0;
};

var bmw = new Car(111,112,0);
console.log(bmw.c);

Car.prototype.drive = function (km) {
    console.log(this.c + km);
    this.km += km;
    console.log(this.km);
};

bmw.drive(10);
bmw.drive(100);

var audi = new Car(999, 555, 333);
audi.drive(1000);
console.log("---------------");

var bec = 100;
console.log(bec);

name = "adam";

function jeden () {
    console.log(name)
}

function dwa () {
    var name = "stef";
    console.log(name);
}

jeden();
dwa();
jeden();

console.log("----------");
var fooOut = function () {
    var name = "Jacek";
    var fooin = function () {
        var age = 43;
        console.log(hi + " " + name + " " + age);
    }
    fooin();
    name = "Wojtek";
    fooin();
}

var hi = "Witaj";
fooOut();

console.log("--------");
var nums = [5 ,4, 2, 33, 7, 9, 19];
nums.sort();
console.log(nums);
nums.sort(function (a, b) {
    return a -b;
});
console.log(nums);

var czasowa = setTimeout(function () {
    console.log("Po czasie test");
    clearTimeout(interval);
}, 3000);
clearTimeout(czasowa);

var interval = setInterval(function () {
    console.log("Interwal");
}, 2000);
clearInterval(interval);

//todo Stringi metody
// str.charAt(); znak na pozycji
// str.concat(); łącznie
// str.indexOf(); pozycja szukanego ciągu
// str.lastIndexOf(); index ostatniego wystapienia ciagu
// str.replace(); zniama jednego ciagu na drugi
// str.slice(); wyciaganie kawalka danego ciagu
// str.split(); dzielenie ciagu na podstawowe dane rozdzielnika
// str.substr(); wyciaganie kawalka danego ciagu
// str.substrring(); wyciaganie kawalka danego ciagu
// str.toLowerCase()
// str.toUpperCase();
// str.trim(); usuwanie białych znaków z początku i końca

console.log("-----------");
var foo = "potato";
console.log(foo.charAt(3));
console.log(foo);

var jeden = ("jeden");
var dwa = ("dwa");
console.log(jeden.concat(dwa));
console.log(jeden);

var tekst = "dupa jaś supa salata podlugowata dupa";
var nowy_tekst = tekst.indexOf("jaś");
console.log(nowy_tekst);

var nowy_tekst = tekst.lastIndexOf("dupa");
console.log(nowy_tekst);

var nowy_tekst = tekst.replace("dupa", "supa");
console.log(nowy_tekst);

var podzielone = tekst.split(" ");
console.log(podzielone);

var text = "abcdefghijg";
var kawalek = text.slice(1,3);
console.log(kawalek);

var text = "abcdefghijg";
console.log("--------");
console.log(text);
var kawalek = text.substr(-8);
console.log(kawalek);

var text = "abcdefghijg";
var kawalek = text.toLowerCase();
console.log(kawalek);

var text = "abcdefghijg";
var kawalek = text.toUpperCase();
console.log(kawalek);

var text = "   a bcdefghijg   ";
var kawalek = text.trim();
console.log(text);
console.log(kawalek);


console.log("-----------");

// todo Metody Tablice
// todo mutacyjne
// arr.pop() usuń i zwruć ostatni element tablicy
// arr.push() dodaj element na koniec  tablicty
// arr.reverse() odwruc całą tablice
// arr.shift() usun i zwruc pierwszy element tablicy
// arr.sort() posortuj na podstaie przekazanje funkji
// arr.splice() usun(ew. zmien) i zwróc kawałek tablicy
// arr.unshift() dodaj element na początek tablicy
// //todo dostepowe
// arr.concat() połącz dwie tablice
// arr.join() połącz tablice w ciąg znakówk
// arr.slice() zwruc kawałek tablicy
// arr.indexOf() pozycja szukanego elementu
// arr.lastIndexOf() ostatnie pozycja szukanego elementu
// //todo iteracyjne
// arr.forEach() wywołaj funkcję dla każdego elementu
// arr.every() sprawdz czy wszystkie lementy spełniają warunek
// arr.some() sprawdz czy jaki kolwiek element spełnia warunek
// arr.filter wywaołaj funkcję na kązdym elemencie tablici i zwruc nową tablice z elementami które go spełniły
// arr.map() wywaołaj funkcję dla każdego elementu i zwruć nową tablice

var foo = [1, 2, 3, 4, 5];
var lastElem = foo.pop();
console.log(lastElem);

foo.push(6, 7);
console.log(foo);

foo.reverse();
console.log(foo);

var firstElem = foo.shift();
console.log(foo);
console.log(firstElem);

var firstElem = foo.unshift(99);
console.log(foo);
console.log(firstElem);

var foo = [1, 2, 3, 4, 5];
foo.splice(-1);
console.log(foo);
foo.splice(4, 0, 5, 6, 7, 8);
// console.log(foo);
// var foo = [1, 2, 3, 4, 5];
// foo.splice(1, 2, 99, 99, 99 );
// console.log(foo);
console.log(foo);
var boo = [9, 10, 11, 12, 13, 14];
var baz = foo.concat(boo);
console.log(baz);
var boz = ["do", "pociągu", "do", "byle", "jakiego"];
var jjj = baz.join(" ");
console.log(jjj);

console.log(boz.slice(-1, 2));
console.log(boz.indexOf("do"));
console.log(boz);
console.log(boz.lastIndexOf("do"));

baz.forEach(function (element, index, array) {
    console.log(array[index]);
    console.log("Element " + element + " ", index);
})

var bbb = baz.some(function (element, index, array) {//przynajmniej jeden
    return element % 2 == 0;
    // if(element % 2 == 0) {
    //     console.log(array[index]);
});

console.log(bbb);
console.log(baz + "------------");
var azz = baz.every(function (element, index, array) {// wszystkie elementy
    if(element % 1 == 0) {
        console.log(array[index]);
    }
})

console.log(baz + "+-----------");
var azz = baz.filter(function (element, index, array) {// wszystkie elementy
    return element % 2 === 0;
});
console.log(azz);

console.log(baz + "++-----------");
var azz = baz.map(function (element, index, array) {// wszystkie elementy
    return element * 2;
});
console.log(azz);









// ------------------------------------- SKOŃCZONE !!!!
