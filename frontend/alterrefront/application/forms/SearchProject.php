<?php
class Form_SearchProject extends Zend_Form {
    
    public function __construct($options = null) {
        parent::__construct($options);
        
        $CitySearchInput = new Zend_Form_Element_Text('CitySearchInput');
        $CitySearchInput->setLabel('Choisissez votre lieu');

        $lat = new Zend_Form_Element_Hidden('lat');
        $lat->setLabel('lat');

        $lng = new Zend_Form_Element_Hidden('lng');
        $lng->setLabel('lng');

        $submit = new Zend_Form_Element_Submit('submit');
        $submit->setLabel('Découvrir les projets');
       
        $this->addElements(array(
            $CitySearchInput,
            $lat,
            $lng,
            $submit
        ));
    }
    
}