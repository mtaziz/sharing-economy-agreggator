<?php

class Admin_Dao_LanguageDao extends App_Model_Dao {

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
			
	public function getLanguage($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Language l')
			->where('l.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getLanguages() {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Language l')
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}