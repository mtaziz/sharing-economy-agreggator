<?php
class App_Form_UniForm extends Zend_Form{
	/**
	 * Array of default element decorators
	 */
	protected $_defaultElementDecorators = null ;
	
	/**
	 * Enable or disable the default decorators
	 */
	protected $_disableDefaultDecorators = false ;

	/**
	 * Standard elements list
	 */
	protected $_standardElements = array(
	  'Zend_Form_Element_Button',
	  'Zend_Form_Element_Captcha',
	  'Zend_Form_Element_Hash',
	  'Zend_Form_Element_Checkbox',
	  'Zend_Form_Element_Multiselect',
	  'Zend_Form_Element_Password',
	  'Zend_Form_Element_Select',
	  'Zend_Form_Element_Text',
	  'Zend_Form_Element_Textarea',
	  'Zend_Form_Element_Xhtml',
	  'Zend_Form_Element_Radio',
	  'App_Form_Element_Note',
	  'Zend_Form_Element_Image'
	) ;
	
	/**
	 * Hidden elements list
	 */
	protected $_hiddenElements = array(
		'Zend_Form_Element_Hidden'
	) ;

	/**
	 * Action elements list (no label displayed)
	 */
	protected $_actionElements = array(
		'Zend_Form_Element_Submit',
		'Zend_Form_Element_Reset',
	) ;
	
	/**
	 * Multi elements list
	 */
	protected $_multiElements = array(
		'Zend_Form_Element_Multi',
		'Zend_Form_Element_MultiCheckbox'
	) ;
	
	public function __construct($options = null)	{
    if (is_array($options)) {
        $this->setOptions($options);
    } elseif ($options instanceof Zend_Config) {
        $this->setConfig($options);
    }

		// Init the default decorators
		$this->initDefaultElementsDecorators() ;

    // Extensions...
    $this->init();

    $this->loadDefaultDecorators();

    // traduction des messages d'erreur de validation
    $french = array(
		'notAlnum' => "'%value%' ne contient pas que des lettres et/ou des chiffres.",
		'notAlpha' => "'%value%' ne contient pas que des lettres.",
		'notBetween' => "'%value%' n'est pas compris entre %min% et %max% inclus.",
		'notBetweenStrict' => "'%value%' n'est pas compris entre %min% et %max% exclus.",
		'dateNotYYYY-MM-DD'=> "'%value%' n'est pas une date au format AAAA-MM-JJ (exemple : 2000-12-31).",
		'dateInvalid' => "'%value%' n'est pas une date valide.",
		'dateFalseFormat' => "'%value%' n'est pas une date valide au format JJ/MM/AAAA (exemple : 31/12/2000).",
		'notDigits' => "'%value%' ne contient pas que des chiffres.",
    	'emailAddressInvalidFormat' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressInvalid' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressInvalidHostname' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressInvalidMxRecord' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressDotAtom' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressQuotedString' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'emailAddressInvalidLocalPart' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'emailAddressInvalidSegment' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'emailAddressLengthExceeded' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'hostnameInvalid' =>"'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'hostnameIpAddressNotAllowed' =>"'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'hostnameInvalidHostname' =>"'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'hostnameInvalidLocalName' =>"'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
    	'hostnameLocalNameNotAllowed' => "'%value%' n'est pas une adresse mail valide selon le format adresse@domaine.fr",
		'notFloat' => "'%value%' n'est pas un nombre décimal.",
		'notGreaterThan' => "'%value%' n'est pas strictement supérieur à '%min%'.",
		'notInt'=> "'%value%' n'est pas un nombre entier.",
		'notLessThan' => "'%value%' n'est pas strictement inférieur à '%max%'.",
		'isEmpty' => "Ce champ est vide : vous devez le compléter.",
		'stringEmpty' => "Ce champ est vide : vous devez le compléter.",
		'regexNotMatch' => "'%value%' ne respecte pas le format '%pattern%'.",
		'stringLengthTooShort' => "'%value%' fait moins de %min% caractères.",
		'stringLengthTooLong' => "'%value%' fait plus de %max% caractères.",
		'recordFound' => "'%value%' est déjà utilisé."
    );

    $translate = new Zend_Translate('array', $french, 'fr');
    $this->setTranslator($translate);
    
    $this->setAttrib( 'class', 'uniForm' );
    $this->setAttrib('style', 'width:500px; margin:0 auto;');
	}
	
	/**
	 * Set to true if you do not want to use the default decorators
	 */
	public function setDisableDefaultDecorators($flag)	{
		$this->_disableDefaultDecorators = (bool) $flag ;
		return $this ;
	}
	
	/**
	 * Overriding the standard addElement method and call addElement
	 * with the default decorators if needed
	 */
	public function addElement($element, $name = null, $options = null)	{
		if ($this->_disableDefaultDecorators)	{
			return parent::addElement($element, $name, $options) ;
		}

		return $this->addElementWithDefaultDecorators($element, $name, $options) ;
	}

	/**
	 * Same as addElement but set the elements decorators
	 */
  public function addElementWithDefaultDecorators($element, $name = null, $options = null)	{
    if (is_string($element)) {
      $element = $this->createElement($element, $name, $options) ;
    }
    
  	if (!$options || !array_key_exists('decorators', $options))	{
  		$element->setDecorators($this->getDefaultElementDecorators(get_class($element))) ;
  	}
  	
  	return parent::addElement($element, $name, $options) ;
  }
  
  /**
   * Set decorators for an element class
   */
  public function setDefaultElementDecorators($className, $decorators)	{
  	$this->_defaultElementDecorators[$className] = $decorators ;
  	return $this ;
  }

	/**
	 * Get decorators from an element class name
	 */
  public function getDefaultElementDecorators($className)	{
		return $this->_defaultElementDecorators[$className] ;
  }

	/**
	 * Set decorators for an array of element class
	 */
  public function setDefaultElementsDecorators(array $classNames, $decorators)	{
  	foreach ($classNames as $className)	{
  		$this->setDefaultElementDecorators($className, $decorators) ;
  	}
  	return $this ;
  }
	
	/**
	 * Initialize the default element decorators
	 */
	public function initDefaultElementsDecorators()	{
		// Standard
		$standardDecorators = array(
			'ViewHelper',
			'Label',
			'Errors',
			//array('decorator' => array('Holder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'ctrlHolder inlineLabels')) //tata
		);
				
		$this->setDefaultElementsDecorators($this->_standardElements, $standardDecorators);

		// Hidden
		$hiddenDecorators = array(
			'ViewHelper',
			//array('decorator' => array('Holder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'hiddenHolder')) 
		) ;

		$this->setDefaultElementsDecorators($this->_hiddenElements, $hiddenDecorators) ;

		// No label
		$actionDecorators = array(
			'ViewHelper',
			//array('decorator' => array('Holder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'actionHolder')) 
		) ;

		$this->setDefaultElementsDecorators($this->_actionElements, $actionDecorators) ;

		// Multi Form Elements
		$multiDecorators = array(
			'ViewHelper',
			//array('decorator' => array('MultiHolder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'multiHolder')),
			'Label',
			//array('decorator' => array('Holder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'ctrlHolder')) 
		) ;

		$this->setDefaultElementsDecorators($this->_multiElements, $multiDecorators) ;
		
		// File
		$this->setDefaultElementsDecorators(array('Zend_Form_Element_File'), array (
        	'File',
        	'Errors',
        	array('Description', array('tag' => 'p', 'class' => 'description')),
        	array('HtmlTag', array('tag' => 'td')),
        	array('Label', array('tag' => 'th')),
        	array(array('tr' => 'HtmlTag'), array('tag' => 'tr')),
        	//array('decorator' => array('Holder' => 'HtmlTag'), 'options' => array('tag' => 'div', 'class' => 'ctrlHolder inlineLabels'))
        ));
        
        $this->setDefaultElementsDecorators(array('Zend_Form_Element_FormRTE'), $standardDecorators);
        $this->setDefaultElementsDecorators(array('Zend_Form_Element_Note'), $standardDecorators);
        
	}
	
	/**
	 * Load the default decorators for the current form
	 */
	public function loadDefaultDecorators()	{
    if ($this->loadDefaultDecoratorsIsDisabled()) {
        return;
    }

    $decorators = $this->getDecorators();
    if (empty($decorators)) {
        $this->addDecorator('FormElements')
             ->addDecorator('Form');
    }
	}
}
