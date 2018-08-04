<?php
header("Content-Type: application/json;charset=utf-8");
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Origin: *');
$cmd = "python ../word.py";
echo shell_exec($cmd);
