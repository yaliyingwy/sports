function valid(){
	name=$("#name").val().trim();
	passwd=$("#passwd").val().trim();
	if (name == ""||passwd == "")
	{
		alert("用户名或密码不能为空");
		return;
	}
	$.post("/movie/login/",
			{name:name,passwd:passwd},
			function(data){
				if (data == "success")
	{
		window.location.reload();
	}
				else
	{
		alert(data);
	}
			});
}

function showBlock(){
	$("#comment").append("<div>hello</div>");
}
function postComment(username,movieid,cont,pid){
	content=$("#" + cont).val().trim();
	if (content == "")
	{
		alert("内容不能为空");
		return;
	}
	$.post("/movie/comment/add",
			{username:username,movieid:movieid,content:content,pid:pid},
			function(data){
				if (data == "success")
	{
	    $("#" + cont).val('');
		window.location.reload();
	}
				else
	{
		alert(data);
	}
			});
}

