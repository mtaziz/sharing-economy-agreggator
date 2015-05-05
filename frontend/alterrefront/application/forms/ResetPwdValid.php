<?php
class Form_ResetPwdValid extends Zend_Form {
	
	public function __construct($options = null) {
        parent::__construct($options);
		
		$email = new Zend_Form_Element_Text('email');
		$email->setLabel('Email');
		$email->setRequired(true);
		
       	$submit = new Zend_Form_Element_Submit('submit');
       	$submit->setLabel('Save');
       
        $this->addElements(array(
        	$email,
        	$submit
        ));
	}
	
}