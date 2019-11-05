'use strict'
var url = 'http://95.163.202.160:8080';
const getJSON = function(url) {
  const promise = new Promise(function(resolve, reject) {
    var request = new XMLHttpRequest(); // 新建Microsoft.XMLHTTP对象
      request.onreadystatechange = function() { // 状态发生变化时，函数被回调
        if (request.readyState === 4) { // 成功完成
          // 判断响应结果:
          if (request.status === 200) {
              // 成功，通过responseText拿到响应的文本:
              resolve(request.responseText);
          } else {
              // 失败，根据响应码判断失败原因:
              reject(request.status);
          }
        } else {
            // HTTP请求还在继续...
        }
      }
      // 发送请求:
      request.open('GET', url);
      request.send();
    });

  return promise;
};

getJSON(url).then(function(json) {
  alert('Contents: ' + json);
}, function(error) {
  alert('出错了', error);
});

alert("还是先输出这个，所以不是从上到下的。");
