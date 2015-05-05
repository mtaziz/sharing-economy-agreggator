<?php
class App_Controller_Helper_Auth extends Zend_Controller_Action_Helper_Abstract{

    private $_auth;

    public function __construct(){
        $this->_auth = Zend_Auth::getInstance();
    }

    public function preDispatch() {

        $request = $this->getRequest();
        //if ($request->module == 'pro') {
        if ($request->module == 'default') {

            // Not Authorized
            if ($this->_auth->hasIdentity() === false) {

                // Permet de rediriger vers le login, suite a un appel ajax, si la session a expiré
                if ($this->getRequest()->isXmlHttpRequest()) {

                    $auth = Zend_Auth::getInstance();
                    if ($auth->hasIdentity() === false) {
                        $response = array(
                            "status" => "401"
                        );

                        $jsonHelper = new Zend_Controller_Action_Helper_Json();
                        $jsonHelper->sendJson($response);
                    }
                }
            }
        }
    }
}