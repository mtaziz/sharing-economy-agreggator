<?php

class Admin_Dao_ContactDao extends App_Model_Dao {

    public function save($model) {
    	
    	try{

			$model->save();
			return true;
		}
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function findAll() {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Contact c')
			;

			return $query->fetchArray();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}