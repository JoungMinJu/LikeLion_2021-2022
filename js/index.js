const  timeContainer = document.querySelector(".time"),
//상수 만들거고 html의 time 클래스 받아오겠다는 뜻
//querySelector 메소드를 사용했다. -- element를 return하는 메소드
    // nowHour=timeContainer.querySelector("#hour"),
    // nowMin=timeContainer.querySelector("#minutes"),
    // nowSec=timeContainer.querySelector("#seconds"),
    nowAmpm=timeContainer.querySelector("#period");
    //timecontainer 내부에 있는 것을 받아오겄다 

const dayContainer = document.querySelector(".date");
    // nowDay = dayContainer.querySelector("#dayname"),
    // nowMonth = dayContainer.querySelector("#month"),
    // nowDate = dayContainer.querySelector("#daynum"),
    // nowYear = dayContainer.querySelector("#year");

//내장객체 : 자바 스크립트 안에 미리 객체로 정의
//         : 대표적인 예로 날짜 정보가 있음


//함수 만들기
function getTime(){
 const now=new Date(); //지금 시간이 now에 담김
 const minutes=now.getMinutes();
 let hours=now.getHours(); //아래에서 hours를 바꿀 것이므로 얘는 상수 아님
 const seconds=now.getSeconds();
 
if (hours>=12){
    nowAmpm.innerText="PM";
}
if(hours==0){
    hours=12;
}
if(hours>12){
    hours=hours-12;
}
let timeIds=["hour","minutes","seconds"];
let timeValues=[hours<10?`0${hours}`:hour,minutes<10?`0${minutes}`:minutes,seconds<10?`0${seconds}`:seconds];

 //html에 text 넣기
//  nowHour.innerText=timeValues[0]; //${}을 통해 변수값을 받아올 수 있음!
//  nowMin.innerText=timeValues[1]; 
//  nowSec.innerText=timeValues[2];

 
 for (let i=0;i<timeIds.length;i++){
     document.getElementById(timeIds[i]).firstChild.nodeValue=timeValues[i]; //firstChld 는 첫번쨰 자식 노드 리턴하겠다는 뜻?
 }

}



function getCalender() {
    const now = new Date();
    const  day = now.getDay(); // 요일
    const  month = now.getMonth(); // 월
    const  date = now.getDate(); // 일
    const  year = now.getFullYear(); // 년

    let week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      let monthList=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ];


    // nowDay.innerText = week[day];//요일
    // nowMonth.innerText = month+1;
    // nowDate.innerText = date;
    // nowYear.innerText = year;

    let ids=["dayname","month","daynum","year"];
    let values=[week[day],monthList[month],date<10?`0${date}`:date,year];

    for (let i=0;i<ids.length;i++){
        document.getElementById(ids[i]).firstChild.nodeValue=values[i]; //firstChld 는 첫번쨰 자식 노드 리턴하겠다는 뜻?
    }


  }


function init(){
    getTime();
    setInterval(getTime, 1000); //1초바다 getTime 함수가 실행된다.
    getCalender();
}

//js의 함수 호출 관습 init함수로 getTime함수를 부름 
//init은 js 실행 시점에 초기화가 되는 함수이다.


init();
