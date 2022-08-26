<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$result = [];
if ($_fp) {
    $i = 0;
    while (($line = fgets($_fp)) !== false) {
        if($i > 0){
            if(preg_match("/^hackerrank$/", $line)) $result[] = 0;
            else if(preg_match("/\shackerrank$/", $line)) $result[] = 2;
            else if(preg_match("/^hackerrank/", $line)) $result[] = 1;
            else $result[] = -1;
        }
        $i++;
    }

    fclose($_fp);
    foreach($result as $v) print_r($v . "\n");
}
?>
