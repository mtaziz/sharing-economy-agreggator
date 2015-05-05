<?php

class Dao_UserDao extends App_Model_Dao {

    public function delete($model) {

        try{

            $model->delete();
            return true;
        }
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function save($model) {

        try{

            $model->save();
            return true;
        }
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getInvitation($hash) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Invitation i')
                ->where('i.hash = ?',$hash)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getUserByEmail($email) {
    
        try{
            
            $query = Doctrine_Query::create()
            ->from('Model_User u')
            ->where('u.email = ?',$email)
            ;

            return $query->fetchOne();
        }
        
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getUserByProvider($provider_name,$provider_id) {
    
        try{
            
            $query = Doctrine_Query::create()
            ->from('Model_User u')
            ->where('u.provider_name = ?',$provider_name)
            ->andwhere('u.provider_id = ?',$provider_id)
            ;

            return $query->fetchOne();
        }
        
        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    
    public function getUser($id) {
    
    	try{
			
			$query = Doctrine_Query::create()
			->from('Model_User u')
			->where('u.id = ?',$id)
			;

			return $query->fetchOne();
		}
		
		catch(Exception $e){
			throw new App_Exception_Model($e->getMessage());
		}
    }
}