<?php

class Bootstrap extends Zend_Application_Bootstrap_Bootstrap {

    protected function _initAutoload(){

        $config = new Zend_Config($this->getOptions());
        Zend_Registry::set('config', $config);

        $myconf = new Zend_Config_Ini(APPLICATION_PATH."/configs/myconf.ini");
        Zend_Registry::set('myconf', $myconf);

        

        $autoLoader = new Zend_Application_Module_Autoloader(array(
            'namespace' => '',
            'basePath' => APPLICATION_PATH ));
        $autoLoader->addResourceType('dao', 'modules/default/dao', 'Dao');
        return $autoLoader;
    }

    protected function _initAutoloadResource() {

        $autoLoader =  new Zend_Loader_Autoloader_Resource(array(
            'basePath'      => APPLICATION_PATH,
            'namespace'     => ''
        ));

        $autoLoader->addResourceType('model', 'models', 'Model_');
        $autoLoader->addResourceType('form', 'forms', 'Form_');
        return $autoLoader;
    }

    protected function _initAuthHelper(){

        // Zend_Controller_Action_HelperBroker::addHelper(new App_Controller_Helper_Auth());
    }

    protected function _initDelimiter() {

        $frontController = Zend_Controller_Front::getInstance();
        $dispatcher = $frontController->getDispatcher();
        $dispatcher->setWordDelimiter(array('-', '.'));
    }

    protected function _initRoutes() {

        $this->bootstrap('frontController');
        $frontController = $this->getResource('frontController');
        $router = $frontController->getRouter();


        // $front = Zend_Controller_Front::getInstance();
        // $router = $front->getRouter();

        // switch (getenv("ID_AGENCE")) {
        //     case "admin":  // BO
        //         $hostnameRouteWebservices = new Zend_Controller_Router_Route_Hostname(
        //                 "admin.".$config->cookie->domain
        //         );
        //         $pathRouteWebservices = new Zend_Controller_Router_Route(
        //                 ':controller/:action/*',
        //                 array(
        //                         'module'     => 'admin',
        //                         'controller' => 'index',
        //                         'action'     => 'index'
        //                 )
        //         );
        //         $router->addRoute("admin", $hostnameRouteWebservices->chain($pathRouteWebservices));
        //         break;

        //     case "www":


                $hostnameRoute = new Zend_Controller_Router_Route_Hostname(
                    'www.alterre.org'
                );
                if ('matthieu' == APPLICATION_ENV) {
                    $hostnameRoute = new Zend_Controller_Router_Route_Hostname(
                      'coosome.dev' //only for local 
                    );
                }


                $pathRouteDefault = new Zend_Controller_Router_Route(
                    '/:controller/:action/*',
                    // '/:lang/:controller/:action/*',
                    array(
                        // 'lang' => $this->getResource('locale'),
                        'controller' => 'index',
                        'action'     => 'index',
                        'module'     => 'default'
                    )
                );
                // $router->addRoute("default", $hostnameRoute->chain($pathRouteDefault));
                $router->addRoute('default', $pathRouteDefault);
                // $router->addRoute('edition-d-un-projet', $hostnameRoute->chain(new Zend_Controller_Router_Route('/projets/edition-d-un-projet',array('module' => 'default','controller' => 'projets','action' => 'edition'))));
                // $router->addRoute('edition-d-une-annonce', $hostnameRoute->chain(new Zend_Controller_Router_Route('/annonces/edition-d-une-annonce',array('module' => 'default','controller' => 'annonces','action' => 'edition'))));
                // $router->addRoute('annonces', $hostnameRoute->chain(new Zend_Controller_Router_Route('annonces',array('module' => 'default','controller' => 'annonces','action' => 'index'))));
                // $router->addRoute('projets', $hostnameRoute->chain(new Zend_Controller_Router_Route('projets',array('module' => 'default','controller' => 'projets','action' => 'index'))));
                $router->addRoute('signup-sent', $hostnameRoute->chain(new Zend_Controller_Router_Route('inscription-envoyee',array('module' => 'default','controller' => 'user','action' => 'signup-sent'))));
                $router->addRoute('login/:provider', $hostnameRoute->chain(new Zend_Controller_Router_Route('login/:provider',array('module' => 'default','controller' => 'user','action' => 'login'))));
                $router->addRoute('login', $hostnameRoute->chain(new Zend_Controller_Router_Route('login',array('module' => 'default','controller' => 'user','action' => 'login'))));
                $router->addRoute('logout', $hostnameRoute->chain(new Zend_Controller_Router_Route('logout',array('module' => 'default','controller' => 'user','action' => 'logout'))));
                $router->addRoute('connexion', $hostnameRoute->chain(new Zend_Controller_Router_Route('connexion',array('module' => 'default','controller' => 'user','action' => 'connexion'))));
                $router->addRoute('activation', $hostnameRoute->chain(new Zend_Controller_Router_Route('activation',array('module' => 'default','controller' => 'user','action' => 'signup-validated'))));
                $router->addRoute('reset-password', $hostnameRoute->chain(new Zend_Controller_Router_Route('mot-de-passe-oublie',array('module' => 'default','controller' => 'user','action' => 'reset-password'))));
                $router->addRoute('reset-password-confirm', $hostnameRoute->chain(new Zend_Controller_Router_Route('mot-de-passe-oublie-envoye',array('module' => 'default','controller' => 'user','action' => 'reset-password-confirm'))));
                $router->addRoute('reset-valid', $hostnameRoute->chain(new Zend_Controller_Router_Route('reinitialisation-du-mot-de-passe',array('module' => 'default','controller' => 'user','action' => 'reset-valid'))));
                $router->addRoute('a-propos', $hostnameRoute->chain(new Zend_Controller_Router_Route('a-propos',array('module' => 'default','controller' => 'page','action' => 'a-propos'))));
                // $router->addRoute('collectivites', $hostnameRoute->chain(new Zend_Controller_Router_Route('collectivites',array('module' => 'default','controller' => 'page','action' => 'collectivites'))));
                // $router->addRoute('associations', $hostnameRoute->chain(new Zend_Controller_Router_Route('associations',array('module' => 'default','controller' => 'page','action' => 'associations'))));
                // $router->addRoute('partenaires', $hostnameRoute->chain(new Zend_Controller_Router_Route('partenaires',array('module' => 'default','controller' => 'page','action' => 'partenaires'))));
                $router->addRoute('mentions-legales', $hostnameRoute->chain(new Zend_Controller_Router_Route('mentions-legales',array('module' => 'default','controller' => 'page','action' => 'mentions-legales'))));
                $router->addRoute('nous-contacter', $hostnameRoute->chain(new Zend_Controller_Router_Route('nous-contacter',array('module' => 'default','controller' => 'page','action' => 'contact'))));


        //         break;
        //     default:

        //         break;
        // }
       
// DEFAULT
        // $pathRouteDefault = new Zend_Controller_Router_Route(
        //     ':controller/:action/*',
        //     array(
        //         'controller' => 'ad',
        //         'action'     => 'company',
        //         'module'     => 'pro'
        //     )
        // );
        // $router->addRoute('pro', $pathRouteDefault);

// ADMIN
        // $hostnameRouteAdmin = new Zend_Controller_Router_Route_Hostname(
        //     'admin.dgefp.dev'
        // );

        // $pathRouteAdmin = new Zend_Controller_Router_Route(
        //     ':controller/:action/*',
        //     array(
        //         'controller' => 'index',
        //         'action'     => 'index',
        //         'module'     => 'admin'
        //     )
        // );
        // $router->addRoute('admin', $hostnameRouteAdmin->chain($pathRouteAdmin));

        
 // PRO
        // $hostnameRoutePro = new Zend_Controller_Router_Route_Hostname(
        //     'dgefp.dev'
        // );

        // $pathRoutePro = new Zend_Controller_Router_Route(
        //     ':controller/:action/*',
        //     array(
        //         'controller' => 'index',
        //         'action'     => 'index',
        //         'module'     => 'default'
        //     )
        // );
        // $router->addRoute('pro', $hostnameRoutePro->chain($pathRoutePro));

        // BEST URL
        // $router->addRoute('login', $hostnameRoutePro->chain(
        //     new Zend_Controller_Router_Route(
        //         '',
        //         array(
        //             'module' => 'pro',
        //             'controller' => 'user',
        //             'action' => 'login')
        //     )
        // ));


    }
}    
