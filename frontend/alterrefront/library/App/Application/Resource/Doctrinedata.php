<?php
class App_Application_Resource_Doctrinedata extends Zend_Application_Resource_ResourceAbstract
{
   /**
    * @var Doctrine_Manager
    */
   protected $_manager;

   protected $_options = array();

   /**
    * Initialize Doctrine
    * 
    * @return Doctrine_Manager
    */
   public function init()
   {                           
       $manager = $this->getManager();
       $this->_options = $this->getOptions();

       $autoloader = $this->getBootstrap()->getApplication()->getAutoloader();
       $autoloader->pushAutoloader(array('Doctrinedata', 'autoload'));

       $manager->setAttribute(Doctrine::ATTR_AUTO_ACCESSOR_OVERRIDE, true);
       $manager->setAttribute(
           Doctrine::ATTR_MODEL_LOADING,
           Doctrine::MODEL_LOADING_CONSERVATIVE                        
       );
       $manager->setAttribute(Doctrine::ATTR_AUTOLOAD_TABLE_CLASSES, true);

       //TODO: quote identifier c'est pas top.
       //Plutôt renommer les tables et champs qui portent des noms réservés
       $manager->setAttribute(Doctrine::ATTR_QUOTE_IDENTIFIER, true);

       //TODO: ajouter des test sur les options si manquantes

       // connection

       $dsn = $this->_options['dsn'];

       try{
	        $conn = Doctrine_Manager::connection($dsn, 'doctrine');
	        $conn->setAttribute(Doctrine::ATTR_USE_NATIVE_ENUM, true);
	        $conn->setCharset('utf8');
       }
       catch(Doctrine_Connection_Exception $e)
       {
       	echo $e->getMessage();
       }

       if (true === (bool)$this->_options['generate']) {       
           $genOptions = array(
           	'pearStyle' => true,
               'baseClassPrefix' => $this->_options['options']['baseClassPrefix'],
               'baseClassesDirectory' => $this->_options['options']['baseClassesDirectory'],
               'classPrefix' => $this->_options['options']['classPrefix'],
               'classPrefixFiles' => (bool)$this->_options['options']['classPrefixFiles'],
               'generateTableClasses' => (bool)$this->_options['options']['generateTableClasses']
           );
			
           Doctrine::generateModelsFromDb( $this->_options['path']['models'], array( 'doctrine' ), $genOptions);
       }
		
       return $manager;
   }

   /**
    * Retrieve Doctrine Manager instance
    * 
    * @return Doctrine_Manager
    */
   public function getManager()
   {
       if (null === $this->_manager) {
           $this->_manager = Doctrine_Manager::getInstance();
       }
       return $this->_manager;
   }
}