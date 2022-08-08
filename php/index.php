<?php
$data1 = '{"token":"Privar Visa","token_ref_number":"200519855049","sid":"af7e5a0d-de46-4e97-97c1-
5b8cfa2e4bc3","type":"Payment"}';
$priv_key = 'QP7RZD2IZlMn2Q1yyxDq3wsVe7dGozvWKZyEBB8F';
 //echo "0 - API-key: $priv_key" . "<br />";
 //echo "1 - Request: $data1". "<br />";
 $datax = json_decode($data1, true);
 $base64 = base64_encode($data1);
 //echo '2 - Base64 request: ' . $base64. "<br />";
 $concat = $priv_key . $base64 . $priv_key;
 //echo '3 - Concat priv_key . base64 . priv_key:' . $concat. "<br />";
 $hmac = hash_hmac('sha1', $concat, $priv_key, TRUE);
 //echo '4 - hash_hmac: ' . $hmac. "<br />";
 $sign = base64_encode($hmac);
 //echo '5 - base64_encode hash_hmac. Sign= ' . $sign. "<br />";
 $sreq = json_encode($datax + ['sign' => $sign], JSON_UNESCAPED_UNICODE);
 //echo '6 - final request= ' . $sreq. "<br />";
 echo $sreq;
 //echo $sreq. "<br />";