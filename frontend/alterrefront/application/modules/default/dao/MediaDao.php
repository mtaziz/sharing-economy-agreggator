<?php

class Dao_MediaDao extends App_Model_Dao {

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

    public function getMedia($media) {

        try{
            $query = Doctrine_Query::create()
                ->from('Model_CzMedia m')
                ->where('m.id = ?',$media)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}