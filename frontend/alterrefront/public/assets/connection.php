<?php

//Informations de connexion à la nouvelle base
// mysqli_connect("myhost","myuser","mypassw","mybd")
$mysqli_NEW = mysqli_connect("92.222.34.133", "mathieu", "123456", "test");
$mysqli_NEW->query("SET NAMES utf8");
if (mysqli_connect_errno($mysqli_NEW)) {
    echo "Echec lors de la connexion à MySQL : " . mysqli_connect_error();
}else{
	echo "connecté";
}

?>