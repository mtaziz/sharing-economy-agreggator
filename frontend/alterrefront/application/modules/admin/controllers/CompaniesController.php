<?php
if ('matthieu' == APPLICATION_ENV) {
    require_once($_SERVER['DOCUMENT_ROOT'] . '/../library/Thumb/ThumbLib.inc.php');
}else{
    require_once($_SERVER['DOCUMENT_ROOT'] . '/library/Thumb/ThumbLib.inc.php');
}

class Admin_CompaniesController extends App_Controller_Action {


	public function indexAction() {
		return $this->_forward('all');
	}

    public function newAction() {

        $page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoCompany = new Admin_Dao_CompanyDao();

        $state="'registered'";
        $this->view->registeredCompanies = $daoCompany->getCompanies($state,$page);

        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;
    }
// anis 19/02/2014
    public function allAction() {

        $page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoCompany = new Admin_Dao_CompanyDao();
        $state="'enable','registered','trial'";
         $this->view->othersCompanies = $daoCompany->getCompanies($state,$page);
        // $this->view->othersCompanies = $daoCompany->getCompanies('registered', $page);
        // $this->view->othersCompanies = $daoCompany->getCompanies('trial', $page);
        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;
    }

    public function disabledAction(){
    	$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoCompany = new Admin_Dao_CompanyDao();
        $state="'disabled'";
        $this->view->othersCompanies = $daoCompany->getCompanies($state,$page);

        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;
    }
//_________________
    public function typesAction() {

        $daoCompany = new Admin_Dao_CompanyDao();
        $this->view->types = $daoCompany->getCompanyTypes();
    }

    public function searchAction() {

        $page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $search = array(
            'words' => '',
            'type' => '',
            'state' => '',
            'workforce' => 0
        );

        if (isset($this->_post['search']) && !empty($this->_post['search'])) {
            $search['words'] = explode(' ',$this->_post['search']);
        }
        if (isset($this->_post['type']) && !empty($this->_post['type'])) {
            $search['type'] = $this->_post['type'];
        }
        if (isset($this->_post['state']) && !empty($this->_post['state'])) {
            $search['state'] = $this->_post['state'];
        }
        if (isset($this->_post['workforce']) && !empty($this->_post['workforce'])) {
            $search['workforce'] = $this->_post['workforce'];
        }

        $daoCompany = new Admin_Dao_CompanyDao();
        $this->view->companies = $daoCompany->searchCompanies($search, $page);
        $this->view->search = $search;
    }

	public function editTypeAction() {
	
		$daoCompany = new Admin_Dao_CompanyDao();
		$type = new Model_CompanyType();
		
		$form = new Form_CompanyType();
		$form->setAction($this->view->link('companies','edit-type'));
		
		// Edition
		if (isset($this->_get['id'])) {
			
			$form->setAction($this->view->link('companies','edit-type', array('id'=>$this->_get['id'])));
			$type = $daoCompany->getCompanyType($this->_get['id']);
			$form->setDefaults($type->toArray());	
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {

				$form->setDefaults($this->_post);
				
				// Save type
				$type->fromArray($form->getValues());
				$daoCompany->save($type);
				
				$this->_helper->redirector('index','companies');
			}
		}
	
		$this->view->form = $form;
	}
		
	public function editAction() {
		
		$daoCompany = new Admin_Dao_CompanyDao();
		$company = new Model_Company();
		$hash = uniqid(md5(rand()), true);
		
		$form = new Form_Company();
		$form->setAction($this->view->link('companies','edit'));
		
		// Edition
		$companies = $daoCompany->getCompanies();
		if (isset($this->_get['id'])) {
			
			$form->setAction($this->view->link('companies','edit', array('id'=>$this->_get['id'])));
			$company = $daoCompany->getCompany($this->_get['id']);
			$form->setDefaults($company->toArray());	
		}
			
		// Select
		$companiesSelect = array();
		$companiesSelect[0] = '- None -';
		foreach ($companies as $comp) {
		
			if (isset($this->_get['id']) && $this->_get['id'] != $comp->id) {
				$companiesSelect[$comp->id] = $comp->name;	
			}
		}
		$form->parent_id->setMultiOptions($companiesSelect);
		
		$daoCountry = new Admin_Dao_CountryDao();
		$countries = $daoCountry->getCountries();
		$countriesSelect = array();
		foreach($countries as $country) {
			$countriesSelect[$country->id] = $country->name;
		}
		$form->country_id->setMultiOptions($countriesSelect);

		$types = $daoCompany->getCompanyTypes();
		$typeSelect = array();
		foreach($types as $type) {
			$typeSelect[$type->id] = $type->name;
		}
		$form->company_type_id->setMultiOptions($typeSelect);
		// --
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// If upload image
				if (isset($_FILES['logo_file']['name']) && !empty($_FILES['logo_file']['name'])) {
		
					$names = explode('.', $_FILES['logo_file']['name']);
					$ext = $names[count($names) - 1];
					$imagePath = $this->companiesTmpImagePath().'/'.$hash.'.'.$ext;
					$imageThumbPath = $this->companiesTmpImagePath().'/'.$hash.'_thumb.'.$ext;
					$form->logo_file->addFilter('Rename', array('target' => $imagePath, 'overwrite' => true));
				}
				
				$values = $form->getValues();
				$company->fromArray($values);
				
				// If upload image
				if (isset($_FILES['logo_file']['name']) && !empty($_FILES['logo_file']['name'])) {
					
					// Create thumbnail
					copy($imagePath, $imageThumbPath);
					$this->_createThumbnail($imagePath, $imageThumbPath);
					
					// Move Logo to Media
					$paths = $this->createUniqueStorage($hash);
					$mediaPath = $paths['path'].$paths['folder'].$hash.'.'.$ext;
					$mediaThumbPath = $paths['path'].$paths['folder'].$hash.'_thumb.'.$ext;
					
					$this->_moveImagesToMedia($imagePath, $mediaPath);
					$this->_moveImagesToMedia($imageThumbPath, $mediaThumbPath);
					$company->logo = 'http://medias.troovon.com/'.$paths['folder'].$hash.'.'.$ext;
					$company->thumbnail = 'http://medias.troovon.com/'.$paths['folder'].$hash.'_thumb.'.$ext;
					// --
				}
				
				// Save Company
				$daoCompany->save($company);
				
				$this->_helper->redirector('index','companies');
			}
		}
	
		$this->view->form = $form;
	}
	
	public function deleteAction() {

		$controllerRetour = $this->_get['controllerR'];
		$actionRetour = $this->_get['actionR'];

		if (isset($this->_get['id'])) {

// anis 19/02/2014
			if (isset($this->_get['delusers']) && $this->_get['delusers'] == "false" ){
				//Désactivation de l'entreprise et de l'utilisateur

				$daoCompany = new Admin_Dao_CompanyDao();
				$company = $daoCompany->getCompany($this->_get['id']);
				
				// If there are users in relation with this company
				// if (count($company->UserCompany) > 0) {
						// echo "<h1>company</h1>";
						$company->state = 'disabled';
						// var_dump($company->id) ;
						// var_dump($company->state) ;
						$daoCompany->save($company);
						// echo "<h1>user</h1>";
						$daoUser = new Admin_Dao_UserDao();
						$users = $daoUser->getUsersByOrgaId($company->id, 0);
						foreach($users as $user){
							$user->state = 'disable';
							$daoUser->save($user);
							// var_dump($user->id);
							// var_dump($user->state);
						}
						// echo "<h1>ad</h1>";
						$daoAd = new Admin_Dao_AdDao();
						$ads = $daoAd->searchAd(array('company_id' => $company->id), $page);
						foreach($ads as $ad){
							$ad->state = 'disable';
							$daoAd->save($ad);
							// var_dump($ad['_data']);
						}

						// echo "<h1>user company</h1>";
						$daoUserCompany = new Admin_Dao_UserCompanyDao();

						foreach($users as $user){
							$usercompany = $daoUser->getUserCompany($company->id,$user->id);
							// var_dump($usercompany['_data']);
							$daoUserCompany->delete($usercompany);
						}
						// exit;
						// $url = Zend_Controller_Front::getInstance()->getRequest()->getRequestUri();
						// var_dump($url);exit;

						$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
						// $this->_redirect($url);
						// var_dump($url);exit;
				// }

			}
			elseif(isset($this->_get['delusers']) && $this->_get['delusers'] == "true" ){
				//désactivation de l'entreprise

				$daoCompany = new Admin_Dao_CompanyDao();
				$company = $daoCompany->getCompany($this->_get['id']);
				
				// If there are users in relation with this company
				if (count($company->UserCompany) > 0) {

					$company->state = 'disabled';
					$daoCompany->save($company);

					$daoUser = new Admin_Dao_UserDao();
					$users = $daoUser->getUsersByOrgaId($company->id, 0);
					foreach($users as $user){
						$user->state = 'disable';
						$daoUser->save($user);
					}
						// var_dump($controllerRetour."/".$actionRetour);exit;
						$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
				}
			
			}
			elseif(isset($this->_get['delusers']) && $this->_get['delusers'] == "all" ){
			
				$daoCompany = new Admin_Dao_CompanyDao();
				$company = $daoCompany->getCompany($this->_get['id']);
				$daoUserCompany = new Admin_Dao_UserCompanyDao();

				if (count($company->UserCompany) > 0) {

					$daoUser = new Admin_Dao_UserDao();
					$users = $daoUser->getUsersByOrgaId($company->id, 0);

					foreach($users as $user){
						$usercompany = $daoUser->getUserCompany($company->id,$user->id);
						$daoUserCompany->delete($usercompany);
						$daoUser->delete($user);
					}
				}
				$daoCompany->delete($company);
									
				$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
			}
		}else {
			
			$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
		}
	}

    public function changeStateAction() {

    	$controllerRetour = $this->_get['controllerRetour'];
		$actionRetour = $this->_get['actionRetour'];
		$id = $this->_get['id'];

		$daoCompany = new Admin_Dao_CompanyDao();
		$company = $daoCompany->getCompany($id);        

        if (isset($company->id) && !empty($company->id)) {

            $company->state = 'enable';
            $daoCompany->save($company);
        }

        $this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
    }

	public function deleteTypeAction() {
		
		if (isset($this->_get['id'])) {
			
			$daoCompany = new Admin_Dao_CompanyDao();	
			$companyType = $daoCompany->getCompanyType($this->_get['id']);	
			$daoCompany->delete($companyType);		
			
			$this->_helper->redirector('index','companies');
			
		}else {
			
			$this->_helper->redirector('index','index');
		}
	}
	
	private function _createThumbnail($imagePath, $thumbPath) {
		
		// Resize picture
		$image = PhpThumbFactory::create($imagePath);
		$image->resize(640, 480);
		$image->save($imagePath);
		
		// Resize thumb
		$thumb = PhpThumbFactory::create($thumbPath);
		$thumb->adaptiveResize(160, 120);
		$thumb->save($thumbPath);
	}
}