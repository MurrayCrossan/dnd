<?php
$file[] = "humanMale.txt";
$file[] = "humanFemale.txt";

if(isset($_REQUEST["q"])) {
    $q = $_REQUEST["q"];
    
    if ($q !== "") {
        try {    
            $lines = file("names/".$file[$q]);
            $formatted = str_replace("\r\n", ",", $lines);
            echo trim($formatted[array_rand($formatted, 1)], ",");
            //for ($j=0; $j<count($formatted);++$j)
                //echo $formatted[$j];  
            } catch (Exception $e) {
                echo "Error";
        }
    }       
}


    /*

    if($q !== "") {
        for($i=0;$i<count($file);++$i) {
            if($q == $file[$i]) {
                $lines = file("names/".$file[$i]);
                $formatted = str_replace("\r\n", ",", $lines);
                for ($j=0; $j<count($formatted);++$j)
                    echo $formatted[$j];
            }  
        }
    } */
//}
else {
    echo("q not set");
};
/*
$lines = file($file);
$formatted = str_replace("\r\n", ",", $lines);
for ($i=0; $i<count($formatted);++$i)
    echo $formatted[$i];
*/
?>