function getInfo(element) {
    clear()
    show(element)
    getSubordinates(element)
}

function clear() {
    elms = document.getElementsByClassName('character');
    for(i=0;i<elms.length;i++) {
        elms[i].removeAttribute('style');
    }
}

function getSubordinates(element) {
    var role = getAttr(element, "Role");
    if(role != "Crew") {
        highlight(role)
    }
}

function getSpecies() {
    var elm = document.getElementById('Species').value
    if(elm != "") {
        clear();
        highlight(elm);
    } else {
        return
    }
}

//Get specificed characterAttr from element
function getAttr(element, attr) {
    var elms = element.getElementsByClassName('characterAttrs')
    for(i=0;i<elms.length;i++) {
        var elm = (elms[i].innerHTML)
        elm = elm.split(":")
        
        if(elm[0] == attr) {
            return elm[1].trim()
        }
    }
}

function highlight(sort){
    var chrs = document.getElementsByClassName('character');
    var sort = sort.toLowerCase();
    var sorted = [];

    for (i=0;i<chrs.length;i++) {
        var attrs = chrs.item(i).getElementsByClassName('characterAttrs');
        for (j=0;j<attrs.length;j++) {
            var inner = attrs.item(j).innerHTML.split(":");
            inner = (inner[1].toLowerCase()).replace(" ","");
             if(inner == sort) {
                sorted.push(chrs.item(i));
            }
        }
    }
    
    //console.log(sorted)
    for(i=0;i<sorted.length;i++) {
        sorted[i].setAttribute('style', 'border: solid 1px black')
    }
}

function show(element) {
    //Gets and clears the infoContainer div if currently populated
    var info = document.getElementById("infoContainer");
    info.innerHTML = "";
    
    //Creates a new div element containing the info header string and appends to the infoContainer div
    var infoHeaderDiv = document.createElement('div');
    infoHeaderDiv.className = "col-12 my-2 align-self-center";

    var infoHeader = document.createElement("h4");
    infoHeader.innerHTML = "Character Info<i class='ra ra-player ra-2x'></i>:";
    
    infoHeaderDiv.append(infoHeader);
    info.append(infoHeaderDiv);

    //Get span elements from clicked character element.
    var spans = element.getElementsByClassName('characterAttrs');//[0].getElementsByTagName('span');

    //Loops through span elements innerHTML values for element clicked
    for(i=0;i<spans.length; i++) {
        
        //Splits span element into key:value array
        var sp = spans[i].innerHTML.replace(" ", "").split(":");
        
        //Container which houses all of the key value attribute pairs. Is appeneded to the infoContainer div once populated.
        var atrDiv = document.createElement("div");
        
        //Each attribute is given its own div. Attribute key and value are added to this div
        atrDiv.className = "col my-2";

        //Loops through ary creating div and span for each element of array
        for (j=0; j<sp.length; j++) {
            var div = document.createElement("div");
            div.className = "col";
            
            //Adds aditional formatting if element is key 
            if (j == 0) {
                div.innerHTML = "<b>" + sp[j] + ":</b>";
            } else {
                div.innerHTML = sp[j];
            }

            //Formats the CO attribute to "Commanding Officer"
            if (div.innerHTML == "<b>Co:</b>"){
                div.innerHTML = "<b>Commanding Officer:</b>";
            }
    
            //Appends new div to the attributeDivContainer
            atrDiv.append(div);
        }
        info.append(atrDiv);

        //Formatting to put Name on its own row
        if (i==0) {
            var br = document.createElement('div');
            br.className = "w-100";
            info.append(br);
        }
    }
}