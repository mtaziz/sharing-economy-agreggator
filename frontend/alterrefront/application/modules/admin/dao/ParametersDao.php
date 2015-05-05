<?php

class Admin_Dao_ParametersDao extends App_Model_Dao {

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
    
    public function getPrivilege($id, $lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Privilege p')
			->innerJoin('p.TranslatePrivilege t')
			->where('p.id = ?',$id)
			->andWhere('t.language_id = ?',$lang)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getPrivileges($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Privilege p')
			->innerJoin('p.TranslatePrivilege t')
			->andWhere('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCurrency($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Currency c')
			->where('c.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCurrencies() {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Currency c')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCountry($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Country c')
			->where('c.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getCountries() {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Countries c')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}    