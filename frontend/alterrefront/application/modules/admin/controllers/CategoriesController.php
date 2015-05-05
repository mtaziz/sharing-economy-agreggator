<?php

class Admin_CategoriesController extends App_Controller_Action  {
	
	
	public function editAction() {
		
		$daoCategory = new Admin_Dao_CategoryDao();
		$category = new Model_Category();
		
		$form = new Form_Category();
		$form->setAction($this->view->link('categories','edit',array('universe' => $this->_get['universe'])));
		
		// Categories
		$daoCategory = new Admin_Dao_CategoryDao();
		$categories = $daoCategory->getCategories($this->_get['universe']);
		$categoriesArray = array();
		$categoriesArray[0] = '- None -';
		foreach($categories as $cat) {
			if (isset($this->_get['id'])) {
				if ($cat->id != $this->_get['id'])
					$categoriesArray[$cat->id] = $cat->TranslateCategory[0]->name;
			}else{
				$categoriesArray[$cat->id] = $cat->TranslateCategory[0]->name;
			}
		}
		$form->parent_id->setMultiOptions($categoriesArray);
		// --
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('categories','edit', array(
				'universe' => $this->_get['universe'],
				'id' => $this->_get['id'])
			));
			$category = $daoCategory->getCategory($this->_get['id']);
			$form->setDefaults($category->TranslateCategory[0]->toArray());
			$form->setDefaults($category->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save category
				$category->fromArray($form->getValues());
				$category->universe_id = $this->_get['universe'];
				$daoCategory->save($category);
				
				// Save Translation
				if (isset($this->_get['id'])) {
					$translate = $category->TranslateCategory[0];
				}else {
					$translate = new Model_TranslateCategory();
				}
				$form->setDefaults($this->_post);
				$translate->fromArray($form->getValues());
				$translate->language_id = BO_LANG;
				$translate->category_id = $category->id;
				$daoCategory->save($translate);
				
				$this->_helper->redirector('edit','universes', null, array('id' => $this->_get['universe']));
			}
		}
		
		$this->view->form = $form;
	}	
	
	public function deleteAction() {
		
		if (isset($this->_get['id'])) {
				
			// Delete Translations
			$daoCategory = new Admin_Dao_CategoryDao();
			$category = $daoCategory->getCategory($this->_get['id']);	
			foreach($category->TranslateCategory as $translation) {
				$daoCategory->delete($translation);
			}
				
			// Delete Category
			$daoCategory->delete($category);			
				
			$this->_helper->redirector('edit','universes', null, array('id' => $this->_get['universe']));
		}
	}
}