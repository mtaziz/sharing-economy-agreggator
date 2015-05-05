<?php

class Dao_CategoryDao extends App_Model_Dao {

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
        
    public function getCategory($id) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Category c')
                ->where('c.id = ?',$id)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }
    public function getCategoryByName($name) {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Category c')
                ->where('c.name = ?',$name)
            ;

            return $query->fetchOne();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

    public function getAll($parent,$state="enable") {

        try{

            $query = Doctrine_Query::create()
                ->from('Model_Category c')
                ->orderBy('c.position ASC')
            ;

            if($parent!="all"){ $query->andwhere('c.parent = ?',$parent); }
            if($state!="enable"){ $query->andwhere('c.state = ?',$state); }

            return $query->execute();
        }

        catch(Exception $e){
            throw new App_Exception_Model($e->getMessage());
        }
    }

}