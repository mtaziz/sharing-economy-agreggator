<?php

class Admin_UsersController extends App_Controller_Action {

	protected $_translate;
	
	public function indexAction() {
		
		// $daoUser = new Admin_Dao_UserDao();
		// $daoAdmin = new Admin_Dao_AdminDao();
		
		// $users = $daoUser->getUsers();
		// $admins = $daoAdmin->getAdmins();
		
		// $this->view->admins = $admins;
		// $this->view->users = $users;
		return $this->_forward('all');
	}
//anis 19/02/2014
	public function allAction(){
		$daoAd = new Admin_Dao_UserDao();
        $this->view->users = $daoAd->getUserbyState($state,$page);
	}

	public function disabledAction(){
		$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoAd = new Admin_Dao_UserDao();

        $state="'disable'";
        $this->view->users = $daoAd->getUserbyState($state,$page);
	}
// _______________
    public function searchAction() {
        $page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $search = array(
            'words' => '',
            'company_id' => 0
        );

        if (isset($this->_post['search']) && !empty($this->_post['search'])) {
            $search['words'] = explode(' ',$this->_post['search']);
        }
        if (isset($this->_post['id_company']) && !empty($this->_post['id_company'])) {
            $search['company_id'] = $this->_post['id_company'];
        }

        $daoUser = new Admin_Dao_UserDao();
        $this->view->users = $daoUser->searchUsers($search, $page);
        $this->view->search = $search;
    }

    public function getUsersAutocompleteAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);

        $words = explode(' ',$this->_get['query']);
        $daoUser = new Admin_Dao_UserDao();
        $users = $daoUser->searchUserWithWords($words);

        $usersArray = array();
        $cpt = 0;
        foreach($users as $user) {
            $usersArray[$cpt]['id'] = $user->id;
            $usersArray[$cpt]['value'] = $user->getFullname();
            $cpt++;
        }

        $this->_helper->json->sendJson($usersArray);
    }

    public function getCompaniesAutocompleteAction() {

        // Disable view and layout
        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);

        $words = explode(' ',$this->_get['query']);
        $daoCompany = new Admin_Dao_CompanyDao();
        $companies = $daoCompany->searchCompanyWithWords($words);

        $companiesArray = array();
        $cpt = 0;
        foreach($companies as $company) {
            $companiesArray[$cpt]['id'] = $company->id;
            $companiesArray[$cpt]['value'] = $company->name;
            $cpt++;
        }

        $this->_helper->json->sendJson($companiesArray);
    }



	public function mailAction() {
		if($this->getRequest()->isPost()) {
			$email = $this->_post['email'];
            $title = $this->view->translate('Congratulations your are now registered on Troovon');
			$lang = 'fr';
            $params = array('email' => $email);
            $content = $this->view->partial('mails/inscription-'.$lang.'.phtml', $params);
            $this->sendMail($title, $content, array($email), true);
		}
		$this->_helper->redirector('index');
	}


	public function editAction() {
		
		$daoUser = new Admin_Dao_UserDao();
		$user = new Model_User();
		
		$form = new Form_User();
		$form->setAction($this->view->link('users','edit'));

        // Language
        $daoLanguage = new Admin_Dao_LanguageDao();
        $languages = $daoLanguage->getLanguages();
        $langArray = array();
        foreach($languages as $language) {
            $langArray[$language->id] = $language->name;
        }

        $form->language_id->setMultiOptions($langArray);
        // --

		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('users','edit', array('id' => $this->_get['id'])));
			$user = $daoUser->getUser($this->_get['id']);
			$form->setDefaults($user->toArray());
			$this->view->user = $user;
			
			// Do not edit password
			$form->removeElement('password');
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save Field
				$user->fromArray($form->getValues());
				if (!isset($this->_get['id']) || empty($this->_get['id'])) {
					$user->password = md5($form->getValue('password'));
				}
				$daoUser->save($user);
				
				$this->_helper->redirector('index','users');
			}else {
                var_export($form->getErrors());
                exit;
            }
		}
		
		$this->view->form = $form;
	}

	public function editAdminAction() {
		
		$daoAdmin = new Admin_Dao_AdminDao();
		$admin = new Model_Admin();
		
		$form = new Form_Admin();
		$form->setAction($this->view->link('users','edit-admin'));
		
		// Privileges
		$daoPrivilege = new Admin_Dao_PrivilegeDao();
		$privileges = $daoPrivilege->getPrivileges();
		$privilegeArray = array();
		foreach($privileges as $privilege) {
			$privilegeArray[$privilege->id] = $privilege->type;
		}
		
		$form->privilege_id->setMultiOptions($privilegeArray);
		// --
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('users','edit-admin', array('id' => $this->_get['id'])));
			$admin = $daoAdmin->getAdmin($this->_get['id']);
			$form->setDefaults($admin->toArray());
			
			// Do not edit password
			$form->removeElement('password');
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save admin
				$admin->fromArray($form->getValues());
				if (!isset($this->_get['id']) || empty($this->_get['id'])) {
					$admin->password = md5($form->getValue('password'));
				}
				$daoAdmin->save($admin);
				
				$this->_helper->redirector('index','users');
			}
		}
		
		$this->view->form = $form;
	}
	
	public function editAddressAction() {
		
		$daoUser = new Admin_Dao_UserDao();
		$address = new Model_Address();
		
		$form = new Form_Address();
		$form->setAction($this->view->link('users','edit-address', array('user' => $this->_get['user'])));
				
		// Countries
		$daoCountry = new Admin_Dao_CountryDao();
		$countries = $daoCountry->getCountries();
		$countryArray = array();
		foreach($countries as $country) {
			$countryArray[$country->id] = $country->name;
		}
		
		$form->country_id->setMultiOptions($countryArray);
		// --
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('users','edit-address', array('id' => $this->_get['id'], 'user' => $this->_get['user'])));
			$address = $daoUser->getAddress($this->_get['id']);
			$form->setDefaults($address->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save Address
				$address->fromArray($form->getValues());
				$address->user_id = $this->_get['user'];
				$daoUser->save($address);
				
				$this->_helper->redirector('edit','users', null, array('id' => $this->_get['user']));
			}
		}
		
		$this->view->form = $form;
	}
	
	public function editCompanyAction() {
		
		$daoUser = new Admin_Dao_UserDao();
		$userCompany = new Model_UserCompany();
		
		$form = new Form_UserCompany();
		$form->setAction($this->view->link('users','edit-company', array('user' => $this->_get['user'])));
		
		// Privileges
		$daoPrivilege  = new Admin_Dao_PrivilegeDao();
		$privileges = $daoPrivilege->getPrivileges();
		
		$privilegesArray = array();
		foreach($privileges as $privilege) {
			$privilegesArray[$privilege->id] = $privilege->TranslatePrivilege[0]->name.' ('.$privilege->type.')';
		}
		$form->privilege_id->setMultiOptions($privilegesArray);
		// --
		
		// Edition
		if (isset($this->_get['company'])) {
		
			$form->setAction($this->view->link('users','edit-company', array('company' => $this->_get['company'], 'user' => $this->_get['user'])));
			$userCompany = $daoUser->getUserCompany($this->_get['company'], $this->_get['user']);
			$form->setDefaults($userCompany->toArray());
			$this->view->userCompany = $userCompany;
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save Address
				$userCompany->fromArray($form->getValues());
                $userCompany->user_id = $this->_get['user'];
				$daoUser->save($userCompany);
				
				$this->_helper->redirector('edit','users', null, array('id' => $this->_get['user']));
			}
		}
		
		$this->view->form = $form;
	}
	
	public function deleteAction() {
		
		$controllerRetour = $this->_get['controllerRetour'];
		$actionRetour = $this->_get['actionRetour'];
		
		if (isset($this->_get['id'])) {
				
			$daoUser = new Admin_Dao_UserDao();
			$user = $daoUser->getUser($this->_get['id']);	
			if (count($user->Ad) > 0) {
				
				$this->view->error = $this->view->translate('This user have add some ads, please delete its before delete the user');
				
			}else {
				
				// Delete User
				$daoUser->delete($user);					
				//$this->_helper->redirector('search','users');
				$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
			}
		}
	}

	public function  modifyAction() {
		$controllerRetour = $this->_get['controllerRetour'];
		$actionRetour = $this->_get['actionRetour'];
		$id = $this->_get['id'];

		$daoUser = new Admin_Dao_UserDao();
		$user = $daoUser->getUser($id);
		$user->state = 'disable';
		$daoUser->save($user);

		$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
	}

    public function deleteCompanyAction() {

        if (isset($this->_get['company']) && isset($this->_get['user'])) {

            // Delete Address
            $daoUser = new Admin_Dao_UserDao();
            $userCompany = $daoUser->getUserCompany($this->_get['company'], $this->_get['user']);
            $daoUser->delete($userCompany);

            $this->_helper->redirector('edit','users', null, array('id' => $this->_get['user']));
        }
    }

	public function deleteAddressAction() {
		
		if (isset($this->_get['id'])) {
				
			// Delete Address
			$daoUser = new Admin_Dao_UserDao();
			$address = $daoUser->getAdress($this->_get['id']);
			$daoUser->delete($address);			
				
			$this->_helper->redirector('edit','users', null, array('id' => $this->_get['user']));
		}
	}
	
	public function deleteAdminAction() {
		
		if (isset($this->_get['id'])) {
				
			// Delete Admin
			$daoAdmin = new Admin_Dao_AdminDao();
			$admin = $daoAdmin->getAdmin($this->_get['id']);
			$daoAdmin->delete($admin);			
				
			$this->_helper->redirector('index','users');
		}
	}

    public function contactAction() {

        if($this->getRequest()->isPost()) {

            $to = $this->_post['to'];
            $subject = $this->_post['subject'];
            $content = $this->_post['content'];

            $this->sendMail($subject,$content,array($to),true);
        }

        $this->_helper->redirector('index','companies');
    }

	public function loginAction() {
	
		$this->_helper->layout->setLayout('layout-login');
		
		if ($this->getRequest()->isPost()) {
		
			if (!isset($this->_post['email']) || empty($this->_post['email'])) {
			
				$this->view->error = array('error-email' => 'Please fill email');
				return;
			}else if (!isset($this->_post['pwd']) || empty($this->_post['pwd'])) {
			
				$this->view->error = array('error-pwd' => 'Please fill password');
				return;
			}
		
		    $dbAdapter = new App_Auth_Adapter_Doctrine( Doctrine::getConnectionByTableName('user') );
			
			$dbAdapter->setTableName('Model_Admin a') 
			            ->setIdentityColumn('a.login') 
			            ->setCredentialColumn('a.password')
			            ->setCredentialTreatment('MD5(?)')
			            ->setIdentity( $this->_post['email'] ) 
			            ->setCredential( $this->_post['pwd'] );

			$auth = Zend_Auth::getInstance();
		    $result = $auth->authenticate( $dbAdapter );
		    $user = $dbAdapter->getResultRowObject(null, array('password'));
		    
		    // Verify Privilege
		    $canLogin = true;
		    $daoAdmin = new Admin_Dao_AdminDao();
			$modelAdmin = new Model_Admin();
			$modelAdmin = $daoAdmin->getAdmin($user->id);
			
		    if ($modelAdmin->Privilege->type != 'superadmin' && $modelAdmin->Privilege->type != 'admin') {
		    
				$canLogin = false;	    	
		    	$errorMessage = 'Your are not authorized to log in';
		    }
		    
		    if ($result->isValid() === true && $canLogin) {
			    
			    $auth->getStorage()->write($user);
			    Zend_Session::regenerateId();
			    
			    // Remember Me
			    if ($this->_post['remember']) {
					Zend_Session::rememberUntil(518400);
				}else {
					Zend_Session::rememberUntil(3600);
				}
			    
			    // Save user in session
			    $this->_session->user['id'] = $modelAdmin->id;
			    $this->_session->user['privilege'] = $modelAdmin->Privilege->type;
			    $this->_session->user['lastConnection'] = strtotime($modelAdmin->last_connection);
			    $this->_session->user['name'] = $modelAdmin->name;
			    
			    // Update last connection date
			    $modelAdmin->last_connection = date('Y-m-d H:i:s',time());
			    $daoAdmin->save($modelAdmin);
			    
			    $this->_helper->redirector('index', 'index');
			    
		    } else{
				
				switch ( $result->getCode() ) {
				
				    case Zend_Auth_Result::FAILURE_IDENTITY_NOT_FOUND:
				    	$error = array('error-email' => 'Email not found');
				        break;
				
				    case Zend_Auth_Result::FAILURE_CREDENTIAL_INVALID:
				    	$error = array('error-pwd' => 'Bad password');
				        break;
				
				    default:
				    	if (!$canLogin) {
				    		$error = array('error' => $errorMessage);
				    	}else{
					    	$error = array('error' => 'Error please try later');
				    	}			    	
				        break;
				}
				
				$this->view->error = $error;		
		    }
	    }
	}
	
	public function logoutAction() {
	
		$auth = Zend_Auth::getInstance();
		$auth->clearIdentity();
		$this->_helper->redirector('login', 'users');
		Zend_Session::forgetMe();
	}
}