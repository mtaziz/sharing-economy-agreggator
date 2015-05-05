<?php
class Form_Signup extends Zend_Form {
	
	public function __construct($options = null) {
        parent::__construct($options);

		$lastname = new Zend_Form_Element_Text('lastname');
		$lastname->setRequired(true);

		$firstname = new Zend_Form_Element_Text('firstname');
		$firstname->setRequired(true);

		$email = new Zend_Form_Element_Text('email');
		$email->setRequired(true);

		$password = new Zend_Form_Element_Text('password');
		$password->setRequired(true);

       	$submit = new Zend_Form_Element_Submit('submit');
       	$submit->setLabel('Save');
       
        $this->addElements(array(
        	$lastname,
        	$firstname,
        	$email,
        	$password,
        	$submit
        ));
	}
	
}