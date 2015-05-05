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
    print " ---------- Envoie de la weekly \n\n";
    flush();


    // Boucle sur tous les users sauf ceux ayant la notification "weekly"==0

    // Récupération des 6 annonces privées les plus vues de ses organisations
    
    // Récupération des 6 annonces puibliques les plus vues des autres membres



    // $users = Model_Users::fetchAllPendingAccounts(1);
    $daoUser = new Pro_Dao_UserDao();
    $users = $daoUser->getUsersForNotification(11,"all","enable","weekly");

    foreach ($users as $user) {
        print " Email envoye a : ".$user->email." \n\n";

        // Récupération des annonces de l'utilisateur
        $daoAds = new Pro_Dao_AdDao();
        // Init Filters
// $filters = array();
// $filters['state'] = "available";
// $filters['visibility'] = 'private+CE'; // Annonces privées ou CE et publique
// $ads = $daoAds->getAds(1,'11', $filters, 8);
        $nb=0;

        // Récupération des annonces par leur ID
        $filters = array();
        $filters['ids'] = "724-300-348-294";
        $adsLeft = $daoAds->getAdsByFilters($filters, 8);
        $filters['ids'] = "292-298-883-291";
        $adsRight = $daoAds->getAdsByFilters($filters, 8);
        

        $subject="Annonces sélectionnées pour vous";
        $lang="fr";
        $params = array(
            'CE' => "CRON",
            'firstname'=>$user->firstname,
            'adsLeft' =>  $adsLeft,
            'adsRight' =>  $adsRight
        );
        $content = $view->partial('mails/weekly.phtml', $params);


        // Envoie du recap a moi
        App_Controller_Action::sendMail($subject,$content,array('matthieu.charron@gmail.com'),true);
        // App_Controller_Action::sendMail($subject,$content,array($user->email),true);

    }
    flush();
}
catch (Exception $e)
{
    // Gestion de l'exception.
    print "Une erreur est survenue \n";
    flush();
}