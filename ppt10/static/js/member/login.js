;
var member_login_ops = {
    init: function () {
        this.eventBind()
    },
    eventBind: function () {
        $(".login-wrap .do-login").click(function () {
            var btn_target = $(this)
            if (btn_target.hasClass('disabled')) {
                console.log('================稍后再点击');
            }
            var login_name = $(".login-wrap input[name=login_name]").val()
            var login_pwd = $(".login-wrap input[name=login_pwd]").val()
            if (login_name == undefined || login_name.length < 1) {
                common_ops.alert('请输入正确的登录用户名~~')
                return
            }
            if (login_pwd == undefined || login_pwd.length < 6) {
                common_ops.alert('请输入正确的登录密码~~，并且长度不能小于6个字符')
                return
            }
            // btn_target.addClass('disabled')
            $.ajax({
                url: common_ops.buildUrl('/member/login'),
                type: 'POST',
                data: {
                    login_name,
                    login_pwd,
                },
                dataType: 'json',
                success: function (res) {
                    var cb = null
                    if(res.code ==200){
                        cb = function () {
                            window.location.href = common_ops.buildUrl('/')
                        }
                    }
                    common_ops.alert(res.msg,cb)
                    btn_target.removeClass('disabled')
                },

            })

        })
    }
}

$(document).ready(function () {
    member_login_ops.init()
})