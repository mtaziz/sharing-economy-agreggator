<?php

class Admin_Bootstrap extends Zend_Application_Module_Bootstrap {
	
	protected function _initAutoload() {
		
        $autoLoader =  new Zend_Application_Module_Autoloader(array(
            'basePath'      => APPLICATION_PATH,
            'namespace'     => ''
        ));

        $autoLoader->addResourceType('dao', 'modules/admin/dao', 'Admin_Dao');
        return $autoLoader;
    }

    protected function _initTranslate(){

    	$translate = new Zend_Translate(
		    array(
		        'adapter' => 'array',
		        'content' => APPLICATION_PATH.'/modules/admin/translations/en.php',
		        'locale'  => 'en'
		    )
		);
		$translate->addTranslation(
		    array(
		        'content' => APPLICATION_PATH.'/modules/admin/translations/fr.php',
		        'locale'  => 'fr'
		    )
		);
		
		Zend_Registry::set('Zend_Translate', $translate);
    }
}