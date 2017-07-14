var myImage = document.getElementsByName('change_image');
console.log(myImage);
function changeImage() {
    
    if (myImage.src.match("abaksoup")) {
        myImage.src = "abak.JPG";
    } else {
        myImage.src = "abaksoup.JPG";
    }
}
//var imgChanger = document,getElementById("myImage");
