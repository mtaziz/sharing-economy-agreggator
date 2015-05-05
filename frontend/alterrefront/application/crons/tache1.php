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
    print " ---------- Execution du CRON : Tache 1 \n\n";
    flush();


    // Traitements de votre cron qui utilise vos modèles,

    // $users = Model_Users::fetchAllPendingAccounts(1);

    $subject="Test tache CRON";
    // $content="envoie du mail";
    $lang="fr";
    $params = array(
    'CE' => "CRON",
    'firstname'=>"CRON",
    'titleAd' => "CRON",
    'descriptionAd' => "CRON",
    'urlMedia' => "http://fr.wikipedia.org/wiki/Cron#mediaviewer/Fichier:Gnome-terminal.svg",
    'urlAd' => "http://fr.wikipedia.org/wiki/Cron"
    );
    // $content = Zend_View::partial('mails/emailingAdCE-'.$lang.'.phtml', $params);
    // $content = $view->partial('mails/emailingAdCE-'.$lang.'.phtml', $params);
    // $content = $view->render('mails/emailingAdCE-'.$lang.'.phtml', $params);
    $content = $view->partial('mails/emailingAdCE-'.$lang.'.phtml', $params);
    // $content = $view->render('mails/emailingAdCE-'.$lang.'.phtml', $params);

    // $content = $view->render('mails/emailingAdCE-fr.phtml');


    // Envoie du recap a moi
    App_Controller_Action::sendMail($subject,$content,array('matthieu.charron@gmail.com'),true);
}
catch (Exception $e)
{
    // Gestion de l'exception.
    print "Une erreur est survenue \n".$content;
    flush();
}