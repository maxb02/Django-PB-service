$(document).ready(function () {


    var initAddIcons = function () {
        var matchTypes = "[href*='zip'], [href*='7z'], [href*='rar'], [href*='exe']";
        $(".container a[href*='ftp'], " + matchTypes).prepend("<i class=\"fa fa-download\" aria-hidden=\"true\">&nbsp;");
        $(".container a[href*='ftp'], " + matchTypes).append("</i>");
        $(".container a[href*='http']:not(" + matchTypes + ", :has(img))").prepend("<i class =\"fa fa-external-link-square\" aria-hidden=\"true\">&nbsp;");
        $(".container a[href*='http']:not(" + matchTypes + ", :has(img))").append("</i>");
    }

    var initFavcyBoxImg = function () {
        $(".box img").each(function () {
            $(this).fancybox({
                //'hideOnContentClick': true,
                'href': $(this).attr('src')
            });
        });
    }

    initAddIcons();
    initFavcyBoxImg();


});