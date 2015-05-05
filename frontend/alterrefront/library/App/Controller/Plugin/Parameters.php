<?php
class App_Controller_Plugin_Parameters extends Zend_Controller_Plugin_Abstract {

    public function preDispatch(Zend_Controller_Request_Abstract $request){



// $auth = Zend_Auth::getInstance();
// if ($auth->hasIdentity()) {
//     // l'identité existe ; on la récupère
//     $identite = $auth->getIdentity();
//     // var_dump($identite);
//     var_dump("connecté par zend");
// }else{
//     var_dump("pas connecté par Zend");
// }

// $auth = TBS\Auth::getInstance();
// if ($auth->hasIdentity()) {
//     // l'identité existe ; on la récupère
//     $identite = $auth->getIdentity();
//     // var_dump($identite);
//     var_dump("connecté par Facebook");
// }else{
//     var_dump("pas connecté par facebook");
// }
// var_dump($_SESSION);
// exit;


        $module = $request->getModuleName();
        $controller = $request->getControllerName();
        $action = $request->getActionName();
        switch ($module) {
            case 'default':

                $session = new Zend_Session_Namespace('troovon');
                $layout = Zend_Layout::getMvcInstance();
                $view = Zend_Controller_Front::getInstance()->getParam('bootstrap')->getResource('view');

                // $counters["inbox"] = 15;

                // $layout->counters = $counters;

                //Url de connexion FB
                $layout->facebookAuthUrl = TBS\Auth\Adapter\Facebook::getAuthorizationUrl();

                // User & company
                if (isset($session->user['id'])) {
                    $layout->isConnected = false;

                    $daoUser = new Dao_UserDao();
                    $user = $daoUser->getUser($session->user['id']);
                    $view->user = $user;
                    $layout->user = $user;

                    // userCompanies 
                    // $daoCompany = new Pro_Dao_CompanyDao();
                    // $communityType = $daoCompany->getCompanyTypeByName('community');
                    
                    // On recherche les orgas de l'user (company, asso, citiz)
                    // $userCompanies = $daoCompany->getOrganizationsOfThisUser($user->id,'1,2,3');
                    // $layout->userCompanies = $userCompanies;
                    // $view->userCompanies = $layout->userCompanies;


                    // Get last conection timestamp
                    $timeLastConnectionUser=$session->user['lastConnection'];
                    $lastConnectionUser = date('Y-m-d H:m:s',$timeLastConnectionUser);

                    // Counters for left menu
                    // $daoAds = new Pro_Dao_AdDao();


                    // $view->company = $session->company;
                    // $layout->company = $session->company;

                    // Infos de l'organisation
                    // if ($session->company->showOrgaPage==1){
                    //     // Orga Infos
                    //     $daoCzOrganisation = new Pro_Dao_OrgaInfoDao();
                    //     $orgaInfos = $daoCzOrganisation->getOrga($session->company->id);
                    //     $layout->orgaInfos = $orgaInfos;
                    // }

                    // $counters['allNewAds'] = $daoAds->countNewAds($session->company->id,$lastConnectionUser);
                   

                }else{
                     $layout->isConnected = true;
                }

                // // Language
                // $daoLanguage = new Dao_LanguageDao();
                // $languages = $daoLanguage->getLanguages();
                // $layout->languages = $languages;

                // // Set Languages
                // $translate = new Zend_Translate(
                //     array(
                //         'adapter' => 'array',
                //         'content' => APPLICATION_PATH.'/modules/default/translations/en-US.php',
                //         'locale'  => 'en-US'
                //     )
                // );
                // $translate->addTranslation(
                //     array(
                //         'adapter' => 'array',
                //         'content' => APPLICATION_PATH.'/modules/default/translations/en-GB.php',
                //         'locale'  => 'en-GB'
                //     )
                // );
                // $translate->addTranslation(
                //     array(
                //         'content' => APPLICATION_PATH.'/modules/default/translations/fr-FR.php',
                //         'locale'  => 'fr-FR'
                //     )
                // );

               //  if(isset($_COOKIE["lang"])&&(!isset($session->user['id']))){
               //      $lang = $daoLanguage->getLanguage($_COOKIE["lang"]);
               //      $session->lang = $lang;
               //      $translate->setLocale($session->lang->type);
               //  }else {

               //      if (isset($session->user['id'])) {

               //          $translate->setLocale($user->Language->type);
               //          $lang = $daoLanguage->getLanguage($user->Language->id);
               //          $session->lang = $lang;
               //      }else {

               //          try {
               //              $locale = new Zend_Locale('browser');
               //          } catch (Zend_Locale_Exception $e) {
               //              $locale = new Zend_Locale('fr');  
               //          }

               //          if ($locale->getLanguage() == 'fr') {
               //              $translate->setLocale('fr-FR');
               //              $lang = $daoLanguage->getLanguage(7);
               //              $session->lang = $lang;
               //          }else {
               //              $translate->setLocale('en-GB');
               //              $lang = $daoLanguage->getLanguage(8);//7=3
               //              $session->lang = $lang;
               //          }
               //      }
               //  }
               // $layout->currentLang = $session->lang;

               // Gestion de la devise de la langue choisie
               // $currency = new Zend_Currency($layout->currentLang->type);
               // $layout->currentSymbol=$currency->getSymbol();

// // Universes & Category for search bloc
// $daoUniverse = new Dao_UniverseDao();
// $universes = $daoUniverse->getUniverses($session->lang->id);
// $view->universes = $universes;
// $layout->universesSearch = $universes;

// $currentUniverse = $universes[0]->id;
// if (isset($_GET['universe']) && !empty($_GET['universe'])) {
//     $currentUniverse = $_GET['universe'];
// }

// $daoCategory = new Pro_Dao_CategoryDao();
// // User & company
// if (isset($session->user['id'])) {
//     $categories = $daoCategory->getCategories($currentUniverse,$session->lang->id,$session->company->id);
// }else{
//     $categories = $daoCategory->getCategories($currentUniverse,$session->lang->id);
// }
                // $layout->categoriesSearch = $categories;
        // $view->categories = $categories;

                // $layout->currentLang = $session->lang;
                // Zend_Registry::set('Zend_Translate', $translate);
                // Zend_Registry::set('Zend_Locale', $session->lang);


                break;
            case 'default2':

                $session = new Zend_Session_Namespace('troovon');

                $layout = Zend_Layout::getMvcInstance();
                $layout->currentNav = $action;

                $daoLanguage = new Pro_Dao_LanguageDao();
                $languages = $daoLanguage->getLanguages();
                $layout->languages = $languages;

                // Set Languages
                $translate = new Zend_Translate(
                    array(
                        'adapter' => 'array',
                        'content' => APPLICATION_PATH.'/modules/default/translations/en-US.php',
                        'locale'  => 'en-US'
                    )
                );
                $translate->addTranslation(
                    array(
                        'adapter' => 'array',
                        'content' => APPLICATION_PATH.'/modules/default/translations/en-GB.php',
                        'locale'  => 'en-GB'
                    )
                );
                $translate->addTranslation(
                    array(
                        'content' => APPLICATION_PATH.'/modules/default/translations/fr-FR.php',
                        'locale'  => 'fr-FR'
                    )
                );

                if(isset($_COOKIE["lang"])){
                    $lang = $daoLanguage->getLanguage($_COOKIE["lang"]);
                    $session->lang = $lang;
                    $translate->setLocale($session->lang->type);
                }else {
                    if (!isset($session->lang)) {

                        $translate->setLocale('fr-FR');
                        $locale = new Zend_Locale();
                        if ($locale->getLanguage() == 'fr') {
                            $translate->setLocale('fr-FR');
                            $lang = $daoLanguage->getLanguage(7);
                            $session->lang = $lang;
                        }else {
                            $translate->setLocale('en-GB');
                            $lang = $daoLanguage->getLanguage(2);
                            $session->lang = $lang;
                        }

                    }else {

                        $translate->setLocale($session->lang->type);
                    }
                }
                $layout->currentLang = $session->lang;
                Zend_Registry::set('Zend_Translate', $translate);

                break;
            case 'webservices':

                $layout = Zend_Layout::getMvcInstance();

                // Language
                $daoLanguage = new Pro_Dao_LanguageDao();
                $languages = $daoLanguage->getLanguages();
                $layout->languages = $languages;

                // Set Languages
                $translate = new Zend_Translate(
                    array(
                        'adapter' => 'array',
                        'content' => APPLICATION_PATH.'/modules/pro/translations/en-US.php',
                        'locale'  => 'en-US'
                    )
                );
                $translate->addTranslation(
                    array(
                        'adapter' => 'array',
                        'content' => APPLICATION_PATH.'/modules/pro/translations/en-GB.php',
                        'locale'  => 'en-GB'
                    )
                );
                $translate->addTranslation(
                    array(
                        'content' => APPLICATION_PATH.'/modules/pro/translations/fr-FR.php',
                        'locale'  => 'fr-FR'
                    )
                );

                $lang = null;
                $postLang = $request->getParam('lang');
                if (isset($postLang)) {
                    $translate->setLocale($request->getParam('lang'));
                }else {

                    $translate->setLocale('fr-FR');
                    $locale = new Zend_Locale();
                    if ($locale->getLanguage() == 'fr') {
                        $translate->setLocale('fr-FR');
                    }else {
                        $translate->setLocale('en-GB');
                    }
                }

                Zend_Registry::set('Zend_Translate', $translate);

                break;
            default:
                break;
        }
    }
}
