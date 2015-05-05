<?php

class Default_Bootstrap extends Zend_Application_Module_Bootstrap {

	protected function _initAutoload() {

        $autoLoader =  new Zend_Application_Module_Autoloader(array(
            'basePath'      => APPLICATION_PATH,
            'namespace'     => ''
        ));

        $autoLoader->addResourceType('dao', 'modules/default/dao', 'Dao');
        return $autoLoader;
    }



    protected function _initRoutes() {

        $hostnameRoutePro = new Zend_Controller_Router_Route_Hostname(
            'www.coosome.com'
        );
        if ('matthieu' == APPLICATION_ENV) {
            $hostnameRoutePro = new Zend_Controller_Router_Route_Hostname(
              'alterre.dev' //only for local 
            );
        }

        $this->bootstrap('frontController');
        $frontController = $this->getResource('frontController');
        $router = $frontController->getRouter();

        // Recherche des structures ayant une page "active"
        $daoCzOrganisation = new Dao_CzOrganisationDao();
        $cities = $daoCzOrganisation->getAllCities();


        foreach($cities as $city) {
            if($city->privee==true || $city->publique==true) {
                $router->addRoute($city["domain"], $hostnameRoutePro->chain(
                    new Zend_Controller_Router_Route(
                        "/".$city["domain"].'/:controller/:action/*',
                        // "/:lang/".$city["domain"].'/:controller/:action/*',
                        array(
                            // 'lang' => $this->getResource('locale'),
                            'module' => 'default',
                            'controller' => 'orga',
                            'action' => 'index',
                            'id_orga' => $city["orga_id"]
                            )
                    )
                ));
            }
        }


        // Rewriting routes
        $router->addRoute('contact', $hostnameRoutePro->chain(
            new Zend_Controller_Router_Route(
                '/nous-contacter',
                array(
                    'module' => 'default',
                    'controller' => 'page',
                    'action' => 'contact')
            )
        ));



    }
}