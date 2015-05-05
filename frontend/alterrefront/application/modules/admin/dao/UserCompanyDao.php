<?php

class Admin_Dao_UserCompanyDao extends App_Model_Dao {

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

}