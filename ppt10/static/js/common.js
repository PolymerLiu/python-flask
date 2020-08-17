/**
 * Created by ${刘家福} on ${2017.05.18}.
 */
;
var common_ops = {
    buildUrl: function (path,params) {
        // params = {'test':'abc','sort':'def'}
        // ?test=abc&sort=def
        var url = ''+path
        var _param_url = ''
        if(params){
            _param_url = Object.keys(params).map(function (k) {
                return[encodeURIComponent(k),encodeURIComponent(params[k])].join('=')
            }).join('&')
        }
        _param_url = '?'+_param_url
        return url+_param_url
    },
    alert: function (msg, cb) {
        layer.alert(msg,{
            yes: function (index) {
                if(typeof  cb =='function'){
                    cb()
                }
                layer.close(index)
                
            }
        })
    }
}