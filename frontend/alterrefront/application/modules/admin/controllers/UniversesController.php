<?php

class Admin_UniversesController extends App_Controller_Action {


	public function indexAction() {
		
	}
	
	public function editAction() {
		
		$daoUniverse = new Admin_Dao_UniverseDao();
		$universe = new Model_Universe();
		
		$form = new Form_Universe();
		$form->setAction($this->view->link('universes','edit'));
		
		// Edition
		if (isset($this->_get['id'])) {
			
			$form->setAction($this->view->link('universes','edit', array('id'=>$this->_get['id'])));
			$universe = $daoUniverse->getUniverse($this->_get['id']);
			
			$form->setDefaults($universe->TranslateUniverse[0]->toArray());
			$form->setDefaults($universe->toArray());
			$this->view->universe = $universe;
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {

				$form->setDefaults($this->_post);
	
				// Save Universe
				$universe->fromArray($form->getValues());
				$daoUniverse->save($universe);				
				
				// Save Translation
				if (isset($this->_get['id'])) {
					$translate = $universe->TranslateUniverse[0];
				}else {
					$translate = new Model_TranslateUniverse();
				}	
				$translate->fromArray($form->getValues());
				$translate->language_id = BO_LANG;
				$translate->universe_id = $universe->id;
				$daoUniverse->save($translate);
				
				$this->_helper->redirector('index','parameters');
			}
		}
		
		$this->view->form = $form;
	}
	
	public function deleteAction() {
		
		if (isset($this->_get['id'])) {
			
			// Delete translation
			$daoUniverse = new Admin_Dao_UniverseDao();
			$universe = $daoUniverse->getUniverse($this->_get['id']);
			foreach($universe->TranslateUniverse as $translation) {
				$daoUniverse->delete($translation);	
			}
			
			// Delete universe	
			$daoUniverse->delete($universe);
				
			$this->_helper->redirector('index','parameters');
		}
	}
}