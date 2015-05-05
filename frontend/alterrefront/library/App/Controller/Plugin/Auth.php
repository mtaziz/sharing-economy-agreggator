<?php
class App_Controller_Plugin_Auth extends Zend_Controller_Plugin_Abstract{
	
	private $_auth;
	
    public function __construct(){
        $this->_auth = Zend_Auth::getInstance();

        $this->_FBauth = TBS\Auth::getInstance();
    }	
	
	public function preDispatch(Zend_Controller_Request_Abstract $request){


        if ($request->module == 'webservices') {

            return true;
        }
        // Back office
        else if ($request->module == 'admin') {

            // Authentification
            if ( $this->_auth->hasIdentity() === true || $this->_FBauth->hasIdentity() === true) {

                if ($request->action == 'login' && $request->controller == 'users'){

                    $request->setControllerName('index');
                    $request->setActionName('index');
                }

            }else {

                if ($request->action != 'login'){

                    $request->setControllerName('users');
                    $request->setActionName('login');
                }
            }
        }

        else if ($request->module == 'default') {

// var_dump($request->module );exit;
            // Authorized
            if ($this->_auth->hasIdentity() === true || $this->_FBauth->hasIdentity() === true) {

                // Want to log in, but already logged in
                if ($request->action == 'login' && $request->controller == 'user'){

                    $request->setControllerName('index');
                    $request->setActionName('index');
                }
            }
            // Not Authorized
            else {

                // Page à rediriger si je ne suis pas loggué
                if ($request->controller == 'user' && 
                    (   
                        $request->action == 'profil' || 
                        $request->action == 'dashboard'
                        )){

                    $request->setControllerName('index');
                    $request->setActionName('index');
                    // return;
                }

                if ($request->controller == 'projets' && 
                    (   
                        $request->action == 'edition' || 
                        $request->action == 'xx'
                        )){

                    $request->setControllerName('index');
                    $request->setActionName('index');
                    // return;
                }

                if ($request->controller == 'annonces' && 
                    (   
                        $request->action == 'edition' || 
                        $request->action == 'xx'
                        )){

                    $request->setControllerName('index');
                    $request->setActionName('index');
                    // return;
                }

                // Pour afficher les pages Entreprises publiques
                if ($request->controller == 'orga'){
                    return;
                }

               // if ($request->action != 'login') {

                //     // Enregistre l'url demandé
                //     if (!$request->isXmlHttpRequest()) {
                //         $session = new Zend_Session_Namespace('lastRequest');
                //         $session->lastRequestUri = Zend_Controller_Front::getInstance()->getRequest()->getRequestUri();
                //     }

                //     $request->setControllerName('user');
                //     $request->setActionName('login');
                // }




            }
        }
        
    }
}