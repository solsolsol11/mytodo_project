



        $(function(){
            var today = new Date();
            var date = new Date();           

            $("input[name=preMon]").click(function() { // 이전달
                $("#calendar > tbody > td").remove();
                $("#calendar > tbody > tr").remove();
                today = new Date ( today.getFullYear(), today.getMonth()-1, today.getDate());
                buildCalendar();
            })
            
            $("input[name=nextMon]").click(function(){ //다음달
                $("#calendar > tbody > td").remove();
                $("#calendar > tbody > tr").remove();
                today = new Date ( today.getFullYear(), today.getMonth()+1, today.getDate());
                buildCalendar();
            })


            function buildCalendar() {
                
                nowYear = today.getFullYear();
                nowMonth = today.getMonth();
                firstDate = new Date(nowYear,nowMonth,1).getDate();
                firstDay = new Date(nowYear,nowMonth,1).getDay(); //1st의 요일
                lastDate = new Date(nowYear,nowMonth+1,0).getDate();

                if((nowYear%4===0 && nowYear % 100 !==0) || nowYear%400===0) { //윤년 적용
                    lastDate[1]=29;
                }

                $(".year_mon").text(nowYear+"년 "+(nowMonth+1)+"월");

                for (i=0; i<firstDay; i++) { //첫번째 줄 빈칸
                    $("#calendar tbody:last").append("<td></td>");
                }
                for (i=1; i <=lastDate; i++){ // 날짜 채우기
                    plusDate = new Date(nowYear,nowMonth,i).getDay();
                    if (plusDate==0) {
                        $("#calendar tbody:last").append("<tr></tr>");
                    }
                    $("#calendar tbody:last").append("<td class='date'>"+ i +"</td>");
                }
                if($("#calendar > tbody > td").length%7!=0) { //마지막 줄 빈칸
                    for(i=1; i<= $("#calendar > tbody > td").length%7; i++) {
                        $("#calendar tbody:last").append("<td></td>");
                    }
                }
                $(".date").each(function(index){ // 오늘 날짜 표시
                    if(nowYear==date.getFullYear() && nowMonth==date.getMonth() && $(".date").eq(index).text()==date.getDate()) {
                        $(".date").eq(index).addClass('colToday');
                    }

                })
                $(".date").each(function(index){ // 이전 날짜 표시
                    for(j=1; j<date.getDate(); j++){
                        if($(".date").eq(index).text()==date.getDate() - j) {
                            $(".date").eq(index).addClass('preToday');
                        }
                    }



                })
            }
            buildCalendar();


        })

        function check_today(indexs, weeks, dates){
    if(dates > today_days){
        //인덱스가 오늘의 날짜보다 크다면(미래: 일정 추가 가능)
        weeks[indexs].style.backgroundColor = '#FFEFD5'; //CSS 불러오기
    } else if(dates == today_days){
         //인덱스가 오늘의 날짜와 같다면(현재: 일정 추가 가능)
         weeks[indexs].style.backgroundColor = '#DB7093'; //CSS 불러오기
    } else if(dates < today_days){
        //인덱스가 오늘의 날짜보다 작다면(지나온 날: 일정 추가 불가)
        weeks[indexs].style.backgroundColor = 'gray'; //CSS 불러오기
    }
}








// todolist 시작
var button = document.getElementById('button');
var input = document.getElementById('input');
var list = document.getElementById('list');

button.addEventListener('click', clickButton);

function clickButton(){
  var temp = document.createElement('li');
  temp.innerHTML = input.value;
  list.appendChild(temp);
}
// todolist 끝


var td = document.querySelectorAll('td'); //모든 태그에 대해 알림창 설정

for(var i=0; i<td.length; i++){
    if(i>=(today_days+null_days-1)){ //여기에서만 실행되도록 정하기 today_days+null_days-1는 현재 날짜 전까지의 인덱스를 표현한 것
        //get_data(i); //해당 인덱스에만 알람 표시하기
        //console.log(get_data(i));
        td[i].ondblclick = function() {
            //test_data = $("#data").text();
           // console.log(get_data(i));
            alert('hum');
        };
    }
}

