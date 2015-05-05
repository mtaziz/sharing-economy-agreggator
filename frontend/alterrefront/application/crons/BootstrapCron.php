<?php

// Define path to application directory
defined('APPLICATION_PATH')
    || define('APPLICATION_PATH', realpath(dirname(__FILE__) . '/..'));

// Define path to library directory
defined('LIBRARY_PATH')
    || define('LIBRARY_PATH', realpath(dirname(__FILE__) . '/../../library'));

// Define path to public directory
defined('PUBLIC_PATH')
    || define('PUBLIC_PATH', realpath(dirname(__FILE__) . '/../../public'));


// Vos fichiers ini de configuration contiennent peut être des sections "developement",
//"production", etc. Si vous voulez faire tourner les mêmes crons dans ces différents 
// environnements vous devez passer en paramètre le nom de l'environnement car 
// avec PHP CLI vos fichiers .htaccess seront ignorés.
if(empty ($argv[1])) exit("L'argument APPLICATION_ENV n'a pas été livré à l’exécution");
$env = (string) $argv[1];
define('APPLICATION_ENV', $env);
putenv('APPLICATION_ENV='.$env);


// Ensure library/ is on include_path
set_include_path(implode(PATH_SEPARATOR, array(
    realpath(LIBRARY_PATH),
    realpath(APPLICATION_PATH),
    realpath(APPLICATION_PATH . '/models'),
    get_include_path(),

)));

require_once 'Zend/Loader/Autoloader.php';
$autoloader = Zend_Loader_Autoloader::getInstance();
// custom classes
$autoloader->registerNamespace('Util_');


/** Zend_Application */
require_once 'Zend/Application.php';

$application = new Zend_Application(APPLICATION_ENV, APPLICATION_PATH 
                                                 . '/configs/application.ini');
$application->bootstrap();

$view = new Zend_View();
$view->setScriptPath(APPLICATION_PATH . '/modules/pro/views/scripts/');