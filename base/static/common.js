



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





function a1__show_green(){

    console.log("성공");
    $('.modal1').css('display', 'block')
}

function a1__show_red(){

    console.log("성공");
    $('.modal2').css('display', 'block')
}

function a1__show_gray(){

    console.log("성공");
    $('.modal3').css('display', 'block')
}

function a1__show_gold(){

    console.log("성공");
    $('.modal4').css('display', 'block')
}

$('.add-green').click(a1__show_green);
$('.add-red').click(a1__show_red);
$('.add-gray').click(a1__show_gray);
$('.add-gold').click(a1__show_gold);



function a1__hide_green(){
    $('.modal1').css('display', 'none');
    console.log("성공2");
}

function a1__hide_red(){
    $('.modal2').css('display', 'none');
    console.log("성공2");
}

function a1__hide_gray(){
    $('.modal3').css('display', 'none');
    console.log("성공2");
}

function a1__hide_gold(){
    $('.modal4').css('display', 'none');
    console.log("성공2");
}





$('.cancel').click(a1__hide_green);

$('.cancel').click(a1__hide_red);

$('.cancel').click(a1__hide_gray);

$('.cancel').click(a1__hide_gold);


function action_add__green(){
	var text_add1 = $("#text_add1").val(); //입력할 글씨
	var ul_list1 = $("#ul_list1"); //ul_list선언
	ul_list1.append("<li>"+text_add1+"</li>"); //ul_list안쪽에 li추가
	$('.modal1').css('display', 'none');
	console.log("성공4");
}

function action_add__red(){
	var text_add2 = $("#text_add2").val(); //입력할 글씨
	var ul_list2 = $("#ul_list2"); //ul_list선언
	ul_list2.append("<li>"+text_add2+"</li>"); //ul_list안쪽에 li추가
	$('.modal2').css('display', 'none');
	console.log("성공4");
}

function action_add__gray(){
	var text_add3 = $("#text_add3").val(); //입력할 글씨
	var ul_list3 = $("#ul_list3"); //ul_list선언
	ul_list3.append("<li>"+text_add3+"</li>"); //ul_list안쪽에 li추가
	$('.modal3').css('display', 'none');
	console.log("성공4");
}

function action_add__gold(){
	var text_add4 = $("#text_add4").val(); //입력할 글씨
	var ul_list4 = $("#ul_list4"); //ul_list선언
	ul_list4.append("<li>"+text_add4+"</li>"); //ul_list안쪽에 li추가
	$('.modal4').css('display', 'none');
	console.log("성공4");
}



$('.add1').click(action_add__green);
$('.add2').click(action_add__red);
$('.add3').click(action_add__gray);
$('.add4').click(action_add__gold);

// 테스트시작
function action_add(){
	var text_add = $("#text_add").val(); //입력할 글씨
	var ul_list = $("#ul_list"); //ul_list선언
	ul_list.append("<li>"+text_add+"</li>"); //ul_list안쪽에 li추가
}
// 테스트 끝

// 체크박스 시작


/* 체크박스 테스트케이스 */
$('.form-1__checkbox-all').change(function() {
  if ( this.checked ) {
    $('.form-1__checkbox-item:not(:checked)').prop('checked', true);
  }
});
/* 체크박스 테스트케이스 끝 */



/* 중요하지만 급하지 않아 체크박스 전체 선택 */
$('.green__check_all').change(function() {
  if ( this.checked ) {
    $('.green_check__item:not(:checked)').prop('checked', true);
  }
  else{
    $('.green_check__item:checked').prop('checked', false);
  }
});

$('.green_check__item').change(function(){
    let allChecked = $('.green_check__item:not(:checked)').length == 0;
    $('.green__check_all').prop('checked', allChecked);
});
/* 중요하지만 급하지 않아 체크박스 전체 선택 끝 */

/* 중요하고 급해 체크박스 전체 선택 */
$('.red__check_all').change(function() {
  if ( this.checked ) {
    $('.red_check__item:not(:checked)').prop('checked', true);
  }
  else{
    $('.red_check__item:checked').prop('checked', false);
  }
});

$('.red_check__item').change(function(){
    let allChecked = $('.red_check__item:not(:checked)').length == 0;
    $('.red__check_all').prop('checked', allChecked);
});
/* 중요하고 급해 체크박스 전체 선택 끝 */

/* 중요하지도 않고 급하지도 않아 체크박스 전체 선택 */
$('.gray__check_all').change(function() {
  if ( this.checked ) {
    $('.gray_check__item:not(:checked)').prop('checked', true);
  }
  else{
    $('.gray_check__item:checked').prop('checked', false);
  }
});

$('.gray_check__item').change(function(){
    let allChecked = $('.gray_check__item:not(:checked)').length == 0;
    $('.gray__check_all').prop('checked', allChecked);
});
/* 중요하지도 않고 급하지도 않아 체크박스 전체 선택 끝 */

/* 중요하진 않은데 급해 체크박스 전체 선택 */
$('.gold__check_all').change(function() {
  if ( this.checked ) {
    $('.gold_check__item:not(:checked)').prop('checked', true);
  }
  else{
    $('.gold_check__item:checked').prop('checked', false);
  }
});

$('.gold_check__item').change(function(){
    let allChecked = $('.gold_check__item:not(:checked)').length == 0;
    $('.gold__check_all').prop('checked', allChecked);
});
/* 중요하진 않은데 급해 체크박스 전체 선택 끝 */


// 체크박스 끝



