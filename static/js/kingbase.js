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
}

