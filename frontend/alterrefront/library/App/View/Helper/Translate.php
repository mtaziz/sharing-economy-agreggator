<?php
/**
 * Crée un lien de manière plus intuitive que l'aide "Url"
 * 
 * @package application
 * @subpackage viewhelpers
 */
class App_View_Helper_Translate extends Zend_View_Helper_Url
{
    /**
     * Crée un lien de manière plus intuitive que l'aide "Url"
     * 
     * @param string $controllerName
     * @param string $actionName
     * @param string $moduleName
     * @param array $params
     * @param string $name
     * @param boolean $reset
     * @return string
     */
    public function translate($key) {
    
        $translate = Zend_Registry::get('Zend_Translate');
        return $translate->translate($key);
    }
}