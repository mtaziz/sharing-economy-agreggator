<?php
class Form_ResetPwd extends Zend_Form {
	
	public function __construct($options = null) {
        parent::__construct($options);
		
		$hash = new Zend_Form_Element_Hidden('h');
		$hash->setRequired(true);
		
		$user = new Zend_Form_Element_Hidden('u');
		$user->setRequired(true);
		
		$password = new Zend_Form_Element_Password('password');
		$password->setLabel('Password');
		$password->setRequired(true);
		
       	$submit = new Zend_Form_Element_Submit('submit');
       	$submit->setLabel('Save');
       
        $this->addElements(array(
	        $hash,
			$user,
        	$password,
        	$submit
        ));
	}
	
}