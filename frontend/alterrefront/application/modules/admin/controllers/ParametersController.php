<?php

class Admin_ParametersController extends App_Controller_Action {

	public function indexAction() {


	}

    public function universesAction() {

        $daoUniverse = new Admin_Dao_UniverseDao();
        $universes = $daoUniverse->getUniverses();
        $this->view->universes = $universes;
    }

    public function privilegesAction() {
        $daoParameter = new Admin_Dao_ParametersDao();
        $privileges = $daoParameter->getPrivileges();
        $this->view->privileges = $privileges;
    }

    public function defaultFieldAction() {
        $daoAd = new Admin_Dao_AdDao();
        $fields = $daoAd->getAdFieldsDefault();
        $this->view->fields = $fields;
    }

    public function currenciesAction() {
        $daoCurrency = new Admin_Dao_CurrencyDao();
        $currencies = $daoCurrency->getCurrencies();
        $this->view->currencies = $currencies;
    }

    public function countriesAction() {
        $daoCountry = new Admin_Dao_CountryDao();
        $countries = $daoCountry->getCountries();
        $this->view->countries = $countries;
    }

    public function languagesAction() {
        $daoLanguage = new Admin_Dao_LanguageDao();
        $languages = $daoLanguage->getLanguages();
        $this->view->languages = $languages;
    }

	public function editCurrencyAction() {
		
		$daoParameters = new Admin_Dao_ParametersDao();
		$currency = new Model_Currency();
		
		$form = new Form_Currency();
		$form->setAction($this->view->link('parameters', 'edit-currency'));
		
		// Edition
		if (isset($this->_get['id'])) {
			
			$form->setAction($this->view->link('parameters', 'edit-currency', array('id'=>$this->_get['id'])));
			$currency = $daoParameters->getCurrency($this->_get['id']);
			$form->setDefaults($currency->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				$form->setDefaults($this->_post);
				$currency->fromArray($form->getValues());
				$daoParameters->save($currency);
				
				$this->_helper->redirector('index','parameters');
			}
		}
		
		$this->view->form = $form;
	}
	
	public function editCountryAction() {
		
		$daoParameters = new Admin_Dao_ParametersDao();
		$country = new Model_Country();
		
		$form = new Form_Country();
		$form->setAction($this->view->link('parameters', 'edit-country'));

        // Currencies
        $daoCurrency = new Admin_Dao_CurrencyDao();
        $currencies = $daoCurrency->getCurrencies();
        $currenciesArray = array();
        foreach($currencies as $currency) {
            $currenciesArray[$currency->id] = $currency->sign;
        }
        $form->currency_id->setMultiOptions($currenciesArray);
        // --

		// Edition
		if (isset($this->_get['id'])) {
			
			$form->setAction($this->view->link('parameters', 'edit-country', array('id'=>$this->_get['id'])));
			$country = $daoParameters->getCountry($this->_get['id']);
			$form->setDefaults($currency->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				$form->setDefaults($this->_post);
				$country->fromArray($form->getValues());
				$daoParameters->save($country);
				
				$this->_helper->redirector('index','parameters');
			}
		}
		
		$this->view->form = $form;
	}
	
	public function editPrivilegeAction() {
		
		$daoParameter = new Admin_Dao_ParametersDao();
		$privilege = new Model_Privilege();
		
		$form = new Form_Privilege();
		$form->setAction($this->view->link('parameters','edit-privilege'));
		
		// Edition
		if (isset($this->_get['id'])) {
		
			$form->setAction($this->view->link('parameters','edit-privilege', array('id' => $this->_get['id'])));
			$privilege = $daoParameter->getPrivilege($this->_get['id']);
			$form->setDefaults($privilege->TranslatePrivilege[0]->toArray());
			$form->setDefaults($privilege->toArray());
		}
		
		if ($this->getRequest()->isPost()) {
			
			if ($form->isValid($this->_post)) {
				
				// Save category
				$privilege->fromArray($form->getValues());
				$daoParameter->save($privilege);
				
				// Save Translation
				if (isset($this->_get['id'])) {
					$translate = $privilege->TranslatePrivilege[0];
				}else {
					$translate = new Model_TranslatePrivilege();
				}
				$form->setDefaults($this->_post);
				$translate->fromArray($form->getValues());
				$translate->privilege_id = $privilege->id;
				$translate->language_id = BO_LANG;
				$daoParameter->save($translate);
				
				$this->_helper->redirector('index','parameters');
			}
		}
		
		$this->view->form = $form;
	}	
		
	public function deleteCurrencyAction() {
	
		if (isset($this->_get['id'])) {
				
			// Delete Currency
			$daoCurrency = new Admin_Dao_CurrencyDao();
			$currency = $daoCurrency->getCurrency($this->_get['id']);	
			$daoCurrency->delete($currency);			
				
			$this->_helper->redirector('index','parameters');
		}
	}
	
	public function deleteCountryAction() {
	
		if (isset($this->_get['id'])) {
				
			// Delete Country
			$daoCountry = new Admin_Dao_CountryDao();
			$country = $daoCountry->getCountry($this->_get['id']);	
			$daoCountry->delete($country);			
				
			$this->_helper->redirector('index','parameters');
		}
	}

    public function getTemplateAction() {

        $this->_helper->layout->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);

        if ($this->getRequest()->isPost()) {
            echo $this->view->partial('mails/'.$this->_post['template'], array('message' => 'VOTRE MESSAGE PERSO ICI'));
        }
    }

	public function chooseLangAction() {
		
		$lang = $this->_get['lang'];
		
		$translate = Zend_Registry::get('Zend_Translate');
		$translate->setLocale($lang);
		Zend_Registry::set('Zend_Translate', $translate);
		$this->_session->lang = $lang;
		
		$this->_helper->redirector('index','index');
	}
}