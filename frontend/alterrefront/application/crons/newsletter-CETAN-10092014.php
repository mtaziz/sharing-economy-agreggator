#!/usr/bin/php
<?php
include 'BootstrapCron.php';

try
{
   // Le script peut mettre jusqu'à 10 minutes à s’exécuter. 
   //Cette valeur doit être réglée en fonction de vos traitements
   //c'est en quelque sorte le timeout.
    ini_set('max_execution_time', 600);

    // Le script peut utiliser 32 Mo de mémoire
    ini_set('memory_limit', "32M");

    $start = microtime(TRUE);
    print " ---------- Envoie de la Newsletter \n\n";
    flush();

    $daoUser = new Pro_Dao_UserDao();
    $users = $daoUser->getUsersForNotification(201,"all","enable","monthly");
    // $users = $daoUser->getUsersForNotification(11,"all","enable","weekly");

    foreach ($users as $user) {
        print " Email envoye a : ".$user->email." \n\n";

        $subject="Troovon fait sa rentrée... et vous ?";
        $params=NULL;
        $content = $view->partial('mails/newsletter-CETAN-10092014.phtml', $params);

        // Envoie du mail
        App_Controller_Action::sendMail($subject,$content,array($user->email),true);
        // App_Controller_Action::sendMail($subject,$content,array('matthieu.charron@gmail.com'),true);
    }
    flush();

    $end = microtime(true);
    $time = $end - $start;
    
    // Envoie du recap a moi
    $subject="Rapport d'envoie de la newsletter CETAN du 10/09/2014";
    $content = "La newsletter à été envoyées à ".count($users)." membres de Troovon en ".$time." secondes";
    App_Controller_Action::sendMail($subject,$content,array('matthieu.charron@gmail.com'),true);

}
catch (Exception $e)
{
    // Gestion de l'exception.
    print "Une erreur est survenue \n";
    flush();
}