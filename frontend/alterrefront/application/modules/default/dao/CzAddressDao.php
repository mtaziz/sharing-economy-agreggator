<?php

class Dao_CzAddressDao extends App_Model_Dao {

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
        
    public function getAddress($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_CzAddress a')
                ->where('a.id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}