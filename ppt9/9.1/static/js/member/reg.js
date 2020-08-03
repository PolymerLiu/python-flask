;
var member_reg_ops = {
  init: function () {
    this.eventBind()
  },
  eventBind: function () {
    $(".reg-wrap .do-reg").click(function () {
      var btn_target = $(this)
      if (btn_target.hasClass('disabled')) {
        console.log('================稍后再点击');
      }
      var login_name = $(".reg-wrap input[name=login_name]").val()
      var login_pw1 = $(".reg-wrap input[name=login_pw1]").val()
      var login_pw2 = $(".reg-wrap input[name=login_pw2]").val()
      if (login_name == undefined || login_name.length<1) {
        alert('请输入正确的登录用户名~~')
        return
      }
      if (login_pw1 == undefined || login_pw1.length<6) {
        alert('请输入正确的登录密码~~，并且长度不能小于6个字符')
        return
      }

      if (login_pw2 == undefined || login_pw1 !==login_pw2) {
        alert('请输入正确的确认密码~~')
        return
      }
      // btn_target.addClass('disabled')
      $.ajax({
        url:'/member/reg',
        type: 'POST',
        data: {
          login_name,
          login_pw1,
          login_pw2,
        },
        dataType:'json',
        success:function (res) {
        btn_target.removeClass('disabled')
        },
        
      })

    })
  }
}

$(document).ready(function () {
  member_reg_ops.init()
})