var img = document.getElementById("progressbar")
var progressInt = 2
function changePicture(progressInt) {
    switch (progressInt){
        case 0:
            img.src = "{% static "PFFU/img/progressbar0.png" %}"
            break
        case 1:
            img.src = "{% static "PFFU/img/progressbar1.png" %}"
            break
        case 2:
            img.src = "{% static "PFFU/img/progressbar2.png" %}"
            break
        case 3:
            img.src = "{% static "PFFU/img/progressbar3.png" %}"
            break
        case 4:
            img.src = "{% static "PFFU/img/progressbar4.png" %}"
            break
        case 5:
            img.src = "{% static "PFFU/img/progressbar5.png" %}"
            break
        case 6:
            img.src = "{% static "PFFU/img/progressbar6.png" %}"
            break
    }
}
changePicture(progressInt)