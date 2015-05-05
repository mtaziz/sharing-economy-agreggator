<?php

class Dao_PrivilegeDao extends App_Model_Dao {

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
    
    public function getPrivileges($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Privilege p')
			->innerJoin('p.TranslatePrivileges t')
			->where('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
    
    public function getPrivilegeWithType($type) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_Privilege p')
			->where('p.type = ?',$type)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}