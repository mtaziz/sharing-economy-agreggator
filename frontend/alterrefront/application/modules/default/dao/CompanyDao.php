<?php

class Dao_CompanyDao extends App_Model_Dao {

    public function save($model) {
    	
    	try{

			$model->save();
			return true;
		}
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function delete($model) {
    	
    	try{

			$model->delete();
			return true;
		}
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCompany($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Company c')
			->where('c.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCompanyType($id) {
    
	    try{
			
			$query = Doctrine_Query::create()
			->from('Model_CompanyType c')
			->where('c.id = ?',$id)
			;
			
			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCompanyTypes() {
    
	    try{
			
			$query = Doctrine_Query::create()
			->from('Model_CompanyType c')
			;
			
			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}