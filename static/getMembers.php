<?php
//Main function. Calls all get functions before returning a JSON encoded array of members
function main() {
    if(isset($_GET["n"])) {
        $num = intval($_GET['n']);
        try {
            $membersArray = [];
            
            for($i=0;$i<$num;++$i) {
                $party = getPartyInfo();
                $race = getRace($party);
                $gender = getGender();
                $name = getName($race, $gender);
                
                //Assigns all info into array keys (Dict)
                $member = array(
                    "race" => $race,
                    "gender" => $gender,
                    "fname" => $name[0],
                    "sname" => $name[1],
                    "party" => $party['party'],
                    "color" => $party['color'],
                    "class" => $party['class']
                );
                $membersArray[] = $member;
            
            }
            echo json_encode($membersArray);        
        } catch (Exception $e) {
            echo $e;
        }
    }
}

function getRace($party) {
    //Note: Find way to simplify this
    $fst = array("Human", "Dwarf", "Elf", "HalfElf", "Halfling", "HalfOrc"); //Other?
    $snd = array("Human", "Elf");
    $trd = array ("Human", "Dwarf", "Elf");
    $for = array("Human", "HalfElf");
    $fth = array("Human", "Dwarf", "Elf", "HalfElf", "Halfling");
    $party = $party['class'];

    //Checks what party a member belongs to and sets race list for party
    //25% FNP, 10% UFU, 15% NIP, 35% SPP, 15% IFL
    if($party === "FNP") {
        return $trd[array_rand($trd, 1)];
    } 
    elseif($party === "UFU" ) {
        return $fth[array_rand($fth, 1)];
    }
    elseif($party === "SPP") {
        return $fst[array_rand($fst, 1)];
    }
    elseif($party === "NIP") {
        return $for[array_rand($for, 1)];
    }
    elseif($party === "IFL") {
        return $snd[array_rand($snd, 1)];
    }
}

function getGender() {
    //Note: Add functionality for non-binary/non-gendered members. Access to any namelist coresponding to race?
    $genders = array("Male", "Female");
    return $genders[array_rand($genders, 1)];
}

function getName($race, $gender) {
    $name = array();
    //If race is HalfElf, randomly choose between the Human and Elf name files.
    if($race == "HalfElf") {
        $ary = array("Human", "Elf");
        $race = $ary[array_rand($ary, 1)];
    }
    //Return the firstname from the specified race and gender first name file
    try {
        $name[] = returnNameFromFile($race, $gender);
    } catch(Exception $e) {
        return "Error";
    }
    //If race is HalfOrc no second name is assigned, otherwise return the second name from the second name file for the specified race
    try {
        if($race == "HalfOrc") {
            $name[] = "";
        } else {
            $name[] = returnNameFromFile($race, "second");
        }
    } catch(Exception $e) {
        return "Error";
    }
    return $name;
}

function returnNameFromFile($fstVar, $sndVar) {
    $lines=file("names/".strtolower($fstVar)."-".strtolower($sndVar).".txt");
    $replace = array("\n", "\r");
    $formatted = str_replace($replace, "", $lines);
    return trim($formatted[array_rand($formatted, 1)], ",");
}

function getPartyInfo() {
    $num = random_int(0, 100);

    //Returns party info for the selected party
    if($num <= 25){
        return array("party"=>"First Nation Party", "color"=>"red", "class" => "FNP"); //25%, Fuck everyone but us
    } elseif($num >25 and $num <= 35) {
        return array("party"=>"United Fatherland Union", "color"=>"tan", "class" => "UFU"); //10%, A united south is the only way to ensure prosperity
    } elseif ($num > 35 and $num <=50) {
        return array("party"=>"New Identity Party", "color"=>"green", "class" => "NIP"); //15%, We can take the world by force
    } elseif($num > 50 and $num <=85) {
        return array("party"=>"Social Protection Party", "color"=>"blue", "class" => "SPP"); //35%, The common good is the most just path
    } else  {
        return array("party"=>"Industrial Formation League", "color"=>"black", "class" => "IFL"); //15%, An alliance with the north is the most benefictal to our nation
    }
}

//Checks if variable is set and is less than 100 (Testing limit to ensure performance)
if(isset($_GET['n']) and is_numeric($_GET['n'])) {
    if(intval($_GET['n']) >= 1 and intval($_GET['n'])-1 < 100) {
        main();
    }
    else {
        echo json_encode("Max 100 seats generated at a time");
    }
} else {
    echo "Error";
}