$("#file0").change(function(){
        var objUrl = getObjectURL(this.files[0]) ;//获取文件信息
        console.log("objUrl = "+objUrl);
            if (objUrl) {
                  $("#img0").attr("src", objUrl);
            }
        });


        function getObjectURL(file) {
            var url = null;
            if(window.createObjectURL!=undefined) {
                url = window.createObjectURL(file) ;
            }else if (window.URL!=undefined) { // mozilla(firefox)
                url = window.URL.createObjectURL(file) ;
            }else if (window.webkitURL!=undefined) { // webkit or chrome
                url = window.webkitURL.createObjectURL(file) ;
            }
            return url ;
        }

        function DrawImage(ImgD, iwidth, iheight) {
            //参数(图片,允许的宽度,允许的高度)
            var image = new Image();
            image.src = ImgD.src;
            if (image.width > 0 && image.height > 0) {
                if (image.width / image.height >= iwidth / iheight) {
                    if (image.width > iwidth) {
                       ImgD.width = iwidth;
                       ImgD.height = (image.height * iwidth) / image.width;
                    }
                    else {
                        ImgD.width = image.width;
                        ImgD.height = image.height;
                    }
                    ImgD.alt = image.width + "×" + image.height;
                }
                else {
                    if (image.height > iheight) {
                        ImgD.height = iheight;
                        ImgD.width = (image.width * iheight) / image.height;
                    }
                    else {
                        ImgD.width = image.width;
                        ImgD.height = image.height;
                    }
                    ImgD.alt = image.width + "×" + image.height;
                }
            }
        }