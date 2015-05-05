<?php
class Form_User extends Zend_Form {
	
	public function __construct($options = null) {
        parent::__construct($options);

        $picture = new Zend_Form_Element_File('picture');
        $picture->setLabel('Photo');

		$lastname = new Zend_Form_Element_Text('lastname');
		$lastname->setLabel('Lastname');
		
		$firstname = new Zend_Form_Element_Text('firstname');
		$firstname->setLabel('Firstname');

		$birthdate = new Zend_Form_Element_Text('birthdate');
		$birthdate->setLabel('birthdate');

		$description = new Zend_Form_Element_Text('description');
		$description->setLabel('description');
		
		$unit = new Zend_Form_Element_Text('unit');
		$unit->setLabel('Unit');
		
		$job = new Zend_Form_Element_Text('job');
		$job->setLabel('Job');

		$sponsor = new Zend_Form_Element_Text('sponsor');
		$sponsor->setLabel('Sponsor');

        $dd = new Zend_Form_Element_Text('dd');
        $mm = new Zend_Form_Element_Text('mm');
        $yyyy = new Zend_Form_Element_Text('yyyy');

        $address = new Zend_Form_Element_Text('address');

        $age = new Zend_Form_Element_Text('age');
        $age->setLabel('Age');

        $phone = new Zend_Form_Element_Text('phone');
        $phone->setLabel('Phone');

		$email = new Zend_Form_Element_Text('email');
		$email->setLabel('Email');
		
		$password = new Zend_Form_Element_Text('password');
		$password->setLabel('Password');

		$oldPwd = new Zend_Form_Element_Text('oldPwd');
		$oldPwd->setLabel('oldPwd');

		$newPwd = new Zend_Form_Element_Text('newPwd');
		$newPwd->setLabel('newPwd');

		$confirmPassword = new Zend_Form_Element_Text('confirmPassword');
		$confirmPassword->setLabel('confirmPassword');

		
		$state = new Zend_Form_Element_Select('state');
		$state->setLabel('State');
		$state->setMultiOptions(array(
			'enable' => 'Enable',
			'disable' => 'Disable',
		));

        // $language = new Zend_Form_Element_Select('language_id');
        // $language->setLabel('Language used');
		
       	$submit = new Zend_Form_Element_Submit('submit');
       	$submit->setLabel('Save');
       
        $this->addElements(array(
            // $picture,
        	$lastname,
        	$firstname,
        	$birthdate,
        	$description,
        	$dd,
        	$mm,
        	$yyyy,
        	$unit,
        	$address,
        	$job,
        	$sponsor,
            $age,
            $phone,
        	$email,
        	$password,
        	$oldPwd,
        	$newPwd,
        	$confirmPassword,
        	$state,
            // $language,
        	$submit
        ));
	}
	
}