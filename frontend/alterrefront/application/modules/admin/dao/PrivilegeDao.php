<?php

class Admin_Dao_PrivilegeDao extends App_Model_Dao {

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
			->innerJoin('p.TranslatePrivilege t ON p.id = t.privilege_id AND t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }

    public function getPrivilegesArray($lang = BO_LANG) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Privilege p')
                ->innerJoin('p.TranslatePrivilege t ON p.id = t.privilege_id AND t.language_id = ?',$lang)
            ;

            return $query->fetchArray();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    
    public function deleteTranslations($lang = BO_LANG) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->delete('Model_TranslatePrivilege t')
			->where('t.language_id = ?',$lang)
			;

			return $query->execute();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}    