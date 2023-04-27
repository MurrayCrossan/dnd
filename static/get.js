var arrayofNames = ""
function getList(option) {
    var httpRequest = new XMLHttpRequest()

    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                var names = httpRequest.responseText.split(",")
                arrayofNames = names
                console.log(names)
                return names
                }
            }
            else {
                //console.log("There was an issue")
            }
        }
    
    //var filename = file
    httpRequest.open('GET', 'http://localhost/info.php?q=' + option, false)
    httpRequest.send()
}

function go() {
    var option = document.getElementById("select")
    var text = getList(option.value);
}