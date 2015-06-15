<?php
$skills = $_REQUEST["skills"];
$type=$_REQUEST["type"];
$url="";
if($type=="companies")
    $url="http://192.168.1.23:5000/companies/?skills=" . urlencode($skills);
else
    $url="http://192.168.1.23:5000/seekers/?skills=" . urlencode($skills);
//echo 'http://127.0.0.1:5000/companies/?skills=' . urlencode($skills);
echo file_get_contents($url);
//echo $skills;
?>