var picArr=new Array("C:\\Users\\April\\OneDrive\\文件\\Visual-inspections\\templates\\photo\\ph1.jpg","C:\\Users\\April\\OneDrive\\文件\\Visual-inspections\\templates\\photo\\ph2.jpg","C:\\Users\\April\\OneDrive\\文件\\Visual-inspections\\templates\\photo\\ph3.jpg","C:\\Users\\April\\OneDrive\\文件\\Visual-inspections\\templates\\photo\\ph4.jpg");
var index=0;
function confirm(){ 
    index++;
    if(index==picArr.length){ 
        index=0;
    }
    document.getElementById("pic").src=picArr[index];
}