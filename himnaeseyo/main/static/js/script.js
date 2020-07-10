function change_bg(bg_img) {
    var context = document.getElementById('div_input_text')
    bg_url = '/static/images/' + bg_img + '.jpg'
    context.style.backgroundImage = "url('"+bg_url+"')"
}

function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

    if(elmnt) {
        elmnt.addEventListener('mousedown', e=> {
            
            e = e || window.event;
            
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
        })

        elmnt.onmousedown = dragMouseDown;

        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            // set the element's new position:

            elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
            elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }

        function closeDragElement() {
            /* stop moving when mouse button is released:*/
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
}


$(function () {
    $("#save").click(function () {
        html2canvas($('#div_input_text').get(0)).then(function (canvas) {

            var data = canvas.toDataURL();

            // ajax통신
            $.ajax({
                type: 'POST',
                url: '/card/save/',
                data: {
                    data: data
                },
                success: function (result) {
                    var filename = result['filename'];
                    console.log(filename + ' 완료')
                    window.location.href = '/';
                },
                error: function (e) {
                    alert("에러발생");
                }
            });

        });
    });
});


function setFontColor(){
    var input_text = document.getElementById('input_text')
    var fontColor = document.getElementById('fontColor')
    input_text.style.color = fontColor.value
    // console.log(fontColor.value)
}


var fontSizeValue = 30
function fontSizeUp(){
    var input_text = document.getElementById('input_text')
    // console.log(input_text.style.fontSize)
    fontSizeValue +=10
    input_text.style.fontSize = fontSizeValue+'pt'
    // console.log("확대")
}

function fontSizeDown(){
    var input_text = document.getElementById('input_text')
    fontSizeValue -= 10
    input_text.style.fontSize = fontSizeValue + 'pt'
    // console.log("축소")
}

var slideIndex = 1;
showDivs(slideIndex);
function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}