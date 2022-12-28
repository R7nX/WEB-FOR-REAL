<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="static/style.css">

<title>Take test</title>
</head>
<body>
<body class="bruh">

<div class="header">
<h1>Vocational Guidance</h1>
</div>

<div class="topnav">
<a href="{{ url_for('index') }}">Home</a>
<a href="{{ url_for('contact') }}">Contact</a>
<a href="{{ url_for('intro') }}"> Intro</a>
</div>

<script>
window.onscroll = function () {
scrollFunction()
};

function scrollFunction() {
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      document.getElementById("navbar").style.top = "0";
} else {
      document.getElementById("navbar").style.top = "-50px";
}
}</script>


<form  method="post">
<label for="lang-switch">
<span lang="vie"> Chọn ngôn ngữ</span>
<span lang="en">Choose language</span>
</label>
<select id="lang-switch">
<option value="en">English</option>
<option value="vie" selected>Tiếng Việt</option>
</select>

<span lang="vie">
<br>
      <label id="q1-label" for="question1">Bạn thường làm quen được nhiều bạn mới.</label> <br><br>
               <input type="radio" name="question1" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question1" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question1" value="-1"> Không đồng tình một phần
               <input type="radio" name="question1" value="0"> Trung lập
               <input type="radio" name="question1" value="1"> Đồng tình một phần
               <input type="radio" name="question1" value="2"> Tương đối đồng tình
               <input type="radio" name="question1" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q2-label" for="question2">Bạn dành nhiều thời gian để khám phá những chủ đề mới lạ khơi gợi cho bạn nhiều hứng thú.</label> <br><br>
               <input type="radio" name="question2" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question2" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question2" value="-1"> Không đồng tình một phần
               <input type="radio" name="question2" value="0"> Trung lập
               <input type="radio" name="question2" value="1"> Đồng tình một phần
               <input type="radio" name="question2" value="2"> Tương đối đồng tình
               <input type="radio" name="question2" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q3-label" for="question3">Bạn cũng thấy muốn khóc khi nhìn người khác bật khóc </label><br><br>
               <input type="radio" name="question3" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question3" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question3" value="-1"> Không đồng tình một phần
               <input type="radio" name="question3" value="0"> Trung lập
               <input type="radio" name="question3" value="1"> Đồng tình một phần
               <input type="radio" name="question3" value="2"> Tương đối đồng tình
               <input type="radio" name="question3" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q4-label" for="question4">Bạn thường có kế hoạch dự phòng.</label><br><br>
               <input type="radio" name="question4" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question4" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question4" value="-1"> Không đồng tình một phần
               <input type="radio" name="question4" value="0"> Trung lập
               <input type="radio" name="question4" value="1"> Đồng tình một phần
               <input type="radio" name="question4" value="2"> Tương đối đồng tình
               <input type="radio" name="question4" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q5-label" for="question5">Bạn thường giữ được sự bình tĩnh kể cả khi chịu đựng áp lực lớn.</label><br><br>
               <input type="radio" name="question5" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question5" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question5" value="-1"> Không đồng tình một phần
               <input type="radio" name="question5" value="0"> Trung lập
               <input type="radio" name="question5" value="1"> Đồng tình một phần
               <input type="radio" name="question5" value="2"> Tương đối đồng tình
               <input type="radio" name="question5" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q6-label" for="question6">Ở những sự kiện, bạn hiếm khi giới thiệu mình với người lạ mà hầu như chỉ nói chuyện với những người bạn đã quen biết.</label> <br><br>
               <input type="radio" name="question6" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question6" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question6" value="-1"> Không đồng tình một phần
               <input type="radio" name="question6" value="0"> Trung lập
               <input type="radio" name="question6" value="1"> Đồng tình một phần
               <input type="radio" name="question6" value="2"> Tương đối đồng tình
               <input type="radio" name="question6" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q7-label" for="question7">Bạn luôn ưu tiên hoàn thành việc đang làm trước khi bắt đầu một việc mới.</label> <br><br>
               <input type="radio" name="question7" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question7" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question7" value="-1"> Không đồng tình một phần
               <input type="radio" name="question7" value="0"> Trung lập
               <input type="radio" name="question7" value="1"> Đồng tình một phần
               <input type="radio" name="question7" value="2"> Tương đối đồng tình
               <input type="radio" name="question7" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q8-label" for="question8">Bạn là một người rất đa cảm. </label><br><br>
               <input type="radio" name="question8" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question8" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question8" value="-1"> Không đồng tình một phần
               <input type="radio" name="question8" value="0"> Trung lập
               <input type="radio" name="question8" value="1"> Đồng tình một phần
               <input type="radio" name="question8" value="2"> Tương đối đồng tình
               <input type="radio" name="question8" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q9-label" for="question9">Bạn thích việc sử dụng những công cụ hỗ trợ tổ chức và sắp xếp, ví dụ như lên thời khóa biểu, danh sách. </label><br><br>
               <input type="radio" name="question9" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question9" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question9" value="-1"> Không đồng tình một phần
               <input type="radio" name="question9" value="0"> Trung lập
               <input type="radio" name="question9" value="1"> Đồng tình một phần
               <input type="radio" name="question9" value="2"> Tương đối đồng tình
               <input type="radio" name="question9" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q10-label" for="question10">Việc mắc một lỗi nhỏ cũng khiến bạn hoài nghi về năng lực và kiến thức của bản thân. </label><br><br>
               <input type="radio" name="question10" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question10" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question10" value="-1"> Không đồng tình một phần
               <input type="radio" name="question10" value="0"> Trung lập
               <input type="radio" name="question10" value="1"> Đồng tình một phần
               <input type="radio" name="question10" value="2"> Tương đối đồng tình
               <input type="radio" name="question10" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q11-label" for="question11">Bạn cảm thấy thoải mái với việc bắt chuyện với những người mà bạn thấy thú vị.</label><br><br>
               <input type="radio" name="question11" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question11" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question11" value="-1"> Không đồng tình một phần
               <input type="radio" name="question11" value="0"> Trung lập
               <input type="radio" name="question11" value="1"> Đồng tình một phần
               <input type="radio" name="question11" value="2"> Tương đối đồng tình
               <input type="radio" name="question11" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q12-label" for="question12">Bạn không hứng thú với việc thảo luận về các góc nhìn hoặc phân tích các tác phẩm nghệ thuật.</label><br><br>
               <input type="radio" name="question12" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question12" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question12" value="-1"> Không đồng tình một phần
               <input type="radio" name="question12" value="0"> Trung lập
               <input type="radio" name="question12" value="1"> Đồng tình một phần
               <input type="radio" name="question12" value="2"> Tương đối đồng tình
               <input type="radio" name="question12" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q13-label" for="question13">Bạn có xu hướng đặt lý trí lên trước cảm xúc cá nhân.</label><br><br>
               <input type="radio" name="question13" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question13" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question13" value="-1"> Không đồng tình một phần
               <input type="radio" name="question13" value="0"> Trung lập
               <input type="radio" name="question13" value="1"> Đồng tình một phần
               <input type="radio" name="question13" value="2"> Tương đối đồng tình
               <input type="radio" name="question13" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q14-label" for="question14">Bạn yêu thích làm việc dựa trên cảm hứng hơn là lên kế hoạch hằng ngày.</label><br><br>
               <input type="radio" name="question14" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question14" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question14" value="-1"> Không đồng tình một phần
               <input type="radio" name="question14" value="0"> Trung lập
               <input type="radio" name="question14" value="1"> Đồng tình một phần
               <input type="radio" name="question14" value="2"> Tương đối đồng tình
               <input type="radio" name="question14" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q15-label" for="question15">Bạn ít khi lo lắng rằng mình có gây ấn tượng tốt với những người bạn gặp.</label><br><br>
               <input type="radio" name="question15" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question15" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question15" value="-1"> Không đồng tình một phần
               <input type="radio" name="question15" value="0"> Trung lập
               <input type="radio" name="question15" value="1"> Đồng tình một phần
               <input type="radio" name="question15" value="2"> Tương đối đồng tình
               <input type="radio" name="question15" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q16-label" for="question16">Bạn yêu thích việc tham gia các hoạt động nhóm.</label><br><br>
               <input type="radio" name="question16" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question16" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question16" value="-1"> Không đồng tình một phần
               <input type="radio" name="question16" value="0"> Trung lập
               <input type="radio" name="question16" value="1"> Đồng tình một phần
               <input type="radio" name="question16" value="2"> Tương đối đồng tình
               <input type="radio" name="question16" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q17-label" for="question17">Bạn thích những bộ phim hoặc quyển sách nào có thể khiến bạn tò mò tưởng tượng ra một đoạn kết khác theo ý của mình</label> <br><br>
               <input type="radio" name="question17" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question17" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question17" value="-1"> Không đồng tình một phần
               <input type="radio" name="question17" value="0"> Trung lập
               <input type="radio" name="question17" value="1"> Đồng tình một phần
               <input type="radio" name="question17" value="2"> Tương đối đồng tình
               <input type="radio" name="question17" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q18-label" for="question18">Việc giúp đỡ người khác đạt được những thành tựu khiến bạn cảm thấy hạnh phúc hơn việc bản thân đạt được những thành tựu.</label><br><br>
               <input type="radio" name="question18" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question18" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question18" value="-1"> Không đồng tình một phần
               <input type="radio" name="question18" value="0"> Trung lập
               <input type="radio" name="question18" value="1"> Đồng tình một phần
               <input type="radio" name="question18" value="2"> Tương đối đồng tình
               <input type="radio" name="question18" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q19-label" for="question19">Bạn có quá nhiều sở thích và chúng làm bạn khó lựa chọn được sẽ làm thử gì tiếp theo.</label><br><br>
               <input type="radio" name="question19" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question19" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question19" value="-1"> Không đồng tình một phần
               <input type="radio" name="question19" value="0"> Trung lập
               <input type="radio" name="question19" value="1"> Đồng tình một phần
               <input type="radio" name="question19" value="2"> Tương đối đồng tình
               <input type="radio" name="question19" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q20-label" for="question20">Bạn dễ bị lo lắng rằng mọi việc có thể trở nên tệ hơn.</label><br><br>
               <input type="radio" name="question20" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question20" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question20" value="-1"> Không đồng tình một phần
               <input type="radio" name="question20" value="0"> Trung lập
               <input type="radio" name="question20" value="1"> Đồng tình một phần
               <input type="radio" name="question20" value="2"> Tương đối đồng tình
               <input type="radio" name="question20" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q21-label" for="question21">Bạn thường tránh vai trò lãnh đạo trong nhóm.</label><br><br>
               <input type="radio" name="question21" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question21" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question21" value="-1"> Không đồng tình một phần
               <input type="radio" name="question21" value="0"> Trung lập
               <input type="radio" name="question21" value="1"> Đồng tình một phần
               <input type="radio" name="question21" value="2"> Tương đối đồng tình
               <input type="radio" name="question21" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q22-label" for="question22">Bạn chắc chắn không phải là một người có tâm hồn nghệ sĩ.</label><br><br>
               <input type="radio" name="question22" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question22" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question22" value="-1"> Không đồng tình một phần
               <input type="radio" name="question22" value="0"> Trung lập
               <input type="radio" name="question22" value="1"> Đồng tình một phần
               <input type="radio" name="question22" value="2"> Tương đối đồng tình
               <input type="radio" name="question22" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q23-label" for="question23">Bạn quan niệm rằng thế giới sẽ tốt hơn nếu mọi người dựa vào lý trí hơn là cảm xúc.</label><br><br>
               <input type="radio" name="question23" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question23" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question23" value="-1"> Không đồng tình một phần
               <input type="radio" name="question23" value="0"> Trung lập
               <input type="radio" name="question23" value="1"> Đồng tình một phần
               <input type="radio" name="question23" value="2"> Tương đối đồng tình
               <input type="radio" name="question23" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q24-label" for="question24">Bạn lựa chọn hoàn thành việc nhà trước khi nghỉ ngơi.</label><br><br>
               <input type="radio" name="question24" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question24" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question24" value="-1"> Không đồng tình một phần
               <input type="radio" name="question24" value="0"> Trung lập
               <input type="radio" name="question24" value="1"> Đồng tình một phần
               <input type="radio" name="question24" value="2"> Tương đối đồng tình
               <input type="radio" name="question24" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q25-label" for="question25">Bạn thích xem người khác tranh luận.</label> <br><br>
               <input type="radio" name="question25" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question25" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question25" value="-1"> Không đồng tình một phần
               <input type="radio" name="question25" value="0"> Trung lập
               <input type="radio" name="question25" value="1"> Đồng tình một phần
               <input type="radio" name="question25" value="2"> Tương đối đồng tình
               <input type="radio" name="question25" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q26-label" for="question26">Bạn có khuynh hướng tránh thu hút sự chú ý về phía mình.</label><br><br>
               <input type="radio" name="question26" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question26" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question26" value="-1"> Không đồng tình một phần
               <input type="radio" name="question26" value="0"> Trung lập
               <input type="radio" name="question26" value="1"> Đồng tình một phần
               <input type="radio" name="question26" value="2"> Tương đối đồng tình
               <input type="radio" name="question26" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q27-label" for="question27">Tâm trạng của bạn dễ bị thay đổi.</label><br><br>
               <input type="radio" name="question27" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question27" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question27" value="-1"> Không đồng tình một phần
               <input type="radio" name="question27" value="0"> Trung lập
               <input type="radio" name="question27" value="1"> Đồng tình một phần
               <input type="radio" name="question27" value="2"> Tương đối đồng tình
               <input type="radio" name="question27" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q28-label" for="question28">Bạn dễ mất kiên nhẫn với những người làm việc không hiệu quả bằng bạn.</label><br><br>
               <input type="radio" name="question28" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question28" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question28" value="-1"> Không đồng tình một phần
               <input type="radio" name="question28" value="0"> Trung lập
               <input type="radio" name="question28" value="1"> Đồng tình một phần
               <input type="radio" name="question28" value="2"> Tương đối đồng tình
               <input type="radio" name="question28" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q29-label" for="question29">Bạn thường hoàn thành công việc vào lúc cuối cùng nhất có thể.</label> <br><br>
               <input type="radio" name="question29" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question29" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question29" value="-1"> Không đồng tình một phần
               <input type="radio" name="question29" value="0"> Trung lập
               <input type="radio" name="question29" value="1"> Đồng tình một phần
               <input type="radio" name="question29" value="2"> Tương đối đồng tình
               <input type="radio" name="question29" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q30-label" for="question30">Bạn luôn băn khoăn về những câu hỏi về việc gì sẽ diễn ra sau cái chết.</label><br><br>
               <input type="radio" name="question30" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question30" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question30" value="-1"> Không đồng tình một phần
               <input type="radio" name="question30" value="0"> Trung lập
               <input type="radio" name="question30" value="1"> Đồng tình một phần
               <input type="radio" name="question30" value="2"> Tương đối đồng tình
               <input type="radio" name="question30" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q31-label" for="question31">Bạn thường thích việc ở gần người khác hơn là ở một mình.</label><br><br>
               <input type="radio" name="question31" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question31" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question31" value="-1"> Không đồng tình một phần
               <input type="radio" name="question31" value="0"> Trung lập
               <input type="radio" name="question31" value="1"> Đồng tình một phần
               <input type="radio" name="question31" value="2"> Tương đối đồng tình
               <input type="radio" name="question31" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q32-label" for="question32">Khi vấn đề tranh luận trở nên quá lý thuyết, bạn cảm thấy buồn chán và mất hết hứng thú.</label><br><br>
               <input type="radio" name="question32" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question32" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question32" value="-1"> Không đồng tình một phần
               <input type="radio" name="question32" value="0"> Trung lập
               <input type="radio" name="question32" value="1"> Đồng tình một phần
               <input type="radio" name="question32" value="2"> Tương đối đồng tình
               <input type="radio" name="question32" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q33-label" for="question33">Bạn cảm thấy dễ dàng đồng cảm với những người có trải nghiệm hoàn toàn khác bạn.</label><br><br>
               <input type="radio" name="question33" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question33" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question33" value="-1"> Không đồng tình một phần
               <input type="radio" name="question33" value="0"> Trung lập
               <input type="radio" name="question33" value="1"> Đồng tình một phần
               <input type="radio" name="question33" value="2"> Tương đối đồng tình
               <input type="radio" name="question33" value="3">Hoàn toàn đồng tình <br><br>
      <label id="q34-label" for="question34">Bạn thường xuyên trì hoãn việc đưa ra lựa chọn cuối cùng.</label><br><br>
               <input type="radio" name="question34" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question34" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question34" value="-1"> Không đồng tình một phần
               <input type="radio" name="question34" value="0"> Trung lập
               <input type="radio" name="question34" value="1"> Đồng tình một phần
               <input type="radio" name="question34" value="2"> Tương đối đồng tình
               <input type="radio" name="question34" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q35-label" for="question35">Bạn hiếm khi nghi ngờ lựa chọn của bản thân.</label><br><br>
               <input type="radio" name="question35" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question35" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question35" value="-1"> Không đồng tình một phần
               <input type="radio" name="question35" value="0"> Trung lập
               <input type="radio" name="question35" value="1"> Đồng tình một phần
               <input type="radio" name="question35" value="2"> Tương đối đồng tình
               <input type="radio" name="question35" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q36-label" for="question36">Những gì bạn cần sau một tuần dài mệt mỏi là những sự kiện sôi động, náo nhiệt.</label><br><br>
               <input type="radio" name="question36" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question36" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question36" value="-1"> Không đồng tình một phần
               <input type="radio" name="question36" value="0"> Trung lập
               <input type="radio" name="question36" value="1"> Đồng tình một phần
               <input type="radio" name="question36" value="2"> Tương đối đồng tình
               <input type="radio" name="question36" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q37-label" for="question37">Bạn thích đi bảo tàng nghệ thuật </label><br><br>
               <input type="radio" name="question37" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question37" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question37" value="-1"> Không đồng tình một phần
               <input type="radio" name="question37" value="0"> Trung lập
               <input type="radio" name="question37" value="1"> Đồng tình một phần
               <input type="radio" name="question37" value="2"> Tương đối đồng tình
               <input type="radio" name="question37" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q38-label" for="question38">Bạn thường gặp khó khăn trong việc thấu hiểu cảm xúc của người khác.</label><br><br>
               <input type="radio" name="question38" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question38" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question38" value="-1"> Không đồng tình một phần
               <input type="radio" name="question38" value="0"> Trung lập
               <input type="radio" name="question38" value="1"> Đồng tình một phần
               <input type="radio" name="question38" value="2"> Tương đối đồng tình
               <input type="radio" name="question38" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q39-label" for="question39">Bạn thích lên danh sách công việc cần làm hằng ngày.</label><br><br>
               <input type="radio" name="question39" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question39" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question39" value="-1"> Không đồng tình một phần
               <input type="radio" name="question39" value="0"> Trung lập
               <input type="radio" name="question39" value="1"> Đồng tình một phần
               <input type="radio" name="question39" value="2"> Tương đối đồng tình
               <input type="radio" name="question39" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q40-label" for="question40">Bạn ít khi cảm thấy thiếu an toàn. </label><br><br>
               <input type="radio" name="question40" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question40" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question40" value="-1"> Không đồng tình một phần
               <input type="radio" name="question40" value="0"> Trung lập
               <input type="radio" name="question40" value="1"> Đồng tình một phần
               <input type="radio" name="question40" value="2"> Tương đối đồng tình
               <input type="radio" name="question40" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q41-label" for="question41">Bạn thường tránh việc gọi điện.</label><br><br>
               <input type="radio" name="question41" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question41" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question41" value="-1"> Không đồng tình một phần
               <input type="radio" name="question41" value="0"> Trung lập
               <input type="radio" name="question41" value="1"> Đồng tình một phần
               <input type="radio" name="question41" value="2"> Tương đối đồng tình
               <input type="radio" name="question41" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q42-label" for="question42">Bạn dành khá nhiều thời gian để thử nghiệm những góc nhìn khác hoàn toàn với góc nhìn của bản thân.</label><br><br>
               <input type="radio" name="question42" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question42" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question42" value="-1"> Không đồng tình một phần
               <input type="radio" name="question42" value="0"> Trung lập
               <input type="radio" name="question42" value="1"> Đồng tình một phần
               <input type="radio" name="question42" value="2"> Tương đối đồng tình
               <input type="radio" name="question42" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q43-label" for="question43">Bạn thường là người chủ động liên hệ với người khác cũng như khới xưởng những hoạt động.</label><br><br>
               <input type="radio" name="question43" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question43" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question43" value="-1"> Không đồng tình một phần
               <input type="radio" name="question43" value="0"> Trung lập
               <input type="radio" name="question43" value="1"> Đồng tình một phần
               <input type="radio" name="question43" value="2"> Tương đối đồng tình
               <input type="radio" name="question43" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q44-label" for="question44">Khi kế hoạch không như dự tính, ưu tiên hàng đầu của bạn là đưa mọi việc trở về đúng với kế hoạch ban đầu càng sớm càng tốt.</label><br><br>
               <input type="radio" name="question44" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question44" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question44" value="-1"> Không đồng tình một phần
               <input type="radio" name="question44" value="0"> Trung lập
               <input type="radio" name="question44" value="1"> Đồng tình một phần
               <input type="radio" name="question44" value="2"> Tương đối đồng tình
               <input type="radio" name="question44" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q45-label" for="question45">Bạn vẫn còn để tâm những lỗi sai trong quá khứ.</label><br><br>
               <input type="radio" name="question45" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question45" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question45" value="-1"> Không đồng tình một phần
               <input type="radio" name="question45" value="0"> Trung lập
               <input type="radio" name="question45" value="1"> Đồng tình một phần
               <input type="radio" name="question45" value="2"> Tương đối đồng tình
               <input type="radio" name="question45" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q46-label" for="question46">Bạn ít khi nghiền ngẫm về lý do con người tồn tại cũng như ý nghĩa của cuộc sống.</label><br><br>
               <input type="radio" name="question46" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question46" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question46" value="-1"> Không đồng tình một phần
               <input type="radio" name="question46" value="0"> Trung lập
               <input type="radio" name="question46" value="1"> Đồng tình một phần
               <input type="radio" name="question46" value="2"> Tương đối đồng tình
               <input type="radio" name="question46" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q47-label" for="question47">Bạn bị cảm xúc kiểm soát hơn là bạn kiểm soát chúng.</label><br><br>
               <input type="radio" name="question47" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question47" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question47" value="-1"> Không đồng tình một phần
               <input type="radio" name="question47" value="0"> Trung lập
               <input type="radio" name="question47" value="1"> Đồng tình một phần
               <input type="radio" name="question47" value="2"> Tương đối đồng tình
               <input type="radio" name="question47" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q48-label"
            for="question48">Bạn luôn cố gắng giữ thể diện cho người khác kể cả khi đó là lỗi của họ.</label><br><br>
               <input type="radio" name="question48" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question48" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question48" value="-1"> Không đồng tình một phần
               <input type="radio" name="question48" value="0"> Trung lập
               <input type="radio" name="question48" value="1"> Đồng tình một phần
               <input type="radio" name="question48" value="2"> Tương đối đồng tình
               <input type="radio" name="question48" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q49-label"
            for="question49">Bạn thường làm việc tự phát hơn là lên kế hoạch sắp xếp từ trước. </label><br><br>
               <input type="radio" name="question49" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question49" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question49" value="-1"> Không đồng tình một phần
               <input type="radio" name="question49" value="0"> Trung lập
               <input type="radio" name="question49" value="1"> Đồng tình một phần
               <input type="radio" name="question49" value="2"> Tương đối đồng tình
               <input type="radio" name="question49" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q50-label" for="question50">Khi được người khác đánh giá cao, bạn thường suy nghĩ xem khi nào thì bạn sẽ gây thất vọng cho họ.</label><br><br>
               <input type="radio" name="question50" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question50" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question50" value="-1"> Không đồng tình một phần
               <input type="radio" name="question50" value="0"> Trung lập
               <input type="radio" name="question50" value="1"> Đồng tình một phần
               <input type="radio" name="question50" value="2"> Tương đối đồng tình
               <input type="radio" name="question50" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q51-label" for="question51">Bạn yêu thích những công việc cho phép bạn làm việc một mình trong hầu hết thời gian.</label><br><br>
                  <input type="radio" name="question51" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question51" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question51" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question51" value="0"> Trung lập
                  <input type="radio" name="question51" value="1"> Đồng tình một phần
                  <input type="radio" name="question51" value="2"> Tương đối đồng tình
                  <input type="radio" name="question51" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q52-label"
            for="question52">Bạn tin rằng việc suy ngẫm về những câu hỏi triết học là phí thời gian.</label><br><br>
                  <input type="radio" name="question52" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question52" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question52" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question52" value="0"> Trung lập
                  <input type="radio" name="question52" value="1"> Đồng tình một phần
                  <input type="radio" name="question52" value="2"> Tương đối đồng tình
                  <input type="radio" name="question52" value="3">Hoàn toàn đồng tình<br><br>

      <label id="q53-label" for="question53">Bạn yêu thích những nơi bận rộn, bùng nổ hơn là những nơi yên ắng, tính lặng. </label><br><br>
                  <input type="radio" name="question53" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question53" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question53" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question53" value="0"> Trung lập
                  <input type="radio" name="question53" value="1"> Đồng tình một phần
                  <input type="radio" name="question53" value="2"> Tương đối đồng tình
                  <input type="radio" name="question53" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q54-label"
            for="question54">Bạn có thể hiểu được cảm xúc của người khác ngay từ ánh nhìn đầu tiên. </label><br><br>
                  <input type="radio" name="question54" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question54" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question54" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question54" value="0"> Trung lập
                  <input type="radio" name="question54" value="1"> Đồng tình một phần
                  <input type="radio" name="question54" value="2"> Tương đối đồng tình
                  <input type="radio" name="question54" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q55-label" for="question55">Bạn thường cảm thấy bị choáng ngợp.</label><br><br>
                  <input type="radio" name="question55" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question55" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question55" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question55" value="0"> Trung lập
                  <input type="radio" name="question55" value="1"> Đồng tình một phần
                  <input type="radio" name="question55" value="2"> Tương đối đồng tình
                  <input type="radio" name="question55" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q56-label" for="question56">Bạn hoàn thành công việc một cách có phương pháp, không bỏ sót bất kỳ giai đoạn nào.</label><br><br>
                  <input type="radio" name="question56" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question56" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question56" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question56" value="0"> Trung lập
                  <input type="radio" name="question56" value="1"> Đồng tình một phần
                  <input type="radio" name="question56" value="2"> Tương đối đồng tình
                  <input type="radio" name="question56" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q57-label"
            for="question57">Bạn đặc biệt thích thú trước những thứ mang tính tranh luận. </label><br><br>
                  <input type="radio" name="question57" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question57" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question57" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question57" value="0"> Trung lập
                  <input type="radio" name="question57" value="1"> Đồng tình một phần
                  <input type="radio" name="question57" value="2"> Tương đối đồng tình
                  <input type="radio" name="question57" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q58-label"
            for="question58">Bạn sẵn sàng nhường lại cơ hội của bản thân cho những người thật sự cần nó.</label><br><br>
               <input type="radio" name="question58" value="-3"> Hoàn toàn không đồng tình
               <input type="radio" name="question58" value="-2"> Tương đối không đồng tình
               <input type="radio" name="question58" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question58" value="0"> Trung lập
                  <input type="radio" name="question58" value="1"> Đồng tình một phần
                  <input type="radio" name="question58" value="2"> Tương đối đồng tình
                  <input type="radio" name="question58" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q59-label" for="question59">Bạn thường gặp khó khăn với deadline.</label><br><br>
                  <input type="radio" name="question59" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question59" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question59" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question59" value="0"> Trung lập
                  <input type="radio" name="question59" value="1"> Đồng tình một phần
                  <input type="radio" name="question59" value="2"> Tương đối đồng tình
                  <input type="radio" name="question59" value="3">Hoàn toàn đồng tình<br><br>
      <label id="q60-label" for="question60">Bạn cảm thấy tự tin rằng mọi chuyện sẽ diễn ra theo ý bạn.</label><br><br>
                  <input type="radio" name="question60" value="-3"> Hoàn toàn không đồng tình
                  <input type="radio" name="question60" value="-2"> Tương đối không đồng tình
                  <input type="radio" name="question60" value="-1"> Không đồng tình một phần
                  <input type="radio" name="question60" value="0"> Trung lập
                  <input type="radio" name="question60" value="1"> Đồng tình một phần
                  <input type="radio" name="question60" value="2"> Tương đối đồng tình
                  <input type="radio" name="question60" value="3">Hoàn toàn đồng tình<br><br>

</span>
<span lang="en">

      <label id="q1eng-label" for="question1">You regularly make new friends.</label><br><br>
            <input type="radio" name="question1" value="-3">Fully Disagree
            <input type="radio" name="question1" value="-2">Partially Disagree
            <input type="radio" name="question1" value="-1">Slightly Disagree
            <input type="radio" name="question1" value="0">Neutral
            <input type="radio" name="question1" value="1">Slightly Agree
            <input type="radio" name="question1" value="2">Partially Agree
            <input type="radio" name="question1" value="3">Fully Agree  <br><br>
      <label id="q2eng-label" for="question2">You spend a lot of your free time exploring various random topics that pique your interest.</label><br><br>
            <input type="radio" name="question2" value="-3">Fully Disagree
            <input type="radio" name="question2" value="-2">Partially Disagree
            <input type="radio" name="question2" value="-1">Slightly Disagree
            <input type="radio" name="question2" value="0">Neutral
            <input type="radio" name="question2" value="1">Slightly Agree
            <input type="radio" name="question2" value="2">Partially Agree
            <input type="radio" name="question2" value="3">Fully Agree <br><br>
      <label id="q3eng-label" for="question3">Seeing other people cry can easily make you feel like you want to cry too. </label><br><br>
            <input type="radio" name="question3" value="-3">Fully Disagree
            <input type="radio" name="question3" value="-2">Partially Disagree
            <input type="radio" name="question3" value="-1">Slightly Disagree
            <input type="radio" name="question3" value="0">Neutral
            <input type="radio" name="question3" value="1">Slightly Agree
            <input type="radio" name="question3" value="2">Partially Agree
            <input type="radio" name="question3" value="3">Fully Agree <br><br>
      <label id="q4eng-label" for="question4">You often make a backup plan for a backup plan.</label><br><br>
            <input type="radio" name="question4" value="-3">Fully Disagree
            <input type="radio" name="question4" value="-2">Partially Disagree
            <input type="radio" name="question4" value="-1">Slightly Disagree
            <input type="radio" name="question4" value="0">Neutral
            <input type="radio" name="question4" value="1">Slightly Agree
            <input type="radio" name="question4" value="2">Partially Agree
            <input type="radio" name="question4" value="3">Fully Agree <br><br>
      <label id="q5eng-label" for="question5">You usually stay calm, even under a lot of pressure.</label><br><br>
            <input type="radio" name="question5" value="-3">Fully Disagree
            <input type="radio" name="question5" value="-2">Partially Disagree
            <input type="radio" name="question5" value="-1">Slightly Disagree
            <input type="radio" name="question5" value="0">Neutral
            <input type="radio" name="question5" value="1">Slightly Agree
            <input type="radio" name="question5" value="2">Partially Agree
            <input type="radio" name="question5" value="3">Fully Agree <br><br>
      <label id="q6eng-label" for="question6">At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.</label><br><br>
            <input type="radio" name="question6" value="-3">Fully Disagree
            <input type="radio" name="question6" value="-2">Partially Disagree
            <input type="radio" name="question6" value="-1">Slightly Disagree
            <input type="radio" name="question6" value="0">Neutral
            <input type="radio" name="question6" value="1">Slightly Agree
            <input type="radio" name="question6" value="2">Partially Agree
            <input type="radio" name="question6" value="3">Fully Agree <br><br>
      <label id="q7eng-label" for="question7">You prefer to completely finish one project before starting another.</label><br><br>
            <input type="radio" name="question7" value="-3">Fully Disagree
            <input type="radio" name="question7" value="-2">Partially Disagree
            <input type="radio" name="question7" value="-1">Slightly Disagree
            <input type="radio" name="question7" value="0">Neutral
            <input type="radio" name="question7" value="1">Slightly Agree
            <input type="radio" name="question7" value="2">Partially Agree
            <input type="radio" name="question7" value="3">Fully Agree <br><br>
      <label id="q8eng-label" for="question8">You are very sentimental.</label><br><br>
            <input type="radio" name="question8" value="-3">Fully Disagree
            <input type="radio" name="question8" value="-2">Partially Disagree
            <input type="radio" name="question8" value="-1">Slightly Disagree
            <input type="radio" name="question8" value="0">Neutral
            <input type="radio" name="question8" value="1">Slightly Agree
            <input type="radio" name="question8" value="2">Partially Agree
            <input type="radio" name="question8" value="3">Fully Agree  <br><br>
      <label id="q9eng-label" for="question9">You like to use organizing tools like schedules and lists.</label><br><br>
            <input type="radio" name="question9" value="-3">Fully Disagree
            <input type="radio" name="question9" value="-2">Partially Disagree
            <input type="radio" name="question9" value="-1">Slightly Disagree
            <input type="radio" name="question9" value="0">Neutral
            <input type="radio" name="question9" value="1">Slightly Agree
            <input type="radio" name="question9" value="2">Partially Agree
            <input type="radio" name="question9" value="3">Fully Agree <br><br>
      <label id="q10eng-label" for="question10">Even a small mistake can cause you to doubt your overall abilities and knowledge.</label><br><br>
            <input type="radio" name="question10" value="-3">Fully Disagree
            <input type="radio" name="question10" value="-2">Partially Disagree
            <input type="radio" name="question10" value="-1">Slightly Disagree
            <input type="radio" name="question10" value="0">Neutral
            <input type="radio" name="question10" value="1">Slightly Agree
            <input type="radio" name="question10" value="2">Partially Agree
            <input type="radio" name="question10" value="3">Fully Agree <br><br>
      <label id="q11eng-label" for="question11">You feel comfortable just walking up to someone you find interesting and striking up a conversation.</label><br><br>
            <input type="radio" name="question11" value="-3">Fully Disagree
            <input type="radio" name="question11" value="-2">Partially Disagree
            <input type="radio" name="question11" value="-1">Slightly Disagree
            <input type="radio" name="question11" value="0">Neutral
            <input type="radio" name="question11" value="1">Slightly Agree
            <input type="radio" name="question11" value="2">Partially Agree
            <input type="radio" name="question11" value="3">Fully Agree <br><br>
      <label id="q12eng-label" for="question12">You are not too interested in discussing various interpretations and analyses of creative works.</label><br><br>
            <input type="radio" name="question12" value="-3">Fully Disagree
            <input type="radio" name="question12" value="-2">Partially Disagree
            <input type="radio" name="question12" value="-1">Slightly Disagree
            <input type="radio" name="question12" value="0">Neutral
            <input type="radio" name="question12" value="1">Slightly Agree
            <input type="radio" name="question12" value="2">Partially Agree
            <input type="radio" name="question12" value="3">Fully Agree <br><br>
      <label id="q13eng-label" for="question13">You are more inclined to follow your head than your heart.</label><br><br>
            <input type="radio" name="question13" value="-3">Fully Disagree
            <input type="radio" name="question13" value="-2">Partially Disagree
            <input type="radio" name="question13" value="-1">Slightly Disagree
            <input type="radio" name="question13" value="0">Neutral
            <input type="radio" name="question13" value="1">Slightly Agree
            <input type="radio" name="question13" value="2">Partially Agree
            <input type="radio" name="question13" value="3">Fully Agree <br><br>
      <label id="q14eng-label" for="question14">You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.</label><br><br>
            <input type="radio" name="question14" value="-3">Fully Disagree
            <input type="radio" name="question14" value="-2">Partially Disagree
            <input type="radio" name="question14" value="-1">Slightly Disagree
            <input type="radio" name="question14" value="0">Neutral
            <input type="radio" name="question14" value="1">Slightly Agree
            <input type="radio" name="question14" value="2">Partially Agree
            <input type="radio" name="question14" value="3">Fully Agree <br><br>
      <label id="q15eng-label" for="question15">You rarely worry about whether you make a good impression on people you meet.</label><br><br>
            <input type="radio" name="question15" value="-3">Fully Disagree
            <input type="radio" name="question15" value="-2">Partially Disagree
            <input type="radio" name="question15" value="-1">Slightly Disagree
            <input type="radio" name="question15" value="0">Neutral
            <input type="radio" name="question15" value="1">Slightly Agree
            <input type="radio" name="question15" value="2">Partially Agree
            <input type="radio" name="question15" value="3">Fully Agree <br><br>
      <label id="q16eng-label" for="question16">You enjoy participating in group activities.</label><br><br>
            <input type="radio" name="question16" value="-3">Fully Disagree
            <input type="radio" name="question16" value="-2">Partially Disagree
            <input type="radio" name="question16" value="-1">Slightly Disagree
            <input type="radio" name="question16" value="0">Neutral
            <input type="radio" name="question16" value="1">Slightly Agree
            <input type="radio" name="question16" value="2">Partially Agree
            <input type="radio" name="question16" value="3">Fully Agree <br><br>
      <label id="q17eng-label" for="question17">You like books and movies that make you come up with your own interpretation of the ending.</label><br><br>
            <input type="radio" name="question17" value="-3">Fully Disagree
            <input type="radio" name="question17" value="-2">Partially Disagree
            <input type="radio" name="question17" value="-1">Slightly Disagree
            <input type="radio" name="question17" value="0">Neutral
            <input type="radio" name="question17" value="1">Slightly Agree
            <input type="radio" name="question17" value="2">Partially Agree
            <input type="radio" name="question17" value="3">Fully Agree  <br><br>
      <label id="q18eng-label" for="question18">Your happiness comes more from helping others accomplish things than your own accomplishments.</label><br><br>
            <input type="radio" name="question18" value="-3">Fully Disagree
            <input type="radio" name="question18" value="-2">Partially Disagree
            <input type="radio" name="question18" value="-1">Slightly Disagree
            <input type="radio" name="question18" value="0">Neutral
            <input type="radio" name="question18" value="1">Slightly Agree
            <input type="radio" name="question18" value="2">Partially Agree
            <input type="radio" name="question18" value="3">Fully Agree <br><br>
      <label id="q19eng-label" for="question19">You are interested in so many things that you find it difficult to choose what to try next.</label><br><br>
            <input type="radio" name="question19" value="-3">Fully Disagree
            <input type="radio" name="question19" value="-2">Partially Disagree
            <input type="radio" name="question19" value="-1">Slightly Disagree
            <input type="radio" name="question19" value="0">Neutral
            <input type="radio" name="question19" value="1">Slightly Agree
            <input type="radio" name="question19" value="2">Partially Agree
            <input type="radio" name="question19" value="3">Fully Agree <br><br>
      <label id="q20eng-label" for="question20">You are prone to worrying that things will take a turn for the worse.</label><br><br>
            <input type="radio" name="question20" value="-3">Fully Disagree
            <input type="radio" name="question20" value="-2">Partially Disagree
            <input type="radio" name="question20" value="-1">Slightly Disagree
            <input type="radio" name="question20" value="0">Neutral
            <input type="radio" name="question20" value="1">Slightly Agree
            <input type="radio" name="question20" value="2">Partially Agree
            <input type="radio" name="question20" value="3">Fully Agree <br><br>
      <label id="q21eng-label" for="question21">You avoid leadership roles in group settings.</label><br><br>
            <input type="radio" name="question21" value="-3">Fully Disagree
            <input type="radio" name="question21" value="-2">Partially Disagree
            <input type="radio" name="question21" value="-1">Slightly Disagree
            <input type="radio" name="question21" value="0">Neutral
            <input type="radio" name="question21" value="1">Slightly Agree
            <input type="radio" name="question21" value="2">Partially Agree
            <input type="radio" name="question21" value="3">Fully Agree <br><br>
      <label id="q22eng-label" for="question22">You are definitely not an artistic type of person.</label><br><br>
            <input type="radio" name="question22" value="-3">Fully Disagree
            <input type="radio" name="question22" value="-2">Partially Disagree
            <input type="radio" name="question22" value="-1">Slightly Disagree
            <input type="radio" name="question22" value="0">Neutral
            <input type="radio" name="question22" value="1">Slightly Agree
            <input type="radio" name="question22" value="2">Partially Agree
            <input type="radio" name="question22" value="3">Fully Agree <br><br>
      <label id="q23eng-label" for="question23">You think the world would be a better place if people relied more on rationality and less on their feelings.</label><br><br>
            <input type="radio" name="question23" value="-3">Fully Disagree
            <input type="radio" name="question23" value="-2">Partially Disagree
            <input type="radio" name="question23" value="-1">Slightly Disagree
            <input type="radio" name="question23" value="0">Neutral
            <input type="radio" name="question23" value="1">Slightly Agree
            <input type="radio" name="question23" value="2">Partially Agree
            <input type="radio" name="question23" value="3">Fully Agree <br><br>
      <label id="q24eng-label" for="question24">You prefer to do your chores before allowing yourself to relax.</label><br><br>
            <input type="radio" name="question24" value="-3">Fully Disagree
            <input type="radio" name="question24" value="-2">Partially Disagree
            <input type="radio" name="question24" value="-1">Slightly Disagree
            <input type="radio" name="question24" value="0">Neutral
            <input type="radio" name="question24" value="1">Slightly Agree
            <input type="radio" name="question24" value="2">Partially Agree
            <input type="radio" name="question24" value="3">Fully Agree <br><br>
      <label id="q25eng-label" for="question25">You enjoy watching people argue.</label><br><br>
            <input type="radio" name="question25" value="-3">Fully Disagree
            <input type="radio" name="question25" value="-2">Partially Disagree
            <input type="radio" name="question25" value="-1">Slightly Disagree
            <input type="radio" name="question25" value="0">Neutral
            <input type="radio" name="question25" value="1">Slightly Agree
            <input type="radio" name="question25" value="2">Partially Agree
            <input type="radio" name="question25" value="3">Fully Agree <br><br>
      <label id="q26eng-label" for="question26">You tend to avoid drawing attention to yourself.</label><br><br>
            <input type="radio" name="question26" value="-3">Fully Disagree
            <input type="radio" name="question26" value="-2">Partially Disagree
            <input type="radio" name="question26" value="-1">Slightly Disagree
            <input type="radio" name="question26" value="0">Neutral
            <input type="radio" name="question26" value="1">Slightly Agree
            <input type="radio" name="question26" value="2">Partially Agree
            <input type="radio" name="question26" value="3">Fully Agree <br><br>
      <label id="q27eng-label" for="question27">Your mood can change very quickly.</label><br><br>
            <input type="radio" name="question27" value="-3">Fully Disagree
            <input type="radio" name="question27" value="-2">Partially Disagree
            <input type="radio" name="question27" value="-1">Slightly Disagree
            <input type="radio" name="question27" value="0">Neutral
            <input type="radio" name="question27" value="1">Slightly Agree
            <input type="radio" name="question27" value="2">Partially Agree
            <input type="radio" name="question27" value="3">Fully Agree <br><br>
      <label id="q28eng-label" for="question28">You lose patience with people who are not as efficient as you.</label><br><br>
            <input type="radio" name="question28" value="-3">Fully Disagree
            <input type="radio" name="question28" value="-2">Partially Disagree
            <input type="radio" name="question28" value="-1">Slightly Disagree
            <input type="radio" name="question28" value="0">Neutral
            <input type="radio" name="question28" value="1">Slightly Agree
            <input type="radio" name="question28" value="2">Partially Agree
            <input type="radio" name="question28" value="3">Fully Agree <br><br>
      <label id="q29eng-label" for="question29">You often end up doing things at the last possible moment.</label><br><br>
            <input type="radio" name="question29">Fully Disagree
            <input type="radio" name="question29" value="-2">Partially Disagree
            <input type="radio" name="question29" value="-1">Slightly Disagree
            <input type="radio" name="question29" value="0">Neutral
            <input type="radio" name="question29" value="1">Slightly Agree
            <input type="radio" name="question29" value="2">Partially Agree
            <input type="radio" name="question29" value="3">Fully Agree <br><br>
      <label id="q30eng-label" for="question30">You have always been fascinated by the question of what, if anything, happens after death.</label><br><br>
            <input type="radio" name="question30" value="-3">Fully Disagree
            <input type="radio" name="question30" value="-2">Partially Disagree
            <input type="radio" name="question30" value="-1">Slightly Disagree
            <input type="radio" name="question30" value="0">Neutral
            <input type="radio" name="question30" value="1">Slightly Agree
            <input type="radio" name="question30" value="2">Partially Agree
            <input type="radio" name="question30" value="3">Fully Agree <br><br>
      <label id="q31eng-label" for="question31">You usually prefer to be around others rather than on your own.</label><br><br>
            <input type="radio" name="question31" value="-3">Fully Disagree
            <input type="radio" name="question31" value="-2">Partially Disagree
            <input type="radio" name="question31" value="-1">Slightly Disagree
            <input type="radio" name="question31" value="0">Neutral
            <input type="radio" name="question31" value="1">Slightly Agree
            <input type="radio" name="question31" value="2">Partially Agree
            <input type="radio" name="question31" value="3">Fully Agree <br><br>
      <label id="q32eng-label" for="question32">You become bored or lose interest when the discussion gets highly theoretical.</label><br><br>
            <input type="radio" name="question32" value="-3">Fully Disagree
            <input type="radio" name="question32" value="-2">Partially Disagree
            <input type="radio" name="question32" value="-1">Slightly Disagree
            <input type="radio" name="question32" value="0">Neutral
            <input type="radio" name="question32" value="1">Slightly Agree
            <input type="radio" name="question32" value="2">Partially Agree
            <input type="radio" name="question32" value="3">Fully Agree <br><br>
      <label id="q33eng-label" for="question33">You find it easy to empathize with a person whose experiences are very different from yours.</label><br><br>
            <input type="radio" name="question33" value="-3">Fully Disagree
            <input type="radio" name="question33" value="-2">Partially Disagree
            <input type="radio" name="question33" value="-1">Slightly Disagree
            <input type="radio" name="question33" value="0">Neutral
            <input type="radio" name="question33" value="1">Slightly Agree
            <input type="radio" name="question33" value="2">Partially Agree
            <input type="radio" name="question33" value="3">Fully Agree <br><br>
      <label id="q34eng-label" for="question34">You usually postpone finalizing decisions for as long as possible.</label><br><br>
            <input type="radio" name="question34" value="-3">Fully Disagree
            <input type="radio" name="question34" value="-2">Partially Disagree
            <input type="radio" name="question34" value="-1">Slightly Disagree
            <input type="radio" name="question34" value="0">Neutral
            <input type="radio" name="question34" value="1">Slightly Agree
            <input type="radio" name="question34" value="2">Partially Agree
            <input type="radio" name="question34" value="3">Fully Agree <br><br>
      <label id="q35eng-label" for="question35">You rarely second-guess the choices that you have made.</label><br><br>
            <input type="radio" name="question35" value="-3">Fully Disagree
            <input type="radio" name="question35" value="-2">Partially Disagree
            <input type="radio" name="question35" value="-1">Slightly Disagree
            <input type="radio" name="question35" value="0">Neutral
            <input type="radio" name="question35" value="1">Slightly Agree
            <input type="radio" name="question35" value="2">Partially Agree
            <input type="radio" name="question35" value="3">Fully Agree <br><br>
      <label id="q36eng-label" for="question36">After a long and exhausting week, a lively social event is just what you need.</label><br><br>
            <input type="radio" name="question36" value="-3">Fully Disagree
            <input type="radio" name="question36" value="-2">Partially Disagree
            <input type="radio" name="question36" value="-1">Slightly Disagree
            <input type="radio" name="question36" value="0">Neutral
            <input type="radio" name="question36" value="1">Slightly Agree
            <input type="radio" name="question36" value="2">Partially Agree
            <input type="radio" name="question36" value="3">Fully Agree <br><br>
      <label id="q37eng-label" for="question37">You enjoy going to art museums.</label><br><br>
            <input type="radio" name="question37" value="-3">Fully Disagree
            <input type="radio" name="question37" value="-2">Partially Disagree
            <input type="radio" name="question37" value="-1">Slightly Disagree
            <input type="radio" name="question37" value="0">Neutral
            <input type="radio" name="question37" value="1">Slightly Agree
            <input type="radio" name="question37" value="2">Partially Agree
            <input type="radio" name="question37" value="3">Fully Agree <br><br>
      <label id="q38eng-label" for="question38">You often have a hard time understanding other people’s feelings.</label><br><br>
            <input type="radio" name="question38" value="-3">Fully Disagree
            <input type="radio" name="question38" value="-2">Partially Disagree
            <input type="radio" name="question38" value="-1">Slightly Disagree
            <input type="radio" name="question38" value="0">Neutral
            <input type="radio" name="question38" value="1">Slightly Agree
            <input type="radio" name="question38" value="2">Partially Agree
            <input type="radio" name="question38" value="3">Fully Agree <br><br>
      <label id="q39eng-label" for="question39">You like to have a to-do list for each day.</label><br><br>
            <input type="radio" name="question39" value="-3">Fully Disagree
            <input type="radio" name="question39" value="-2">Partially Disagree
            <input type="radio" name="question39" value="-1">Slightly Disagree
            <input type="radio" name="question39" value="0">Neutral
            <input type="radio" name="question39" value="1">Slightly Agree
            <input type="radio" name="question39" value="2">Partially Agree
            <input type="radio" name="question39" value="3">Fully Agree <br><br>
      <label id="q40eng-label" for="question40">You rarely feel insecure.</label><br><br>
            <input type="radio" name="question40" value="-3">Fully Disagree
            <input type="radio" name="question40" value="-2">Partially Disagree
            <input type="radio" name="question40" value="-1">Slightly Disagree
            <input type="radio" name="question40" value="0">Neutral
            <input type="radio" name="question40" value="1">Slightly Agree
            <input type="radio" name="question40" value="2">Partially Agree
            <input type="radio" name="question40" value="3">Fully Agree <br><br>
      <label id="q41eng-label" for="question41">You avoid making phone calls.</label><br><br>
            <input type="radio" name="question41" value="-3">Fully Disagree
            <input type="radio" name="question41" value="-2">Partially Disagree
            <input type="radio" name="question41" value="-1">Slightly Disagree
            <input type="radio" name="question41" value="0">Neutral
            <input type="radio" name="question41" value="1">Slightly Agree
            <input type="radio" name="question41" value="2">Partially Agree
            <input type="radio" name="question41" value="3">Fully Agree <br><br>
      <label id="q42eng-label" for="question42">You often spend a lot of time trying to understand views that are very different from your own.</label><br><br>
            <input type="radio" name="question42" value="-3">Fully Disagree
            <input type="radio" name="question42" value="-2">Partially Disagree
            <input type="radio" name="question42" value="-1">Slightly Disagree
            <input type="radio" name="question42" value="0">Neutral
            <input type="radio" name="question42" value="1">Slightly Agree
            <input type="radio" name="question42" value="2">Partially Agree
            <input type="radio" name="question42" value="3">Fully Agree <br><br>
      <label id="q43eng-label" for="question43">In your social circle, you are often the one who contacts your friends and initiates activities.</label><br><br>
            <input type="radio" name="question43" value="-3">Fully Disagree
            <input type="radio" name="question43" value="-2">Partially Disagree
            <input type="radio" name="question43" value="-1">Slightly Disagree
            <input type="radio" name="question43" value="0">Neutral
            <input type="radio" name="question43" value="1">Slightly Agree
            <input type="radio" name="question43" value="2">Partially Agree
            <input type="radio" name="question43" value="3">Fully Agree  <br><br>
      <label id="q44eng-label" for="question44">If your plans are interrupted, your top priority is to get back on track as soon as possible.</label><br><br>
            <input type="radio" name="question44" value="-3">Fully Disagree
            <input type="radio" name="question44" value="-2">Partially Disagree
            <input type="radio" name="question44" value="-1">Slightly Disagree
            <input type="radio" name="question44" value="0">Neutral
            <input type="radio" name="question44" value="1">Slightly Agree
            <input type="radio" name="question44" value="2">Partially Agree
            <input type="radio" name="question44" value="3">Fully Agree <br><br>
      <label id="q45eng-label" for="question45">You are still bothered by mistakes that you made a long time ago.</label><br><br>
            <input type="radio" name="question45" value="-3">Fully Disagree
            <input type="radio" name="question45" value="-2">Partially Disagree
            <input type="radio" name="question45" value="-1">Slightly Disagree
            <input type="radio" name="question45" value="0">Neutral
            <input type="radio" name="question45" value="1">Slightly Agree
            <input type="radio" name="question45" value="2">Partially Agree
            <input type="radio" name="question45" value="3">Fully Agree <br><br>
      <label id="q46eng-label" for="question46">You rarely contemplate the reasons for human existence or the meaning of life.</label><br><br>
            <input type="radio" name="question46" value="-3">Fully Disagree
            <input type="radio" name="question46" value="-2">Partially Disagree
            <input type="radio" name="question46" value="-1">Slightly Disagree
            <input type="radio" name="question46" value="0">Neutral
            <input type="radio" name="question46" value="1">Slightly Agree
            <input type="radio" name="question46" value="2">Partially Agree
            <input type="radio" name="question46" value="3">Fully Agree <br><br>
      <label id="q47eng-label" for="question47">Your emotions control you more than you control them.</label><br><br>
            <input type="radio" name="question47" value="-3">Fully Disagree
            <input type="radio" name="question47" value="-2">Partially Disagree
            <input type="radio" name="question47" value="-1">Slightly Disagree
            <input type="radio" name="question47" value="0">Neutral
            <input type="radio" name="question47" value="1">Slightly Agree
            <input type="radio" name="question47" value="2">Partially Agree
            <input type="radio" name="question47" value="3">Fully Agree <br><br>
      <label id="q48eng-label" for="question48">You take great care not to make people look bad, even when it is completely their fault.</label><br><br>
            <input type="radio" name="question48" value="-3">Fully Disagree
            <input type="radio" name="question48" value="-2">Partially Disagree
            <input type="radio" name="question48" value="-1">Slightly Disagree
            <input type="radio" name="question48" value="0">Neutral
            <input type="radio" name="question48" value="1">Slightly Agree
            <input type="radio" name="question48" value="2">Partially Agree
            <input type="radio" name="question48" value="3">Fully Agree <br><br>
      <label id="q49eng-label" for="question49">Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.</label><br><br>
            <input type="radio" name="question49" value="-3">Fully Disagree
            <input type="radio" name="question49" value="-2">Partially Disagree
            <input type="radio" name="question49" value="-1">Slightly Disagree
            <input type="radio" name="question49" value="0">Neutral
            <input type="radio" name="question49" value="1">Slightly Agree
            <input type="radio" name="question49" value="2">Partially Agree
            <input type="radio" name="question49" value="3">Fully Agree <br><br>
      <label id="q50eng-label" for="question50">When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.</label><br><br>
            <input type="radio" name="question50" value="-3">Fully Disagree
            <input type="radio" name="question50" value="-2">Partially Disagree
            <input type="radio" name="question50" value="-1">Slightly Disagree
            <input type="radio" name="question50" value="0">Neutral
            <input type="radio" name="question50" value="1">Slightly Agree
            <input type="radio" name="question50" value="2">Partially Agree
            <input type="radio" name="question50" value="3">Fully Agree <br><br>
      <label id="q51eng-label" for="question51">You would love a job that requires you to work alone most of the time.</label><br><br>
            <input type="radio" name="question51" value="-3">Fully Disagree
            <input type="radio" name="question51" value="-2">Partially Disagree
            <input type="radio" name="question51" value="-1">Slightly Disagree
            <input type="radio" name="question51" value="0">Neutral
            <input type="radio" name="question51" value="1">Slightly Agree
            <input type="radio" name="question51" value="2">Partially Agree
            <input type="radio" name="question51" value="3">Fully Agree <br><br>
      <label id="q52eng-label" for="question52">You believe that pondering abstract philosophical questions is a waste of time.</label><br><br>
            <input type="radio" name="question52" value="-3">Fully Disagree
            <input type="radio" name="question52" value="-2">Partially Disagree
            <input type="radio" name="question52" value="-1">Slightly Disagree
            <input type="radio" name="question52" value="0">Neutral
            <input type="radio" name="question52" value="1">Slightly Agree
            <input type="radio" name="question52" value="2">Partially Agree
            <input type="radio" name="question52" value="3">Fully Agree <br><br>
      <label id="q53eng-label" for="question53">You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.</label><br><br>
            <input type="radio" name="question53" value="-3">Fully Disagree
            <input type="radio" name="question53" value="-2">Partially Disagree
            <input type="radio" name="question53" value="-1">Slightly Disagree
            <input type="radio" name="question53" value="0">Neutral
            <input type="radio" name="question53" value="1">Slightly Agree
            <input type="radio" name="question53" value="2">Partially Agree
            <input type="radio" name="question53" value="3">Fully Agree <br><br>
      <label id="q54eng-label" for="question54">You know at first glance how someone is feeling.</label><br><br>
            <input type="radio" name="question54" value="-3">Fully Disagree
            <input type="radio" name="question54" value="-2">Partially Disagree
            <input type="radio" name="question54" value="-1">Slightly Disagree
            <input type="radio" name="question54" value="0">Neutral
            <input type="radio" name="question54" value="1">Slightly Agree
            <input type="radio" name="question54" value="2">Partially Agree
            <input type="radio" name="question54" value="3">Fully Agree <br><br>
      <label id="q55eng-label" for="question55">You often feel overwhelmed.</label><br><br>
            <input type="radio" name="question55" value="-3">Fully Disagree
            <input type="radio" name="question55" value="-2">Partially Disagree
            <input type="radio" name="question55" value="-1">Slightly Disagree
            <input type="radio" name="question55" value="0">Neutral
            <input type="radio" name="question55" value="1">Slightly Agree
            <input type="radio" name="question55" value="2">Partially Agree
            <input type="radio" name="question55" value="3">Fully Agree <br><br>
      <label id="q56eng-label" for="question56">You complete things methodically without skipping over any steps.</label><br><br>
            <input type="radio" name="question56" value="-3">Fully Disagree
            <input type="radio" name="question56" value="-2">Partially Disagree
            <input type="radio" name="question56" value="-1">Slightly Disagree
            <input type="radio" name="question56" value="0">Neutral
            <input type="radio" name="question56" value="1">Slightly Agree
            <input type="radio" name="question56" value="2">Partially Agree
            <input type="radio" name="question56" value="3">Fully Agree <br><br>
      <label id="q57eng-label" for="question57">You are very intrigued by things labeled as controversial.</label><br><br>
            <input type="radio" name="question57" value="-3">Fully Disagree
            <input type="radio" name="question57" value="-2">Partially Disagree
            <input type="radio" name="question57" value="-1">Slightly Disagree
            <input type="radio" name="question57" value="0">Neutral
            <input type="radio" name="question57" value="1">Slightly Agree
            <input type="radio" name="question57" value="2">Partially Agree
            <input type="radio" name="question57" value="3">Fully Agree <br><br>
      <label id="q58eng-label" for="question58">You would pass along a good opportunity if you thought someone else needed it more.</label><br><br>
            <input type="radio" name="question58" value="-3">Fully Disagree
            <input type="radio" name="question58" value="-2">Partially Disagree
            <input type="radio" name="question58" value="-1">Slightly Disagree
            <input type="radio" name="question58" value="0">Neutral
            <input type="radio" name="question58" value="1">Slightly Agree
            <input type="radio" name="question58" value="2">Partially Agree
            <input type="radio" name="question58" value="3">Fully Agree <br><br>
      <label id="q59eng-label" for="question59">You struggle with deadlines.</label><br><br>
            <input type="radio" name="question59" value="-3">Fully Disagree
            <input type="radio" name="question59" value="-2">Partially Disagree
            <input type="radio" name="question59" value="-1">Slightly Disagree
            <input type="radio" name="question59" value="0">Neutral
            <input type="radio" name="question59" value="1">Slightly Agree
            <input type="radio" name="question59" value="2">Partially Agree
            <input type="radio" name="question59" value="3">Fully Agree <br><br>
      <label id="q60eng-label" for="question60">You feel confident that things will work out for you.</label><br><br>
            <input type="radio" name="question60" value="-3">Fully Disagree
            <input type="radio" name="question60" value="-2">Partially Disagree
            <input type="radio" name="question60" value="-1">Slightly Disagree
            <input type="radio" name="question60" value="0">Neutral
            <input type="radio" name="question60" value="1">Slightly Agree
            <input type="radio" name="question60" value="2">Partially Agree
            <input type="radio" name="question60" value="3">Fully Agree <br><br>
      </span>

<button type="submit" class="btn-submit" onclick=window.location.href="{{ url_for('predict') }}">Submit</button>
</form>
<script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
<script>
$('[lang]').hide(); // hide all lang attributes on start.
      $('[lang="vie"]').show(); // show just Korean text (you can change it)
      $('#lang-switch').change(function () { // put onchange event when user select option from select
         var lang = $(this).val(); // decide which language to display using switch case. The rest is obvious (i think)
switch (lang) {
case 'en':
$('[lang]').hide();
$('[lang="en"]').show();
break;
case 'vie':
$('[lang]').hide();
$('[lang="vie"]').show();
break;
default:
$('[lang]').hide();
$('[lang="vie"]').show();
}
});
</script>
</html>
