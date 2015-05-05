<?php
if ('matthieu' == APPLICATION_ENV) {
    require_once($_SERVER['DOCUMENT_ROOT'] . '/../library/Thumb/ThumbLib.inc.php');
}else{
    require_once($_SERVER['DOCUMENT_ROOT'] . '/library/Thumb/ThumbLib.inc.php');
}

class Admin_AdsController extends App_Controller_Action {

	public function indexAction() {

  //       $daoCategory = new Admin_Dao_CategoryDao();
  //       $this->view->categories = $daoCategory->getCategories();
		// $this->_helper->redirector('news','ads');
		return $this->_forward('new');
	}
//anis 19/02/2014
	public function allAction(){
        $daoAd = new Admin_Dao_AdDao();
        $this->view->ads = $daoAd->getAdbyState($state,$page);
	}

	public function newAction(){
		$page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $daoAd = new Admin_Dao_AdDao();

        $state="'available'";
        $this->view->ads = $daoAd->getAdbyState($state,$page);

        $controller = $this->getRequest()->getControllerName();
        $action = $this->getRequest()->getActionName();

        $this->view->controller = $controller;
        $this->view->action = $action;
	}
// _______________	
	public function editAction() {
	
		$daoAd = new Admin_Dao_AdDao();
		$ad = new Model_Ad();
		
		$form = new Form_Ad();
		$form->setAction($this->view->link('ads','edit'));
		
		// Categories
		$daoCategory = new Admin_Dao_CategoryDao();
		$categories = $daoCategory->getCategories();
		$categoriesArray = array();
		foreach($categories as $category) {
			$categoriesArray[$category->id] = $category->TranslateCategory[0]->name;
		}
		$form->category_id->setMultiOptions($categoriesArray);
		// --
		
		// Company
		$daoCompany = new Admin_Dao_CompanyDao();
		$companies = $daoCompany->getCompanies();
		$companiesArray = array();
		foreach($companies as $company) {
			$companiesArray[$company->id] = $company->name;
		}
		$form->company_id->setMultiOptions($companiesArray);
		// --
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('ads','edit', array('id' => $this->_get['id'])));
			$ad = $daoAd->getAd($this->_get['id']);
			$this->view->ad = $ad;
			$form->setDefaults($ad->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save Field
				$ad->fromArray($form->getValues());
				$daoAd->save($ad);
				
				$this->_helper->redirector('index','ads');
			}
		}

        $this->view->categories = $daoCategory->getCategories();
		$this->view->form = $form;
	}

    public function searchAction() {

        $page = 1;
        if (isset($this->_get['p'])) {
            $page = $this->_get['p'];
        }

        $search = array(
            'words' => '',
            'company_id' => 0,
            'user_id' => 0,
            'state' => '',
            'category_id' => 0
        );

        if (isset($this->_post['search']) && !empty($this->_post['search'])) {
            $search['words'] = explode(' ',$this->_post['search']);
        }
        if (isset($this->_post['company_id']) && !empty($this->_post['company_id'])) {
            $search['company_id'] = $this->_post['company_id'];
        }
        if (isset($this->_post['state']) && !empty($this->_post['state'])) {
            $search['state'] = $this->_post['state'];
        }
        if (isset($this->_post['user_id']) && !empty($this->_post['user_id'])) {
            $search['user_id'] = $this->_post['user_id'];
        }
        if (isset($this->_post['category_id']) && !empty($this->_post['category_id'])) {
            $search['category_id'] = $this->_post['category_id'];
        }

        $daoCategory = new Admin_Dao_CategoryDao();
        $this->view->categories = $daoCategory->getCategories();

        $daoAd = new Admin_Dao_AdDao();
        $this->view->ads = $daoAd->searchAd($search, $page);
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

	public function addMediaAction() {
	
		if ($this->getRequest()->isPost()) {
			
			if (isset($_FILES['media']['name']) && !empty($_FILES['media']['name'])) {
				
				$hash = uniqid(md5(rand()), true);
				$names = explode('.', $_FILES['media']['name']);
				$ext = $names[count($names) - 1];
			
				$imagePath = $this->adsTmpImagePath().'/'.$hash.'.'.$ext;
				$imageThumbPath = $this->adsTmpImagePath().'/'.$hash.'_thumb.'.$ext;
				
				$picturesType = array(
					'image/x-png',
					'image/png',
					'image/pjpeg',
					'image/jpeg',
					'image/jpg',
					'image/gif',
					'image/bmp'
				);
				
				$movieType = array(
					"video/mov", 
					"video/avi",
					"video/mpg",
					"video/mpeg"
				);
				
				$type = null;
				if (in_array($_FILES['media']['type'], $picturesType)) {
					$type = 'picture';
				}else if (in_array($_FILES['media']['type'], $movieType)) {
					$type = 'movie';
				}
				
				if (!$type) {
					$this->error = 'File must be : *.jpeg, *.bmp, *.jpg, *.png or *.gif';
					return;
				}
				
				if (move_uploaded_file($_FILES['media']['tmp_name'],$imagePath)) {
					
					// Create thumbnail
					copy($imagePath, $imageThumbPath);
					$this->_createThumbnail($imagePath, $imageThumbPath);
					
					// Move Logo to Media
					$paths = $this->createUniqueStorage($hash);
					$mediaPath = $paths['path'].$paths['folder'].$hash.'.'.$ext;
					$mediaThumbPath = $paths['path'].$paths['folder'].$hash.'_thumb.'.$ext;
					
					$this->_moveImagesToMedia($imagePath, $mediaPath);
					$this->_moveImagesToMedia($imageThumbPath, $mediaThumbPath);
					// --	
					
					$media = new Model_Media();
					$daoAd = new Admin_Dao_AdDao();
					$media->name = $paths['folder'].$hash.'.'.$ext;
					$media->thumb_name = $paths['folder'].$hash.'_thumb.'.$ext;
					$media->link = 'http://medias.troovon.com/'.$paths['folder'].$hash.'.'.$ext;
					$media->thumbnail = 'http://medias.troovon.com/'.$paths['folder'].$hash.'_thumb.'.$ext;
					$media->ad_id = $this->_get['id'];
				    $media->type = $type;
					$daoAd->save($media);
					
					$this->_helper->redirector('edit','ads', null, array('id' => $this->_get['id']));
					
				}else {
					$this->error = 'Error while uploading file';
				}
			}
		}
	}
	
	public function deleteMediaAction() {
		
		if (isset($this->_get['id'])) {
				
			// Delete Media
			$daoAd = new Admin_Dao_AdDao();
			$media = $daoAd->getMedia($this->_get['id']);
			$name = $media->name;
			$thumbnail = $media->thumb_name;
			$daoAd->delete($media);
			
			@unlink('/homez.441/troovon/medias/'.$name);
			@unlink('/homez.441/troovon/medias/'.$thumbnail);
				
			$this->_helper->redirector('edit','ads', null, array('id' => $this->_get['ad']));
		}
	}
	
	public function deleteAction() {
		
		$controllerRetour = $this->_get['controllerR'];
		$actionRetour = $this->_get['actionR'];

		if (isset($this->_get['id'])) {
				
			// Delete Ad
			$daoAd = new Admin_Dao_AdDao();
			$ad = $daoAd->getAd($this->_get['id']);
			// var_dump($ad);exit;
			$ad->state = 'deleted_by_admin';

			$daoAd->save($ad);
			$daoAd->delete($ad);
			// var_dump($ad);exit;			

			// var_dump("suppr");exit;

			// var_dump($controllerRetour."/".$actionRetour);exit;
			$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);
		}
	}
	
	public function editFieldDefaultAction() {

		$daoAd = new Admin_Dao_AdDao();
		$translate = new Model_TranslateAdFieldDefault();
		
		$form = new Form_AdFieldDefault();
		$form->setAction($this->view->link('ads','edit-field-default'));
		
		// Categories
		$daoCategory = new Admin_Dao_CategoryDao();
		$categories = $daoCategory->getCategories();
		$categoriesArray = array();
		foreach($categories as $category) {
			$categoriesArray[$category->id] = $category->TranslateCategory[0]->name;
		}
		$form->category_id->setMultiOptions($categoriesArray);
		// --
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('ads','edit-field-default', array('id' => $this->_get['id'])));
			$field = $daoAd->getAdFieldDefault($this->_get['id']);
			$form->setDefaults($field->TranslateAdFieldDefault[0]->toArray());
			$form->setDefaults($field->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save Field
				$field = new Model_AdFieldDefault();
				$field->fromArray($form->getValues());
				$daoAd->save($field);
				
				// Save Translation
				if (isset($this->_get['id'])) {
					$translate = $field->TranslateAdFieldDefault[0];	
				}else {
					$translate = new Model_TranslateAdFieldDefault();
				}
				$form->setDefaults($this->_post);
				$translate->fromArray($form->getValues());
				$translate->ad_field_default_id = $field->id;
				$translate->language_id = BO_LANG;
				$daoAd->save($translate);
				
				$this->_helper->redirector('index','parameters');
			}
		}

        $this->view->categories = $daoCategory->getCategories();
		$this->view->form = $form;
	}	
	
	public function deleteFieldDefaultAction() {
		
		if (isset($this->_get['id'])) {
				
			// Delete Translation	
			$daoAd = new Admin_Dao_AdDao();
			$field = $daoAd->getAdFieldDefault($this->_get['id']);	
			foreach($field->TranslateAdFieldDefault as $translation) {
				$daoAd->delete($translation);
			}		
			
			// Delete Field	
			$daoAd->delete($field);
				
			$this->_helper->redirector('index','parameters');
		}
	}
	
	private function _createThumbnail($imagePath, $thumbPath) {
		
		// Resize picture
		$image = PhpThumbFactory::create($imagePath);
		$image->adaptiveResize(640, 480);
		$image->save($imagePath);
		
		// Resize thumb
		$thumb = PhpThumbFactory::create($thumbPath);
		$thumb->adaptiveResize(230, 230);
		$thumb->save($thumbPath);
	}

	public function disableAction() {

		$controllerRetour = $this->_get['controllerRetour'];
		$actionRetour = $this->_get['actionRetour'];
		$id = $this->_get['id'];

		$daoAd = new Admin_Dao_AdDao();
		$ad = $daoAd->getAd($id);

		$ad->state = 'disable';

		$daoAd->save($ad);

		$this->_helper->redirector->gotoUrl($controllerRetour."/".$actionRetour);

		// var_dump($ad);exit;
		//désactiver et sauvegarder
	}
}