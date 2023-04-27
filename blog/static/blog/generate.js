//Count of total seats generated
var arrayofMembers = []
var saves = Array()
//Error catch testing
//var ret = "er"

//XMLRequest returns specified number of member info in JSON format.
function getList(num) {
    var httpRequest = new XMLHttpRequest()
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                var members = httpRequest.responseText
                //Error catch testing
                /*
                if(JSON.parse(members) == "Max 100 seats generated at a time") {
                    ret = "Max 100 seats generated at a time"
                }
                */
                arrayofMembers = JSON.parse(members)
                }
            }
        }
    httpRequest.open('GET', 'http://192.168.0.139/getMembers.php?n=' + num, false)
    httpRequest.send()
}

//Element Creation
function box(num) { //add num to allow custom seat gen
    if(num== "") {
        num = 100
    }
    getList(num)
    //Error catch testing
    /*
    if(ret == "er") {
        return containerDiv.innerHTML = "Max 100 seats generated at a time"
    }
    */
    for (let i=0; i<arrayofMembers.length; i++) {
        //Create the box containing the member seat
        var elmDiv = document.createElement('div')        
        elmDiv.setAttribute('class', 'tool')
        //elmDiv.setAttribute('class', 'testing')
        elmDiv.style.backgroundColor = arrayofMembers[i].color

        //Create and format the info popup.
        var info = document.createElement('span')
        info.setAttribute("class", "tooltiptext "+ arrayofMembers[i].class)
        var genderInfo = ""
        if(arrayofMembers[i].gender === "Male") {
            genderInfo = "<br><i class='fa-solid fa-mars'></i>"
        }
        else {
            genderInfo = "<br><i class='fa-solid fa-venus'></i>"
        }
        info.innerHTML = "<i class='fa-solid fa-user'></i><p class='nameText'> : " + arrayofMembers[i].fname + " " + arrayofMembers[i].sname + "</p>" +  "<br/><i class='fa-solid fa-users'></i><p class='raceText'> : " + arrayofMembers[i].race + "</p>" + genderInfo + "<p class='genderText'> : " + arrayofMembers[i].gender + "</p>" +  "<br/><i class='fa-solid fa-scroll'></i><p class='partyText'> : " + arrayofMembers[i].party + "</p>"
    
        /* Image testing
        var image = document.createElement('img')
        image.setAttribute('src', './images/testCap.jpg')
        */
        
        //Asign elements to parents and append to page
        var containerDiv = document.getElementById('containerDiv')
        containerDiv.appendChild(elmDiv)
        elmDiv.appendChild(info)
        //info.appendChild(image)
    }
}

function sort() {
    //Gets the current sort dropdown value
    var sortParam = document.getElementById("sortDropdown")
    sortParam = sortParam.selectedOptions[0]['value']
    if(sortParam == "nameText") {
        return
    }
    //Gets all of the tooltip elements
    var ar = document.getElementsByClassName("tool")
    if(ar.length == 0) {
        return
    }
    var j = getIndexOfSortParam(ar)
    //prepares the array for sorting
    ar = Array.prototype.slice.call(ar, 0)

    //Sorts the array by the element specified by the sortParam
    ar.sort(function (a, b) {
        a = a.childNodes[0].childNodes[j].innerHTML.replace(":", "").trim()
        b = b.childNodes[0].childNodes[j].innerHTML.replace(":", "").trim()
        
        if (a < b) {
            
            return -1;
            
        }
        if (a > b) {
            return 1;
        } 
        return 0;
    })
    //Wipes the content of the containerDiv containing the seat boxes.
    document.getElementById('containerDiv').innerHTML = ""
    //Appends each element of the sorted array to the container div in the sorted order.
    for(i=0;i<ar.length;i++) {
        document.getElementById('containerDiv').appendChild(ar[i])
    }
    //if(sortParam != "nameText") {
    addCountBoxes()
    //}
}

function getIndexOfSortParam(ar) {
    //Gets the current sort dropdown value
    var sortParam = document.getElementById("sortDropdown")
    sortParam = sortParam.selectedOptions[0]['value']
    if(sortParam == "nameText") {
        return
    }
    //Gets a list of childnodes of the 0th node of the first array element
    var f = ar[0].childNodes[0].childNodes
    
    //Finds the index of the element specified by the dropdown
    for(i=0;i<f.length;i++) {
        try {
            if(f[i].getAttribute('class') == sortParam) {
                return i
            }
        } catch(Exeption){
            //pass
        }
    }
}

function addCountBoxes() {
    //Gets all of the tooltips elements
    var ar = document.getElementsByClassName("tool")
    var j = getIndexOfSortParam(ar)
    if(j == null) {
        return
    }

    ar = Array.prototype.slice.call(ar, 0)
    var counts = {}
    
    //For each unique entry in the innerHTML of the sortparam specified by the dropdown, add a key and total count to 
    //an array named counts.
    ar.forEach(x => { 
        counts[x.childNodes[0].childNodes[j].innerHTML.replace(":", "").trim()] = (counts[x.childNodes[0].childNodes[j].innerHTML.replace(":", "").trim()] || 0) + 1;
    });
    
    //Clear the current innerHTML from the count container
    document.getElementById("countContainer").innerHTML = ""
    //For each unique key in the counts array, append a span element to the count container in the format - Key: Count
    for(var key in counts) {
        var elm = document.createElement("pre")
        elm.innerHTML = key + ": " + counts[key] + "  "
        document.getElementById("countContainer").appendChild(elm)
    }   
}

function save() {
    //Save the current containerDiv innerHTML to an array
    var elm = document.getElementById("containerDiv").innerHTML
    if(elm != "") {
        if(!saves.includes(elm))
            saves.push(elm)
    }
}

function load(id) {
    //Clears the containerDiv element
    clearElm()
    //Gets the data of the specified save clicked and loads it to the containerDivs innerHTML, also adds count boxes for the current sort parameter (This may be changed in future to change back to the sort parameter at time of saving)
    if(saves[id] != null) { 
        document.getElementById("containerDiv").innerHTML = saves[id]
        addCountBoxes()
    }
    
}

//Clears everything from the containerDiv and countContainer elements
function clearElm() {
    document.getElementById("containerDiv").innerHTML = ""
    document.getElementById("countContainer").innerHTML = ""
}