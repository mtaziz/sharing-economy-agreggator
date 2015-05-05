<?php

class Admin_LanguagesController extends App_Controller_Action {


	public function indexAction() {

        // ### !!!!!! ###
        // GARDER LE "fetchArray", en "execute", problème de référence !
        // ### !!!!!! ###

		$daoAd = new Admin_Dao_AdDao();
		$daoCategory = new Admin_Dao_CategoryDao();
		$daoPrivilege = new Admin_Dao_PrivilegeDao();
		$daoUniverse = new Admin_Dao_UniverseDao();

        $this->view->fields = $daoAd->getAdFieldsDefaultArray();
        $this->view->categories = $daoCategory->getCategoriesArray();
        $this->view->privileges = $daoPrivilege->getPrivilegesArray();
        $this->view->universes = $daoUniverse->getUniversesArray();

		$this->view->fieldsTranslate = $daoAd->getAdFieldsDefaultArray($this->_get['id']);
		$this->view->categoriesTranslate = $daoCategory->getCategoriesArray(null, $this->_get['id']);
		$this->view->privilegesTranslate = $daoPrivilege->getPrivilegesArray($this->_get['id']);
        $this->view->universesTranslate = $daoUniverse->getUniversesArray($this->_get['id']);

		$this->view->action = $this->view->link('languages','save',array('id' => $this->_get['id']));
	}
	
	public function saveAction() {

		$universes = $this->_post['universes'];
		$categories = $this->_post['categories'];
		$fields = $this->_post['fields'];
		$privileges = $this->_post['privileges'];
		
		$daoAd = new Admin_Dao_AdDao();
		$daoCategory = new Admin_Dao_CategoryDao();
		$daoPrivilege = new Admin_Dao_PrivilegeDao();
		$daoUniverse = new Admin_Dao_UniverseDao();
		
		// Delete fields, universes, privileges, categories
		$daoAd->deleteTranslations($this->_get['id']);
		$daoUniverse->deleteTranslations($this->_get['id']);
		$daoCategory->deleteTranslations($this->_get['id']);
		$daoPrivilege->deleteTranslations($this->_get['id']);
		
		foreach($fields as $field) {
			
			$translation = new Model_TranslateAdFieldDefault();
			$translation->name = $field['name'];
			$translation->value = $field['value'];
			$translation->ad_field_default_id = $field['ad_field_default_id'];
			$translation->language_id = $this->_get['id'];
			$daoUniverse->save($translation);
		}
		
		foreach($universes as $universe) {
			
			$translation = new Model_TranslateUniverse();
			$translation->name = $universe['name'];
			$translation->description = $universe['description'];
			$translation->universe_id = $universe['universe_id'];
			$translation->language_id = $this->_get['id'];
			$daoUniverse->save($translation);
		}
		
		foreach($categories as $category) {
			
			$translation = new Model_TranslateCategory();
			$translation->name = $category['name'];	
			$translation->category_id = $category['category_id'];
			$translation->language_id = $this->_get['id'];
			$daoCategory->save($translation);
		}
		
		foreach($privileges as $privilege) {
			
			$translation = new Model_TranslatePrivilege();
			$translation->name = $privilege['name'];
			$translation->privilege_id = $privilege['privilege_id'];
			$translation->language_id = $this->_get['id'];
			$daoPrivilege->save($translation);
		}
			
		$this->_helper->redirector('index','languages', 'admin', array('id' => $this->_get['id']));
	}
	
	public function editLangAction() {
		
		$daoLanguage = new Admin_Dao_LanguageDao();
		$lang = new Model_Language();
		
		$form = new Form_Language();
		$form->setAction($this->view->link('languages', 'edit-lang'));
		
		// Edition
		if (isset($this->_get['id'])) {
			$form->setAction($this->view->link('languages', 'edit-lang', array('id'=>$this->_get['id'])));
			$lang = $daoLanguage->getLanguage($this->_get['id']);
			$form->setDefaults($lang->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				$form->setDefaults($this->_post);
				$lang->fromArray($form->getValues());
				$daoLanguage->save($lang);
				
				$this->_helper->redirector('index','parameters');
			}
		}
		
		$this->view->form = $form;
	}
	
	public function deleteLangAction() {
		
		$daoLanguage = new Admin_Dao_LanguageDao();
		$daoAd = new Admin_Dao_AdDao();
		$daoCategory = new Admin_Dao_CategoryDao();
		$daoPrivilege = new Admin_Dao_PrivilegeDao();
		$daoUniverse = new Admin_Dao_UniverseDao();
		
		$daoAd->deleteTranslations($this->_get['id']);
		$daoUniverse->deleteTranslations($this->_get['id']);
		$daoCategory->deleteTranslations($this->_get['id']);
		$daoPrivilege->deleteTranslations($this->_get['id']);
		
		$lang = $daoLanguage->getLanguage($this->_get['id']);
		$daoLanguage->delete($lang);
		
		$this->_helper->redirector('index','parameters');
	}	
}