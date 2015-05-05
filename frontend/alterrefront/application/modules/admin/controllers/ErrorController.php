<?php 

class Admin_ErrorController extends Zend_Controller_Action {
	
	public function errorAction() {
	
		$errors = $this->_getParam('error_handler');
 
        switch ($errors->type) {
            case Zend_Controller_Plugin_ErrorHandler::EXCEPTION_NO_ROUTE:
            case Zend_Controller_Plugin_ErrorHandler::EXCEPTION_NO_CONTROLLER:
            case Zend_Controller_Plugin_ErrorHandler::EXCEPTION_NO_ACTION:
                // erreur 404 -- contrôleur ou action introuvable
                $this->getResponse()->setRawHeader('HTTP/1.1 404 Not Found');
 
                $this->error = $errors->exception->getMessage();
                break;
            default:
                $this->error = $errors->exception->getMessage();
                exit;
                break;
        }
	}
}