<?php

class Dao_CzCommentDao extends App_Model_Dao {

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
        
    public function getComment($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_CzComment c')
                ->where('c.id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
   public function getCommentsByProject($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_CzComment c')
                ->where('c.project_id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}