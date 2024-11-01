$(function (){
    function bindCapchaBtnClick(){
        $("#captcha-btn").click(function (event){
            let $this = $(this);
            let email = $("input[name='email']").val();
            if(!email){
                alert('请先输入邮箱！');
                return;
            }
            //取消按钮点击事件
            $this.off('click');

            //ajax请求
            $.ajax('captcha?email=' + email,{
                method : 'GET',
                success: function(result){
                    if(result['code']==200){
                        alert('邮箱发送成功')
                    }else{
                        alert(result['message'])
                    }
                },
                fail : function (error){
                    console.log(error)
                }
            })

            //倒计时
            let countdown = 60;
            let timer = setInterval(function(){
                if (countdown <= 0) {
                    //清掉计时器
                    $this.text('获取验证码');
                    clearInterval(timer)
                    //重新绑定点击事件
                    bindCapchaBtnClick();
                } else {
                    $this.text(countdown + 's')
                    countdown--;
                }
            }, 1000);
        });
    }
    bindCapchaBtnClick();
});
