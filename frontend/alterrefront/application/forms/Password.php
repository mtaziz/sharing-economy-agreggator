<?php
class Form_Password extends Zend_Form {
	
	public function __construct($options = null) {
        parent::__construct($options);

		$oldPwd = new Zend_Form_Element_Text('oldPwd');
		$oldPwd->setLabel('oldPwd');

		$newPwd = new Zend_Form_Element_Text('newPwd');
		$newPwd->setLabel('newPwd');

		$confirmPassword = new Zend_Form_Element_Text('confirmPassword');
		$confirmPassword->setLabel('confirmPassword');

       	$submit = new Zend_Form_Element_Submit('submit');
       	$submit->setLabel('Save');
       
        $this->addElements(array(
        	$oldPwd,
        	$newPwd,
        	$confirmPassword,
        	$submit
        ));
	}
	
}